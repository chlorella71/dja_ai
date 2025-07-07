# import
import os
import warnings

import implicit.als
import pandas as pd
import numpy as np
import pickle

from threadpoolctl import threadpool_limits
from scipy.sparse import lil_matrix, coo_matrix
from sklearn.decomposition import TruncatedSVD, NMF
from db_conn.postgres_db import conn_postgres_db # from은 모듈을 가지고 올때, from 디렉토리.파일 이름 import 함수 이름
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tqdm import tqdm

# from lightfm import LightFM
# from lightfm.data import Dataset
warnings.filterwarnings('ignore')

# df = pd.read_csv("data/ratings.dat", sep="::", engine='python')
# df.columns = ["userId", "movieId", "rating", "time"]
# with open("data/ratings.pkl", "wb") as f:   # f는 변수 선언
#     pickle.dump(df, f)
# exit()   # 여기까지만 실행하라는 뜻

# 함수
# def extract_high_rating_data(minimum_rating=3.5):
def extract_high_rating_data(minimum_rating=3.0):
    # with open("data/ratings.pkl", "wb") as f:  # f는 변수 선언
    with open("data/ratings.pkl", "rb") as f:  # 불러올 때는 wb, 읽을때는 rb
        df = pickle.load(f)
    # print(df)
    # users= df['userId'].value_counts().index[:1000] # groubby, 영화를 많이본사람 1000명 계산
    users= df['userId'].value_counts().index[:100] # groubby, 영화를 많이본사람 1000명 계산

    # print(users)
    movies = df['movieId'].value_counts().index[:]
    # print(movies)
    data= df[(df['userId'].isin(users)) & (df['movieId'].isin(movies)) & (df['rating'] >= minimum_rating)] # users에 userId가, movies에 movieId가 포함되는지
    # print(data)
    # data.rename(columns={"userId":"user_id", "movieId":"movie_id"}, inplace=True) #이건 컬럼명 다르게 지정한사람만
    # renamedData = data.rename(columns={"userId":"user_id", "movieId":"movie_id"}) #이건 컬럼명 다르게 지정한사람만

    # print(renamedData.keys())
    # exit()
    data = data.rename(columns={"userId":"user_id", "movieId":"movie_id"})
    return data
    # return renamedData

def svd_predict_model(matrix, users, degree):
    # pass
    # # 피봇 테이블 만들기   # 피봇팅은 다 해야하는 중복코드
    # pivot_rating = users.pivot_table(
    #     index="userId",
    #     columns="movieId",
    #     values="rating",
    #     fill_value=None  # 일단 모르니깐 0을 넣음 # 0대신 None을넣어서 아예 값에서 제외시킴
    # )
    # # 각열의 평균 구하기
    # random_mean = pivot_rating.mean(axis=0)
    # # 각열의 평균 넣기(None 값)
    # pivot_rating.fillna(random_mean, inplace=True) #df의 기능
    # matrix = pivot_rating.values
    # print(matrix)
    # exit()
    # svd(특이값 분해, 차원축소의 일종)
    svd = TruncatedSVD(n_components=degree, random_state=42) # random_state는 seed값, random으로 했을때 seed값을 뽑도록(만약 seed값이 성능이 좋았던 값(평점을 잘 준 값)이라면 그것을 계속 뽑도록), 42는 그냥 딥러닝에서 행운의 숫자처럼여겨져서 그런것
    # user_latent_matrix = svd.fit_transform(pivot_rating)
    user_latent_matrix = svd.fit_transform(matrix)
    # print(user_latent_matrix)
    item_latent_matrix = svd.components_
    #예측 머신러닝 모델 만들기
    predicted_ratings= user_latent_matrix @ item_latent_matrix # 식에 대한 이론도 알면 좋음, numpy 기능
    # print(predicted_ratings)
    # 피봇행렬(pivot)을 데이터프레임으로 만들기
    index = users["userId"].unique()
    columns = users["movieId"].unique()
    predicted_ratings_df=pd.DataFrame(
        predicted_ratings,
        index=index,
        columns=columns
    )
    # print(predicted_ratings_df)
    #피봇테이블(pivot) 해제해서 데이터 프레임
    unpivot_predicted_rating_df = predicted_ratings_df.stack().reset_index() # 피벗해제, df기능
    unpivot_predicted_rating_df.columns = ["userId", "movieId", "predicted_rating",]
    # print(unpivot_predicted_rating_df)
    return unpivot_predicted_rating_df

