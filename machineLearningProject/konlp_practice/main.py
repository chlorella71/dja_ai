import warnings

import pandas as pd
import numpy as np
import seaborn as sns
import pickle
import re
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report
# classfication_report : 성능이 어느정도 되는지 분석해줌

from korean_encoding import korean_font_config
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
# warnings.filterwarnings("ignore") # waring message를 무시하게 해줌

def preprocessing_embeddings():
    df = pd.read_excel("data/NAVER-Webtoon_OSMU.xlsx")
    feature_names = ['synopsis', 'genre']
    df = df[feature_names]

    embedder = SentenceTransformer('sentence-transformers/xlm-r-base-en-ko-nli-ststb')
    X_embeddings = embedder.encode(
        df['synopsis'].tolist(),
        convert_to_tensor=False,
        show_progress_bar=True
    )

    df["synopsis_embeddings"] = list(X_embeddings)

    with open("data/synopsis_embedding_df.pkl", "wb") as file:
        pickle.dump(df, file)

def visualization_pca(df):
    embedding_matrix = np.vstack(df['synopsis_embeddings'].values)

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(embedding_matrix)

    plt.figure(figsize=(12, 10))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.5, s=30)
    plt.title("synopsis 2차원 시각화", fontsize=16)
    plt.xlabel("pca component 1", fontsize=12)
    plt.ylabel("pca component 2", fontsize=12)
    plt.grid()
    plt.savefig("data/synopsis_scatter.png")
    # plt.show()

    return pca_result

def visulization_kmeans(df):
    pca_result = visualization_pca(df)

    df['pca_x'] = pca_result[:, 0]
    df['pca_y'] = pca_result[:, 1]

    X = df[['pca_x', "pca_y"]]
    kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
    kmeans.fit(X)

    df['label'] = kmeans.labels_

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='pca_x', y='pca_y', data=df, hue='label', palette='viridis')
    plt.title("synopsis_4_label_시각화")
    plt.grid()
    plt.savefig('data/synopsis_4_label_시각화.png')
    # plt.show()

    return df

def visulization_lda(df):
    df = visulization_kmeans(df)
    X = np.vstack(df['synopsis_embeddings'].values)
    y = df['label'].values

    lda = LDA(n_components=2)
    lda_result = lda.fit_transform(X, y)

    df['lda_x'] = lda_result[:, 0]
    df['lda_y'] = lda_result[:, 1]

    plt.figure(figsize=(12, 10))
    sns.scatterplot(x='lda_x', y='lda_y', data=df, hue='label', palette='viridis', s=50, alpha=.8)
    plt.title("synopsis_4_label_lda_시각화", fontsize=16)
    plt.xlabel("lda component 1", fontsize=12)
    plt.ylabel('lda component 2', fontsize=12)
    plt.grid(True)
    plt.savefig("data/synopsis_4_label_lda_시각화.png")
    # plt.show()

    return df

def put_label_genres(df):
    df = visulization_lda(df)

    # apply는 자동으로 for문을 돔
    label_to_genre_counts = df.groupby('label')['genre'].sum().apply(
        # lambda text: Counter(re.findall(r'[A-Z]*', text)).most_common()
        lambda text: Counter(re.findall(r'[A-Z]+', text)).most_common()
    )
    df['label_genre'] = df['label'].map(label_to_genre_counts)

    return df

def accuracy_analytics(df):
    df = put_label_genres(df)

    X = np.vstack(df['synopsis_embeddings'].values)  # arrays를 만드는 방법은 여러가지, values, tolist(), ...
    y = df['label'].values  # y는 label

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,  # test_size를 보통 8:2 정도로 나눔
        random_state=42,
        stratify=y)

    # support vector machine 사용해보기
    svm_model = SVC(kernel='rbf', C=1.0, random_state=42, probability=True)  # model이라고 해도 되고 machine이라고 해도 됨
    svm_model.fit(X_train, y_train)

    return svm_model

if __name__ == "__main__":
    korean_font_config()
    with open("data/synopsis_embedding_df.pkl", "rb") as file:
        df = pickle.load(file)

    # 함수로 만들어서 사용해보기
    df = visulization_lda(df)
    df = put_label_genres(df)
    # print(df)
    # print(df.keys())
    svm_model = accuracy_analytics(df)



    genre_series = df.groupby('label')['genre'].sum()
    genre_list = []
    for genre in genre_series:
        word_list = re.findall(r'[A-Z]+', genre)
        genre_list.append(word_list)
    # print(len(genre_list))
    # sorted_genre_dict_series = genre_series.apply(lambda c: dict(c.most_common()))
    # print(sorted_genre_dict_series)

