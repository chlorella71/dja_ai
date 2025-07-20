import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt # as: alias 별칭으로 라이브러리 호출을 축약하겠음, plt : pythonmatplotlib의 약자

if __name__ == "__main__":
    # csv파일 읽기
    df = pd.read_csv("data/diabetes.csv")
    print(df.keys())

    # Outcome(결과값) 제외하기, 지금은 data의 상관관계를 시각하하려는 것이기때문에 결과값이 필요하지 않음
    df = df.iloc[:, :-1] # 앞에는 data, 뒤에는 차원이 됨, 차원에서 Outcome을 빼겠다는 말, loc은 마지막이 포함안됨, iloc은 마지막이 포함됨
    # print(df.keys())

    # 피벗테이블(차원의 상관관계 구하기)
    correlation_matrix = df.corr() # corr() 라이브러리의 함수를 사용하면 바로 구할수 있음
    # print(correlation_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt='.2f',
        linewidths=0.5
    )
    plt.title("Correlation Matrix Heatmap")
    plt.show()


