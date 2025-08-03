import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler # SVD는 정규분포를 기본으로 하기 떄문에 StandardScaler를 사용해야함(MinMaxScaler는 안됨)

if __name__=="__main__":
    iris = load_iris()
    X = iris.data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # print(X_scaled)

    # 특이값분해(SVD) U: 우측 제곱, VT: 좌측 제곱, S: 고윳값
    U, S, VT = np.linalg.svd(X_scaled, full_matrices=False)
    # print(S)

    D = np.diag(S) # S를 대각행렬로 변환
    # print(D)

    XX = U @ D @ VT
    # print(XX[0])
    # print(X_scaled[0])
    print(XX.shape)

    ## 차원축소
    # 사진 흑백전환 기법에 사용됨
    # print(U.shape)
    # print(D.shape)
    # print(VT.shape)
    # U[:, :2]의 의미: 앞에는 다 가져오고 뒤에는 2개만 가져옴
    XX = U[:, :2] @ D[:2, :2] @ VT[:2, :2] # U:(150,2), D:(2,2), VT(2,2)
    print(XX.shape)

    plt.figure(figsize=(8, 6))
    # plt.scatter(XX[:, 0], XX[:, 1], c='yellow', cmap='viridis', edgecolor='k', s=50)
    plt.scatter(XX[:, 0], XX[:, 1], c='yellow', edgecolor='k', s=50)
    plt.show()