def nmf_predict_model(matrix, users, degree):
    # pass
    #정규화(단위맞추기)
    # scaler= StandardScaler() # 표준 정규분포로 정규화(마할라노비스 거리, (데이터 - 평균)/표준편차)
    # matrix=scaler.fit_transform(matrix) # 평균, 표준편차 계싼 후 모든데이터 표준화
    # matrix= np.maximum(matrix, 0)#음수값없애기(제곱)

    #사실 표준정규분포 맞출필요 없었음
    nmf = NMF(n_components=degree, random_state=42, init='random', max_iter=500, tol=1e-5) # 1e-5 1의 -5승

    P = nmf.fit_transform(matrix) # 사용자(행)의 잠재요인행렬
    Q = nmf.components_ #항목(열)의 잠재요인 행렬
    pred_model = P @ Q #내적 구함?, 행렬곱으로 원본 matrix를 근사복원?

    # 피봇행렬(pivot)을 데이터프레임으로 만들기
    index = users["userId"].unique()
    columns = users["movieId"].unique()
    predicted_ratings_df = pd.DataFrame(
        pred_model,
        index=index,
        columns=columns
    )
    # print(predicted_ratings_df)
    # 피봇테이블(pivot) 해제해서 데이터 프레임
    unpivot_predicted_rating_df = predicted_ratings_df.stack().reset_index()  # 피벗해제, df기능
    unpivot_predicted_rating_df.columns = ["userId", "movieId", "predicted_rating", ]
    # print(unpivot_predicted_rating_df)
    return unpivot_predicted_rating_df

def mf_predict_model(matrix, users, degree):
    pass # 딥러닝관련이라 지금 안할것?

