import pandas as pd
import numpy as np # numpy는 계산할때 쓰는것
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns =iris.feature_names)
    # print(df)

    ## matrix(행렬) 만들기
    matrix= df.values
    # print(matrix)
    # print(matrix.shape)
    # exit()

    ## 각 평균 구하기
    means = df.mean(axis=0)
    # print(means)
    # print(means.shape)
    # exit()

    ## 각 데이터에셔 평균빼기
    xminusmean = matrix - means.values # mean이 df형태라 행렬로 바꿔야함
    # print(xminusmean)
    # print(xminusmean.shape)

    ## 공분산구하기
    cov= xminusmean.T @ xminusmean # T는 전치행렬 @는 numpy 행렬곱을 의미
    # print(cov)

    ## 고유값, 고유벡터구하기
    eigen_values, eigen_vectors = np.linalg.eig(cov)
    # print(eigen_values) # 가중치
    # print(eigen_vectors) # 미지의 데이터의 축

    ## 차원축소
    dimension_decrease = eigen_vectors[:, :2] # 가중치가 큰 축만 가져오기, 행은 첫번째거 열은 2개 가져오면 됨?, numpy와 pandas는 한몸, python문법의 slicing사용됨, 여기선 loc이 사용안됨?
    # print(eigen_vectors) # 미지의 데이터의 축
    # print(dimension_decrease)
    new_X = xminusmean @ dimension_decrease
    # print(new_X) # 차원을 축소해서 새로운 차원을 찾음, 선형 변환

    ## 시각화
    plt.figure(figsize=(10, 7))
    colors=['red', 'green', 'blue']
    target_names= iris.target_names
    for i, target_name in enumerate(target_names):
        plt.scatter(
            new_X[iris.target==i, 0], # 0번이면 0번필드만
            new_X[iris.target==i, 1], # 1번이면 1번필드만
            label=target_name, # label은 정답을 의미
            alpha=0.8 # 흐림 정도
        )
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("PCA of Iris Dataset")
    plt.legend() # 상단오른쪽에 그룹 표시
    plt.grid(True) # 모눈종이 효과
    plt.show()