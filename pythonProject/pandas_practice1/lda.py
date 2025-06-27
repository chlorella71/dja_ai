import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.decomposition import PCA
iris = load_iris()

if __name__ == "__main__":
    X= iris.data    #data를 입력값과 정답값으로 나눔
    y = iris.target
    # print(X ,y)
    normalization = MinMaxScaler()
    X_normal = normalization.fit_transform(X) ## 정규화
    # print(X_normal)
    y_reshape = iris.target.reshape(-1,1) #배열을 2차원(행렬모양)으로 변환
    onehotencoding = OneHotEncoder(sparse_output=False)
    y_oneHot = onehotencoding.fit_transform(y_reshape)
    # print(y_oneHot)

    # print(iris.target_names)
    setosa= X_normal[:50, :]
    versicolor = X_normal[50: 100, :]
    virginica = X_normal[100:, :]
    # print(setosa.shape, versicolor.shape, virginica.shape)

    setosa_cov= np.cov(setosa.T)
    versicolor_cov= np.cov(versicolor.T)
    virginica_cov= np.cov(virginica.T)
    # print(setosa_cov.shape, versicolor_cov.shape, virginica_cov.shape)

    SW = setosa_cov + versicolor_cov + virginica_cov
    # print(SW)

    setosa_mean = np.mean(setosa, axis=0)
    versicolor_mean = np.mean(versicolor, axis=0)
    virginica_mean = np.mean(virginica, axis=0)
    # print(setosa_mean, versicolor_mean, virginica_mean)

    mean_matrix= np.vstack((setosa_mean, versicolor_mean, virginica_mean))
    # print(mean_matrix.shape)

    SB = np.cov(mean_matrix.T)
    # print(SB)

    inv_SW = np.linalg.inv(SW)
    W= SB @ inv_SW
    # print(W)

    #원본을 곱하면 됨?
    transX = X_normal @ W
    # print(transX.shape)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(transX)
    # print(X_pca.shape)

    # 시각화
    colors = ['r', 'g', 'b']
    target_names = iris.target_names

    for i, target_name in enumerate(target_names):
        plt.scatter(X_pca[iris.target == i, 0],
                    X_pca[iris.target == i, 1],
                    c=colors[i], label=target_name, alpha=0.8)
    plt.xlabel("Principal Component1")
    plt.xlabel("Principal Component2")
    plt.title("20 PCA of Iris Dataset")
    plt.legend()
    plt.grid(True)
    plt.show()