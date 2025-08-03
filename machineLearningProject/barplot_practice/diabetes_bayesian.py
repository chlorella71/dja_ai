import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import BayesianRidge, Lasso, LinearRegression, Ridge, ElasticNet, ARDRegression, SGDRegressor
from sklearn.metrics import accuracy_score

def accuracy_test(input_model):
    ## 데이터 가져오기(csv -> DataFrame 변환)
    df = pd.read_csv('data/diabetes.csv')
    # print(df)
    # Outcome : Label, 0은 No_diabetes, 1은 diabetes

    ## 정답값(label) 분리
    # print(df.keys())
    x_feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                       'BMI', 'DiabetesPedigreeFunction', 'Age']
    y_feature_name = ['Outcome']

    X = df[x_feature_names]
    y = df[y_feature_name]

    ## Column들의 단위 맞추기(정규화, normalization) - 이번엔 MinMaxScaler 사용
    scaler = MinMaxScaler()  # MinMax는 범위가 0부터 1까지
    X_scaled = scaler.fit_transform(X)
    # print(X_scaled)

    ## 과적합 막기(train, test 분리)
    # Xtrain, Xtest, ytrain, ytest = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    Xtrain, Xtest, ytrain, ytest = train_test_split(X_scaled, y, test_size=0.2, random_state=77)
    # print(Xtrain.shape)
    # print(Xtest.shape)
    # print(len(Xtrain))
    # print(len(Xtest))
    # print(ytrain.shape)
    # print(ytest.shape)
    # print(len(ytrain))
    # print(len(ytest))

    ## 모델만들기
    model = input_model
    # y는 (n, 1)형태의 DataFrame인데 fit()은 y를 1차원 배열로 기대하기 때문에 에러발생
    # model.fit(Xtrain, ytrain.values.ravel()) # 학습시 1차원으로 변환
    model.fit(Xtrain, ytrain.iloc[:, 0])  # 또는 DataFrame => Series로 변환
    predicts = model.predict(Xtest)
    predicts_class = np.round(predicts).astype(int).reshape(-1)
    ytest = ytest.values.reshape(-1)
    accuracy = accuracy_score(ytest, predicts_class)
    print(f'{input_model} accuracy: {accuracy}')


if __name__ == "__main__":
    ## 모델별 정확도 테스트해보기
    accuracy_test(BayesianRidge()) # BayesianRidge
    accuracy_test(Lasso()) # Lasso
    accuracy_test(LinearRegression()) # LinearRegression
    accuracy_test(Ridge()) # Ridge
    accuracy_test(ElasticNet()) # ElasticNet
    accuracy_test(ARDRegression()) # ARDRegression
    accuracy_test(SGDRegressor()) # SGDRegressor

