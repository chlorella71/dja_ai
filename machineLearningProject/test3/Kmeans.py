import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler as Scaler # 표준정규화(마할라노비스거리로 정규화), 평균 0, 분산 1
from sklearn.cluster import KMeans
# import는 모듈전체가져오기
# from module import name은 모듈 내부의 특정 항목만 가져오기


if __name__=="__main__":
    # sklearn의 dataset에서 load_iris라이브러리 함수로 iris data 가져오기
    iris=load_iris()

    # [[], [], []] 형태를 dataframe 형태로 변환
    df = pd.DataFrame(iris.data, columns=iris.feature_names) #labeling(결과값도출)을 하지않고 data만 모은상태

    # 정규화(표준정규분포 정규화), 보통 0, 1사이의 값으로 scailing이 되어있지만, 혹시 모르니 StandardScaler로 0과 1사이의 값으로 표준정규화
    scaler = Scaler() # StandardSclaer 클래스를 호출하기위해 인스턴스 만들기
    normalization = scaler.fit_transform(df) # 정규화하여 변수에 담기
    # print(normalization)
    # exit()


    # 그래프 시각화를 위해 PCA(주성분분석)기법으로 2차원으로 축소
    pca = PCA(n_components=2)
    matrix = pca.fit_transform(df)
    # print(matrix)
    df['feature1'] = matrix[:, 0] # DataFrame에 담은 전체 데이터를 다 가져와서 matrix의 0번을 feature1으로 붙임
    df['feature2'] = matrix[:, 1]
    # print(df)

    ## Kmeans 적용(여기만 빼면 pca)
    # 군집(clusters)은 3개로 해보겠음, 초기 중심점 설정을 고정하기 위한 랜덤시드는 42(결과를 재현가능하게 해줌?)
    kmeans = KMeans(n_clusters=3, random_state=42) # random_state값을 바꾸면 군집 분류가 변함, 이를 이용하여 원하는 군집을 찾을 수 있음?
    df['cluster_label'] = kmeans.fit_predict(matrix)
    # Kmeans가 찾은 각 군집의 중심점좌표(centroids)를 가져오기
    centroids= kmeans.cluster_centers_
    # print(centroids)
    # exit()

    ## 그래프 그리기
    # matplotlib 시각화 라이브러리를 이용하여 그래프 틀 만들기
    plt.figure(figsize=(10, 7))
    # Seaborn 시각화 라이브러리를 이용하여 데이터의 두 특성(feature1, featur2)를 기준으로 산점도(scatter plot)를 그리기
    sns.scatterplot(
        data=df,
        x='feature1',
        y='feature2',
        hue='cluster_label', # kmeans꺼(pca때는 주석처리)
        palette='viridis', # 군집별로 색 나누기(pca때는 적용안됨)
        s=100,
        alpha=0.8,
        # color='blue'
        # color='green' (pca할때 색지정할 수 있음)
    )
    # Kmeans의 각 군집의 중심점(centroid)의 좌표 찍기(pca때는 주석처리)
    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        c='red',
        marker='X',
        s=200,
        label="Centroid"
    )
    plt.title("PCA Scatter Plot(No Clustering)") # plot은 그래프라는 뜻 No clustring는 비지도학습
    plt.title("PCA Scatter Plot(KMeans Clustering)") # plot은 그래프라는 뜻 KMeans Clustring는 kmeans를 사용했다는 뜻
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend(title='Clusters')
    plt.grid(True) # 모눈종이 배경
    plt.show()