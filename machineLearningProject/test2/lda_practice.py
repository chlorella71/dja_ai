import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA









if __name__ == "__main__":
    # pass
    iris= load_iris()
    X = iris.data
    y = iris.target # 정답값, 라벨링 데이터?
    # lda = LDA(n_components=2) ## 2차원으로 차원축소, lda는 지도학습, pca를 하고 난뒤 진행됨, 분류가 된상태
    lda = PCA(n_components=2) ## PCA로 해보기

    X = lda.fit_transform(X, y) # 값을 정답과 매칭시킴
    # print(X)

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", edgecolors='k', s=100) # 첫번째 값을 가져와 x축에 두번째값을 y축에 넣음, 그래프를 그리겠단 말, color= yellow

    handles, _ = scatter.legend_elements()
    plt.legend(handles=handles, labels=iris.target_names.tolist(), title='Classes') # Target은 label, 정답값(숫자)를 의미, Class는 각 숫자가 의미하는 실제 클래스 이름['setosa', 'versicolor', 'virginica']을 의미

    plt.xlabel("First Linear Discriminant")
    plt.ylabel("Second Linear Discriminant")
    # plt.title("LDA on Iris Dataset")
    plt.title("PCA on Iris Dataset")
    plt.grid(True)
    plt.show()
