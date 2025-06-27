import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
iris = load_iris()

if __name__ == "__main__":
    X = iris.data
    y = iris.target

    normal = MinMaxScaler()
    X_normal = normal.fit_transform(X)

    U, S, VT = np.linalg.svd(X_normal, full_matrices=False)
    # print(U.shape)
    # print(S.shape)
    # print(VT.shape)

    # print(S)
    DS = np.diag(S) # S는 벡터, S를 대각행렬로 만듬
    # print(DS)

    US = U @ DS
    USVT = US @ VT
    # print(USVT)
    # print(X_normal)
    # print(USVT[0,0])
    # print(X_normal[0,0])
    # print(USVT[77, 3])
    # print(X_normal[77, 3])
    print(USVT[149, 3])
    print(X_normal[149, 3])