# def imf_predict_model(users, minimum_num_ratings=4.0, factors=10, epochs=50): #최소점수는 4.0
def imf_predict_model(users, minimum_num_ratings=4.0, factors=10, epochs=50):  # 최소점수는 4.0

    """
      IMF(Implicit Matrix Factorization)를 사용한 협업 필터링 추천 시스템

      Args:
        users: 사용자-영화-평점 데이터프레임
        factors: ALS에서 사용할 잠재 요인 수
        minimum_num_ratings: 최소 평점 개수 (이보다 적은 상호작용을 가진 사용자/영화 제외)
        epochs: 학습 반복 횟수

      Returns:
        각 사용자별 상위 N개 추천 영화 리스트
      """

    # ================================
    # 1단계: 데이터 필터링
    # ================================
    # 최소 평점 개수 이상의 상호작용을 가진 사용자만 선택
    user_counts = users["userId"].value_counts()
    valid_users = user_counts[user_counts >= minimum_num_ratings].index

    # 최소 평점 개수 이상의 상호작용을 가진 영화만 선택
    movie_counts = users["movieId"].value_counts()
    valid_movies = movie_counts[movie_counts >= minimum_num_ratings].index

    # 필터링된 데이터만 사용
    filtered_users = users[
        (users["userId"].isin(valid_users)) & (users["movieId"].isin(valid_movies))]

    # ================================
    # 2단계: 인덱스 매핑 생성
    # ================================
    # 필터링된 데이터를 기반으로 인덱스 매핑 생성
    num_users = filtered_users["userId"].nunique()
    num_movies = filtered_users["movieId"].nunique()

    user_id2index = {
        user_id: i for i, user_id in enumerate(filtered_users["userId"].unique())}
    movie_id2index = {
        movie_id: i for i, movie_id in enumerate(filtered_users["movieId"].unique())}

    # ================================
    # 3단계: 희소 행렬 생성
    # ================================
    # 사용자-영화 상호작용 행렬 생성
    matrix = lil_matrix((num_users, num_movies))

    # 모든 평점을 1.0으로 변환 (상호작용 여부만 고려)
    for _, row in tqdm(filtered_users.iterrows(), total=len(filtered_users)):
        user_idx = user_id2index[row["userId"]]
        movie_idx = movie_id2index[row["movieId"]]
        matrix[user_idx, movie_idx] = 1.0

    # ================================
    # 4단계: CSR 형태로 변환
    # ================================
    # 희소 행렬을 CSR(Compressed Sparse Row) 형태로 변환 (연산 효율성)
    matrix_csr = matrix.tocsr()

    # ================================
    # 5단계: ALS 모델 학습
    # ================================
    # AlternatingLeastSquares: implicit feedback을 위한 행렬분해 알고리즘
    # factors: 잠재 요인의 개수 (차원 축소)
    # iterations: 학습 반복 횟수
    # calculate_training_loss: 학습 손실 계산 여부
    # random_state: 재현 가능한 결과를 위한 시드값
    model = implicit.als.AlternatingLeastSquares(
        factors=factors,
        iterations=epochs,
        calculate_training_loss=True,
        random_state=42
    )

    # ================================
    # 6단계: 모델 학습 실행
    # ================================
    # threadpool_limits: BLAS 스레드 수 제한 (메모리 안정성)
    with threadpool_limits(limits=4, user_api="blas"):
        model.fit(matrix_csr)

    # ================================
    # 7단계: 추천 결과 생성
    # ================================
    # 각 사용자별 상위 N개 영화 추천
    predicted_model = model.recommend_all(matrix_csr, N=10)

    # ================================
    # 8단계: DataFrame 형태로 변환
    # ================================
    # 추천 결과를 저장할 리스트
    recommendations = []

    # 인덱스를 원본 ID로 변환하기 위한 역매핑 생성
    index2user_id = {v: k for k, v in user_id2index.items()}
    index2movie_id = {v: k for k, v in movie_id2index.items()}

    # recommend_all 결과를 올바른 형태로 변환
    for user_idx in range(len(predicted_model)):
        original_user_id = index2user_id[user_idx]
        user_recommendations = predicted_model[user_idx]

        # 각 사용자의 추천 영화들을 처리
        for rank, movie_idx in enumerate(user_recommendations):
            original_movie_id = index2movie_id[movie_idx]

            # 추천 점수는 순위 기반으로 계산 후 0~5점 범위로 스케일링
            # 1위가 5점, 마지막 순위가 0점에 가깝게 설정
            normalized_score = 1.0 - (rank / len(user_recommendations))  # 0~1 범위
            predicted_score = normalized_score * 5.0  # 0~5점 범위로 변환

            recommendations.append({
                'user_id': original_user_id,
                'movie_id': original_movie_id,
                'predicted_rating': float(predicted_score)
            })

    # print(recommendations)

    # DataFrame으로 변환
    predicted_df = pd.DataFrame(recommendations)

    return predicted_df


    # num_users = users["userId"].nunique()
    # num_movies=users["movieId"].nunique()
    #
    # userIdToIndex={userId: idx for idx, userId in enumerate(users['userId'].unique())}
    # movieIdToIndex={movieId: idx for idx, movieId in enumerate(users['movieId'].unique())}
    #
    # matrix = lil_matrix((num_users, num_movies))
    # for _, row in tqdm(users.iterrows()):
    #     user_idx= userIdToIndex[row["userId"]]
    #     movie_idx= movieIdToIndex[row["movieId"]]
    #     matrix[user_idx, movie_idx] = 1.0  # 빈곳은 1.0으로 채움?
    #
    # matrix_csr = matrix.tocsr()
    #
    # model = implicit.als.AlternatingLeastSquares(
    #     factors=factors, iterations=epochs, calculate_training_loss=True, random_state=42
    # )
    #
    # with threadpool_limits(limits=1, user_api='blas'):
    #     model.fit(matrix_csr)
    #
    # predicted_model = model.recommend_all(matrix_csr)
    # print(predicted_model)

