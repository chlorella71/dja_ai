from sklearn.datasets import load_iris
import pandas as pd # 데이터정제용
import numpy as np # 산술계산?


def mahalanobis_np(x, mean, inv_cov):
    # return (x-mean).T @ inv_cov @ (x-mean) # 마할라노비스 거리의 공식?
    return np.sqrt((x-mean).T @ inv_cov @ (x-mean)) # 숫자가 크면 루트 넣기(제곱된 값이라?)



if __name__=="__main__":
    # pass

    # iris data 가져오기
    iris = load_iris() # data는 json구조로 오게됨, json구조라는 것은 dictionary형태라는 것
    # print(iris.keys()) # fields를 출력해보기, target은 labeling 할 data

    # dataframe에 넣기
    iris_df= pd.DataFrame(iris.data, columns=iris.feature_names)
    # print(iris_df)

    iris_df["label"] = iris.target
    # print(iris_df)

    # target_names 확인
    # print(iris.target_names)

    setosa_train = iris_df.iloc[:45, :-1] # 0~44인덱스, 마지막거 뽑기(-1) -> 라벨링된 마지막꺼 뺀다는뜻?, train용 test data용는 분리해야함?
    setosa_test = iris_df.iloc[45:50, :-1] # 마지막꺼 5개 뽑기(테스트용)
    setosa_label= iris_df.iloc[45:50, -1] # 테스트용 5개의 정답
    # print(setosa_test)
    # print(setosa_label)

    versicolor_train = iris_df.iloc[50:95, :-1]
    versicolor_test= iris_df.iloc[95:100, :-1]
    versicolor_label= iris_df.iloc[95:100, -1]
    virginica_train = iris_df.iloc[100:145, :-1]
    virginica_test = iris_df.iloc[145:, :-1] # ::되면 거꾸로됨?
    virginica_label = iris_df.iloc[145:, -1]

    # 특징을 알려면 평균과 공분산을 구해야함?
    setosa_train_mean= setosa_train.mean(axis=0)
    setosa_train_covariance = np.cov(setosa_train.T) # covariance는 공분산?, T는 90도로 꺾기?
    setosa_train_cov_inv = np.linalg.inv(setosa_train_covariance) # 역행렬구하기?
    # setosa_train_cov_inv_det = np.linalg.det(setosa_train_cov_inv)
    # print(setosa_train_mean)
    # print(setosa_train_covariance)
    # print(setosa_train_mean.shape)
    # print(setosa_train_covariance.shape)
    # print(setosa_train_cov_inv_det)

    versicolor_train_mean = virginica_train.mean(axis=0)
    versicolor_train_covariance = np.cov(versicolor_train.T)
    versicolor_train_cov_inv = np.linalg.inv(versicolor_train_covariance)  # 역행렬구하기?

    virginica_train_mean = virginica_train.mean(axis=0)
    virginica_train_covariance = np.cov(virginica_train.T)
    virginica_train_cov_inv = np.linalg.inv(virginica_train_covariance)  # 역행렬구하기?

    mu = setosa_train_mean.values
    # print(mu)
    inv_cov= setosa_train_cov_inv
    test= setosa_test.values[0]
    # print(test)
    distance = test - mu
    # print(distance)
    distance = (test - mu).T @ inv_cov
    # print(distance)
    distance = distance @ (test - mu)
    # print(distance)

    se_mu = setosa_train_mean.values
    se_inv_cov = setosa_train_cov_inv
    ve_mu = versicolor_train_mean.values
    ve_inv_cov = versicolor_train_cov_inv
    vi_mu = virginica_train_mean.values
    vi_inv_cov = virginica_train_cov_inv

    # test = setosa_test.values[0]
    test = versicolor_test.values[0]
    # test = virginica_test.values[0]
    se_distance = (test - se_mu).T @ se_inv_cov @ (test - se_mu)
    ve_distance = (test - ve_mu).T @ ve_inv_cov @ (test - ve_mu)
    vi_distance = (test - vi_mu).T @ vi_inv_cov @ (test - vi_mu)
    # print(se_distance, ve_distance, vi_distance)

    # 함수 이용
    test= setosa_test.values[0]
    se_se_result = mahalanobis_np(test, se_mu, se_inv_cov)
    se_ve_result = mahalanobis_np(test, ve_mu, ve_inv_cov)
    se_vi_result = mahalanobis_np(test, vi_mu, vi_inv_cov)
    # print(se_se_result, se_ve_result, se_vi_result)

    test= setosa_test.values[0]
    # print(test)
    se_result = se_mu * test # 내적?
    # print(se_result)
    se_result = se_mu @ test # 행렬곱으로 내적이 구해짐
    # print(se_result)
    ve_result = ve_mu @ test
    vi_result = vi_mu @ test
    print(se_result, ve_result, vi_result) # 내적은 크면 클수록 관련성이 큰데, test의 값이 좋지 않음...