##---- 여기부터 수업 들음

    ## 정규식
    text = "[ 'a' ][ 'b' ][ 'c' ]"  # 정규식: 문자열을 다루는 방법(어떤 언어든 동일)
    result = re.findall(r'[a-z]*', text)
    # print(result)
    result = re.findall(r'[^a-z]*', text)
    # print(result)

    # collections라이브러리 Counter는 숫자를 셀 수 있음
    test = [ 'a', 'a', 'b', 'b', 'c']
    result = Counter(text)
    # print(result)

    # 가장 많이 나온 것 구하기(튜플 식으로 나옴)
    text = ['a', 'a', 'a', 'b', 'b', 'c']
    result = Counter(text).most_common()
    # print(result)

    # apply는 자동으로 for문을 돔
    label_to_genre_counts = df.groupby('label')['genre'].sum().apply(
        # lambda text: Counter(re.findall(r'[A-Z]*', text)).most_common()
        lambda text: Counter(re.findall(r'[A-Z]+', text)).most_common()
    )

    df['label_genre'] = df['label'].map(label_to_genre_counts)
    # print(df[['label', 'label_genre']])

    df = put_label_genres(df)
    # print(df)
    # print(df.keys())

#--- 머신 만들어보기

    # X = np.vstack(df['synopsis_embeddings'].tolist())
    X = np.vstack(df['synopsis_embeddings'].values) # arrays를 만드는 방법은 여러가지, values, tolist(), ...
    # print(X)
    y = df['label'].values # y는 label

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2, # test_size를 보통 8:2 정도로 나눔
        random_state=42,
        stratify=y)

    # support vector machine 사용해보기
    svm_model = SVC(kernel='rbf', C=1.0, random_state=42, probability=True)# model이라고 해도 되고 machine이라고 해도 됨
    svm_model.fit(X_train, y_train)

    y_pred = svm_model.predict(X_test) # 예측값
    accuracy = accuracy_score(y_pred, y_test) # 정답과 정답사이의 차이(정확도) 계산해보기
    # print(f"정확도: {accuracy:.4f}")
    analytics = classification_report(y_test, y_pred)
    # print(analytics)

#--- 예시 문장을 넣어 직접 테스트해보기
    svm_model = accuracy_analytics(df)
    # 예시 문장 만들기
    synopsis = "평범한 대학생 지훈은 우연히 손에 넣은 오래된 스마트폰을 통해 과거와 연결되며, 미래를 바꾸기 위한 예측 불가능한 모험에 뛰어든다."
    # embedding 해주어야 함
    embedder = SentenceTransformer('sentence-transformers/xlm-r-base-en-ko-nli-ststb')
    X_embeddings = embedder.encode(
        [synopsis], # synopsis를 list형태로 넣기
        convert_to_tensor=False,
        show_progress_bar=True
    )
    # X_embeddings 값을 arrays형태로 변환?
    X_embeddings = np.array(X_embeddings).reshape(1, -1)
    # 예측값? 구해보기
    y_pred = svm_model.predict(X_embeddings)
    # print(y_pred)
    # label 찍어보기
    # print(df[['label', 'label_genre']])
    # synopsis에 대한 예측값은 2, 2번은 drama와 fantasy가 높게 나옴

    # synopsis 10개 만들어서 테스트해보기
    synopsises = [
        '평범한 여대생 수지는 동아리에서 만난 차가운 선배에게 점점 끌리게 되고, 두 사람은 서로 다른 성격 때문에 갈등하지만 결국 진심을 확인하게 된다.',
        '고아 소년 민호는 숲에서 발견한 신비한 검을 통해 왕국의 잃어버린 전설과 마주하게 되고, 동료들과 함께 세상을 구하기 위한 여정을 시작한다.',
        '직장에서 해고당한 아버지와 가출한 딸이 우연히 길에서 재회하며, 서로의 상처를 이해하고 가족의 의미를 다시 찾아간다.',
        '작은 마을에서 연쇄 실종 사건이 발생하고, 초보 형사 지훈은 아무도 믿을 수 없는 상황 속에서 진실을 쫓는다.',
        '회사에 막 입사한 인턴은 매일 엉뚱한 실수를 반복하지만, 특유의 밝은 성격으로 주변 동료들의 마음을 사로잡는다.',
        '시간 여행 능력을 가진 여주인공이 과거의 왕자와 현재의 남자를 동시에 사랑하게 되면서, 두 세계 사이에서 선택을 해야 하는 운명에 놓인다.',
        '인공지능이 모든 것을 지배하는 미래 사회에서, 감정을 되찾은 로봇과 인간 저항군 소녀가 함께 자유를 꿈꾸며 싸운다.',
        '오래된 기숙사에 이사 온 학생들은 한밤마다 들려오는 알 수 없는 발자국 소리에 시달리며, 점점 어두운 진실을 마주한다.',
        '농구를 전혀 못하던 소년은 열정과 노력으로 팀의 주전 선수가 되고, 전국 대회에서 운명을 건 시합에 나선다.',
        '결혼을 앞둔 두 연인이 각자의 꿈을 위해 갈등하다가, 결국 서로를 위해 희생하는 선택을 하게 된다.'
    ]
    embedder = SentenceTransformer('sentence-transformers/xlm-r-base-en-ko-nli-ststb')
    X_embeddings = embedder.encode(
        synopsises,  # synopsis를 list형태로 넣기
        convert_to_tensor=False,
        show_progress_bar=True
    )
    # X_embeddings = np.array(X_embeddings).reshape(1, -1) # 문장 1개일때
    X_embeddings = np.array(X_embeddings) # 문장이 여러개일때
    y_pred = svm_model.predict(X_embeddings)
    for s, p in zip(synopsises, y_pred):
        print(f"[예측] {p} | 문장: {s}")
    print(df[['label', 'label_genre']])