def bpr_predict_model(users, factors=10, minimum_num_ratings=4, epochs=50):
    """
      IMF(Implicit Matrix Factorization)를 사용한 협업 필터링 추천 시스템

      Args:
        users: 사용자-영화-평점 데이터프레임
        factors: ALS에서 사용할 잠재 요인 수
        minimum_num_ratings: 최소 평점 개수 (이보다 적은 상호작용을 가진 사용자/영화 제외)
        epochs: 학습 반복 횟수

      Returns:
        각 사용자별 상위 N개 추천 영화 리스트
      """

    # ================================
    # 1단계: 데이터 필터링
    # ================================
    # 최소 평점 개수 이상의 상호작용을 가진 사용자만 선택
    user_counts = users["userId"].value_counts()
    valid_users = user_counts[user_counts >= minimum_num_ratings].index

    # 최소 평점 개수 이상의 상호작용을 가진 영화만 선택
    movie_counts = users["movieId"].value_counts()
    valid_movies = movie_counts[movie_counts >= minimum_num_ratings].index

    # 필터링된 데이터만 사용
    filtered_users = users[
        (users["userId"].isin(valid_users)) & (users["movieId"].isin(valid_movies))]

    # ================================
    # 2단계: 인덱스 매핑 생성
    # ================================
    # 필터링된 데이터를 기반으로 인덱스 매핑 생성
    num_users = filtered_users["userId"].nunique()
    num_movies = filtered_users["movieId"].nunique()

    user_id2index = {
        user_id: i for i, user_id in enumerate(filtered_users["userId"].unique())}
    movie_id2index = {
        movie_id: i for i, movie_id in enumerate(filtered_users["movieId"].unique())}

    # ================================
    # 3단계: 희소 행렬 생성
    # ================================
    # 사용자-영화 상호작용 행렬 생성
    matrix = lil_matrix((num_users, num_movies))

    # 모든 평점을 1.0으로 변환 (상호작용 여부만 고려)
    for _, row in tqdm(filtered_users.iterrows(), total=len(filtered_users)):
        user_idx = user_id2index[row["userId"]]
        movie_idx = movie_id2index[row["movieId"]]
        matrix[user_idx, movie_idx] = 1.0

    # ================================
    # 4단계: CSR 형태로 변환
    # ================================
    # 희소 행렬을 CSR(Compressed Sparse Row) 형태로 변환 (연산 효율성)
    matrix_csr = matrix.tocsr()

    # ================================
    # 5단계: ALS 모델 학습
    # ================================
    # AlternatingLeastSquares: implicit feedback을 위한 행렬분해 알고리즘
    # factors: 잠재 요인의 개수 (차원 축소)
    # iterations: 학습 반복 횟수
    # calculate_training_loss: 학습 손실 계산 여부
    # random_state: 재현 가능한 결과를 위한 시드값
    model = implicit.bpr.BayesianPersonalizedRanking(
        # factors=factors,
        # iterations=epochs,
        # calculate_training_loss=True,
        # random_state=42
        factors=100,
        learning_rate=0.01,
        regularization=0.01,
        iterations=100,
        # calculate_training_loss=True,
        random_state=42
    )

    # ================================
    # 6단계: 모델 학습 실행
    # ================================
    # threadpool_limits: BLAS 스레드 수 제한 (메모리 안정성)
    with threadpool_limits(limits=4, user_api="blas"):
        model.fit(matrix_csr)

    # ================================
    # 7단계: 추천 결과 생성
    # ================================
    # 각 사용자별 상위 N개 영화 추천
    predicted_model = model.recommend_all(matrix_csr, N=10)

    # ================================
    # 8단계: DataFrame 형태로 변환
    # ================================
    # 추천 결과를 저장할 리스트
    recommendations = []

    # 인덱스를 원본 ID로 변환하기 위한 역매핑 생성
    index2user_id = {v: k for k, v in user_id2index.items()}
    index2movie_id = {v: k for k, v in movie_id2index.items()}

    # recommend_all 결과를 올바른 형태로 변환
    for user_idx in range(len(predicted_model)):
        original_user_id = index2user_id[user_idx]
        user_recommendations = predicted_model[user_idx]

        # 각 사용자의 추천 영화들을 처리
        for rank, movie_idx in enumerate(user_recommendations):
            original_movie_id = index2movie_id[movie_idx]

            # 추천 점수는 순위 기반으로 계산 후 0~5점 범위로 스케일링
            # 1위가 5점, 마지막 순위가 0점에 가깝게 설정
            normalized_score = 1.0 - (rank / len(user_recommendations))  # 0~1 범위
            predicted_score = normalized_score * 5.0  # 0~5점 범위로 변환

            recommendations.append({
                'user_id': original_user_id,
                'movie_id': original_movie_id,
                'predicted_rating': float(predicted_score)
            })

    # print(recommendations)

    # DataFrame으로 변환
    predicted_df = pd.DataFrame(recommendations)

    return predicted_df

    # num_users = users["userId"].nunique()
    # num_movies=users["movieId"].nunique()
    #
    # userIdToIndex={userId: idx for idx, userId in enumerate(users['userId'].unique())}
    # movieIdToIndex={movieId: idx for idx, movieId in enumerate(users['movieId'].unique())}
    #
    # matrix = lil_matrix((num_users, num_movies))
    # for _, row in tqdm(users.iterrows()):
    #     user_idx= userIdToIndex[row["userId"]]
    #     movie_idx= movieIdToIndex[row["movieId"]]
    #     matrix[user_idx, movie_idx] = 1.0  # 빈곳은 1.0으로 채움?
    #
    # matrix_csr = matrix.tocsr()
    #
    # model = implicit.als.AlternatingLeastSquares(
    #     factors=factors, iterations=epochs, calculate_training_loss=True, random_state=42
    # )
    #
    # with threadpool_limits(limits=1, user_api='blas'):
    #     model.fit(matrix_csr)
    #
    # predicted_model = model.recommend_all(matrix_csr)
    # print(predicted_model)

