import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


if __name__ == "__main__":
    # # 데이터 가져와서 표로 만들기
    # data = pd.read_csv('data/diabetes.csv')
    # # print(data)
    #
    # # 특성, 타겟 나누기
    # X = data.drop('Outcome', axis=1)    # 입력데이터만
    # y = data['Outcome'].to_numpy()      # 정답만
    # # print(X)
    # # print(Y)
    #
    # # 나눈 표를 행렬로 변환
    # X = X.to_numpy()
    # # print(X)
    #
    # # 정규화하기
    # X = (X - np.min(X)) / (np.max(X) - np.min(X))
    # # print(X)
    #
    # # 평균구하기
    # # print(np.mean(X))
    #
    # # 공분산구하기
    # cov = (X-np.mean(X)).T @ (X-np.mean(X))
    # # print(cov)
    #
    # # 공분산의 고유값, 고유벡터
    # eigenvalues, eigenvectors = np.linalg.eig(cov)
    # # print("고유값:\n", eigenvalues)
    # # print("고유벡터:\n", eigenvectors)
    #
    # # 내림차순으로 정리하기(비중이 큰것 위주로, 차원을 축소하기 위함)
    # idx = eigenvalues.argsort()[::-1]
    # # print(idx)
    # eigenvalues = eigenvalues[idx]
    # eigenvectors = eigenvectors[:, idx]
    # # print(eigenvalues)
    # # print(eigenvectors)
    #
    #
    #
    # # 차원을 2차원으로 축소
    # transformer = eigenvectors[:, :2]
    # # print("선형변화벡터: \n", transformer)
    # transX = X @ transformer
    # # print(transX)
    #
    # # 시각화
    # # colors = ['r', 'g']
    # # target_names = ['diabetes', 'no']
    # #
    # # for i, target_name in enumerate(target_names):
    # #     plt.scatter(transX[y == i, 0],
    # #                 transX[y == i, 1],
    # #                 c=colors[i],
    # #                 label=target_name,
    # #                 alpha=0.7)
    # #
    # # plt.xlabel("PCA Component 1")
    # # plt.ylabel("PCA Component 2")
    # # plt.title("2D PCA of Diabetes Dataset")
    # # plt.legend()
    # # plt.grid(True)
    # # plt.show()

    #LDA
    df = pd.read_csv('data/diabetes.csv')
    diabetes_one = df[df['Outcome']==1]
    diabetes_zero = df[df['Outcome'] == 0]
    # print(diabetes_one)
    # print(diabetes_zero)

    X_one = diabetes_one.iloc[:, :-1]
    X_zero = diabetes_zero.iloc[:, :-1]
    y_one = diabetes_one.iloc[:, -1]
    y_zero = diabetes_zero.iloc[:, -1]

    #행렬식
    X_one = X_one.values
    X_zero = X_zero.values

    #정규화
    normalization = MinMaxScaler()
    X_one_norm = normalization.fit_transform(X_one)
    X_zero_norm = normalization.fit_transform(X_zero)
    # print(X_one_norm)
    # print(X_zero_norm)

    X = normalization.fit_transform(df.iloc[:, :-1].values)
    # print(X_normal)

    y = df.iloc[:, -1].values

    X_one_cov = np.cov(X_one_norm.T)
    X_zero_cov = np.cov(X_zero_norm.T)
    # print(setosa_cov.shape, versicolor_cov.shape, virginica_cov.shape)

    SW = X_one_cov + X_zero_cov
    # print(SW)

    X_one_mean = np.mean(X_one_norm, axis=0)
    X_zero_mean = np.mean(X_zero_norm, axis=0)
    # print(setosa_mean, versicolor_mean, virginica_mean)

    mean_matrix = np.vstack((X_one_mean, X_zero_mean))
    # print(mean_matrix.shape)

    SB = np.cov(mean_matrix.T)
    # print(SB)

    inv_SW = np.linalg.inv(SW)
    W = SB @ inv_SW
    print(W)

    # 원본을 곱하면 됨?
    transX = X @ W
    # print(transX.shape)

    # 공분산구하기
    cov = (X - np.mean(X)).T @ (X - np.mean(X))
    # print(cov)

    # 공분산의 고유값, 고유벡터
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    # print("고유값:\n", eigenvalues)
    # print("고유벡터:\n", eigenvectors)

    # 내림차순으로 정리하기(비중이 큰것 위주로, 차원을 축소하기 위함)
    idx = eigenvalues.argsort()[::-1]
    # print(idx)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    # print(eigenvalues)
    # print(eigenvectors)

    # 차원을 2차원으로 축소
    transformer = eigenvectors[:, :2]
    # print("선형변화벡터: \n", transformer)
    transX = X @ transformer
    # print(transX)

    # pca = PCA(n_components=2)
    # X_pca = pca.fit_transform(transX)
    # print(X_pca.shape)

    # # lda = LinearDiscriminantAnalysis(n_components=2)
    # lda = LinearDiscriminantAnalysis(n_components=1)
    # x_lda = lda.fit_transform(X, y)
    # # print(x_lda)

    # 시각화
    colors = ['r', 'g']
    target_names = ['diabetes', 'no']

    for i, target_name in enumerate(target_names):
        plt.scatter(transX[y == i, 0],
                    transX[y == i, 1],
                    c=colors[i],
                    label=target_name,
                    alpha=0.7)

    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.title("2D PCA of Diabetes Dataset")
    plt.legend()
    plt.grid(True)
    plt.show()