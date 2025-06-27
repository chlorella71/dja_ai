import pandas as pd
import numpy as np
from pyexpat import features
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


if __name__ == "__main__":
    iris =load_iris() # 데이터가져오기
    # print(iris.keys())
    df =pd.DataFrame(iris.data, columns=iris.feature_names) # 필드 붙이기
    # print(df)

    # 넘파이 행렬식
    matrix =df.values # 행렬로 만들기(numpy배열로 반환)
    # print(matrix)
    X = df.values

    # 정규화
    X = (X-np.min(X))/(np.max(X)-np.min(X))

    # 공분산
    cov = (X-np.mean(X)).T @ (X-np.mean(X))# 공분산 구하기, T는 transpose, @는 곱하기(matrix에서)
    # print(cov.shape)

    # 고유값, 고유벡터
    eigenvalues, eigenvectors = np.linalg.eig(cov) # 공분산의 고유값 고유벡터 구하기
    # print("\n고윳값:\n", eigenvalues)
    # print("\n고유벡터:\n", eigenvectors)

    # 내림차순 정리
    idx = eigenvalues.argsort()[::-1]  # 열(가로줄)을 내림차순으로 정렬
    # print(idx)
    eigenvalues = eigenvalues[idx] # 고유값을 정렬한idx로 출력
    eigenvectors = eigenvectors[:, idx] # 고유벡터를 정렬한 idx로 출력, [행, 열]
    # print(eigenvalues)
    # print(eigenvectors)

    # 차원 2차원으로 축소
    transformer = eigenvectors[:2, :]  ##(잘못출력함) 2차원 행렬로 축소하기
    # print("선형변화벡터", transformer)
    # print(X.shape)   # transform할 위치 확인하기
    # print(transformer.shape)
    transX = X@transformer.T
    # print(transX)
    transformer = eigenvectors[:, :2] ##(이게 제대로)
    # print("선형변화벡터", transformer)
    transX = X @ transformer
    # print(transX)

    # 시각화
    colors = ['r', 'g', 'b']
    target_names = iris.target_names

    for i, target_name in enumerate(target_names):
        plt.scatter(transX[iris.target == i, 0],
                    transX[iris.target == i, 1],
                    c=colors[i], label=target_name, alpha=0.8)
    plt.xlabel("Principal Component1")
    plt.ylabel("Principal Component2")
    plt.title("20 PCA of Iris Dataset")
    plt.legend()
    plt.grid(True)
    plt.show()