def fm_predict_model(users, factors=10, minimum_num_ratings=4, epochs=30):
    # 1단계: 유효 사용자/영화 필터링
    user_counts = users["userId"].value_counts()
    movie_counts = users["movieId"].value_counts()

    valid_users = user_counts[user_counts >= minimum_num_ratings].index
    valid_movies = movie_counts[movie_counts >= minimum_num_ratings].index

    filtered_users = users[
        (users["userId"].isin(valid_users)) & (users["movieId"].isin(valid_movies))
        ]

    # 2단계: user_id, movie_id 인덱싱
    user_ids = filtered_users["userId"].astype("category")
    movie_ids = filtered_users["movieId"].astype("category")

    user_index = user_ids.cat.codes.values
    movie_index = movie_ids.cat.codes.values
    num_users = len(user_ids.cat.categories)
    num_movies = len(movie_ids.cat.categories)

    # 3단계: 상호작용 행렬 생성 (암묵적 피드백)
    interactions = coo_matrix((np.ones_like(user_index), (user_index, movie_index)), shape=(num_users, num_movies))

    # 4단계: LightFM (FM 모델) 학습
    model = LightFM(no_components=factors, loss='bpr', random_state=42)
    # model.fit(interactions, epochs=epochs, num_threads=4)
    # model.fit(interactions, epochs=epochs, num_threads=1)
    model.fit(interactions, epochs=epochs, num_threads=os.cpu_count())


    # 5단계: 추천 생성
    recommendations = []
    index2user_id = dict(enumerate(user_ids.cat.categories))
    index2movie_id = dict(enumerate(movie_ids.cat.categories))

    for user_idx in range(num_users):
        scores = model.predict(user_idx, np.arange(num_movies))
        top_items = np.argsort(-scores)[:10]

        for rank, item_idx in enumerate(top_items):
            predicted_score = (1.0 - (rank / 10)) * 5.0
            recommendations.append({
                'user_id': index2user_id[user_idx],
                'movie_id': index2movie_id[item_idx],
                'predicted_rating': float(predicted_score)
            })

    return pd.DataFrame(recommendations)

