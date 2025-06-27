import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


if __name__ == "__main__":
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # 넘파이 행렬식
    X = df.values

    # 정규화
    X = (X - np.min(X)) / (np.max(X) - np.min(X))

    # 공분산
    cov = (X-np.mean(X)).T @ (X-np.mean(X))

    # 고유값, 고유벡터
    eigenvalues, eigenvectors = np.linalg.eig(cov)

    # 내림차순 정리
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    # print(eigenvalues)
    # print(eigenvectors)
    # print(idx)
    # print("\n고윳값:\n", eigenvalues)
    # print("\n고유벡터:\n", eigenvectors)

    # 차원 2원으로 축소
    transformer = eigenvectors[:, :2]
    # # print("선형변화벡터", transformer)
    transX = X@transformer
    # print(transX)

    # 시각화
    colors = ['r', 'g', 'b']
    target_names = iris.target_names

    for i, target_name in enumerate(target_names):
        plt.scatter(transX[iris.target == i, 0],
                    transX[iris.target == i, 1],
                    c=colors[i], label=target_name, alpha=0.8)
    plt.xlabel("Principal Component1")
    plt.xlabel("Principal Component2")
    plt.title("2D PCA of Iris Dataset")
    plt.legend()
    plt.grid(True)
    plt.show()