# 실행
if __name__ == "__main__":
    # pass
    # with open("data/ratings.pkl", "wb") as f:  # f는 변수 선언
    # with open("data/ratings.pkl", "rb") as f:  # 불러올 때는 wb, 읽을때는 rb
    #     df = pickle.load(f)
    # print(df["userId"].unique().shape)
    # print(df["movieId"].unique().shape)
    # exit()

    # users =df[(df["userId"] >=1) & (df["userId"] <= 1001)] # df 기능
    # print(users)
    # exit()

    users = extract_high_rating_data()


    # 피봇 테이블 만들기  # 매번 사용될 중복코드이므로 실행하는곳에서 사용
    pivot_rating = users.pivot_table(
        index="userId",
        columns="movieId",
        values="rating",
        fill_value=None  # 일단 모르니깐 0을 넣음 # 0대신 None을넣어서 아예 값에서 제외시킴
    )
    # 각열의 평균 구하기
    random_mean = pivot_rating.mean(axis=0)
    # # 각열의 평균 넣기(None 값)
    pivot_rating.fillna(random_mean, inplace=True)  # df의 기능
    matrix = pivot_rating.values

    # matrix = svd_predict_model(users, 10)
    # users_df = svd_predict_model(users, 10)
    # print(users_df)
    # users_df = svd_predict_model(matrix, users, 10) # matrix도 같이 넘겨 줌
    # print(users_df)

    # conn_postgres_db(users_df, "postgres", 111, "mydb", "svd_model")
    # conn_postgres_db(users_df, "kogo", 111, "mydb", "svd_model")


    # users_df = nmf_predict_model(matrix, users, 10)  # matrix도 같이 넘겨 줌
    # print(users_df)

    # conn_postgres_db(users_df, "postgres", 111, "mydb", "nmf_model")
    # conn_postgres_db(users_df, "postgres", 111, "mydb", "nmf_model")
    # conn_postgres_db(users_df, "kogo", 111, "mydb", "nmf_model")


    # users_df=imf_predict_model(users)
    # print(users_df)

    # conn_postgres_db(users_df, "postgres", 111, "mydb", "imf_model")
    # conn_postgres_db(users_df, "kogo", 111, "mydb", "imf_model")

    # users_df=bpr_predict_model(users)
    # print(users_df)
    # conn_postgres_db(users_df, "postgres", 111, "mydb", "bpr_model")


    users_df = fm_predict_model(users)
    print("✅ users_df shape:", users_df.shape)
    print(users_df.head(3))
    # print(users_df)

    # users_df = extract_high_rating_data()
    # print(users_df.shape)
    # users_df=imf_predict_model(users_df)
    # print(users_df)
    # print(users_df[users_df["user_id"]==143])

    # print(users["userId"].unique().shape)
    # print(users["movieId"].unique().shape)

    # exit()

    # pivot_rating = users.pivot_table(
    #         index="userId",
    #         columns="movieId",
    #         values="rating",
    #         fill_value=None   # 일단 모르니깐 0을 넣음 # 0대신 None을넣어서 아예 값에서 제외시킴
    # )
    # print(pivot_rating)
    # random_mean= pivot_rating.mean(axis=0)
    # print(random_mean)
    # print(random_mean.shape)

    # print(pivot_rating[1])
    # print(random_mean[1])
    # pivot_rating[1].apply(lambda x: random_mean[1])  # fill_value값에 random_mean[1]을 넣으려고 했으나 immutable이라 값이 들어가지 않음
    # print(pivot_rating[1])
    # pivot_rating[1] = pivot_rating[1].apply(lambda x: random_mean[1]) # drop하고 ?는 immuatble?
    # print(pivot_rating[1])
    # pivot_rating.fillna(random_mean, inplace=True) # 각 평균을 알아서 넣게끔 해줌, inplace는 원본데이터를 수정할 수 있게 해줌
    # print(pivot_rating)
