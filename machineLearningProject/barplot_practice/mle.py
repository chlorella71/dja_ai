import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split # 원본데이터를 train(학습용), test(검증용)으로 나눠주는 라이브러리
from sklearn.covariance import EmpiricalCovariance
# 데이터의 '통계적 분포'를 분석하는 클래스
# - fit(X) : 각 feature의 평균과 공분산(covariance) 계산
# - cov.covariance_ : 공분산 행렬
# - cov.location_ : 평균 벡터
# - Mahalanobis distance 계산, 이상치 탐지 등에 사용
from sklearn.linear_model import LinearRegression
# 선형회귀 모델(Linear Regression) 객체
# - fit(X_train, y_train) : 최소제곱법(Least Squares)으로 가중치(Weight, β) 학습
# - predict(X_test) : 학습된 가중치로 y 예측 (y_hat)
# - coef_ : 각 feature별 회귀계수(기울기)
# - intercept_ : 절편(bias)
from sklearn.linear_model import BayesianRidge
# 베이지안 릿지 회귀(Bayesian Ridge Regression) 모델 객체
# - fit(X_train, y_train) : 베이지안 방식으로 가중치(Weight, β) 학습
#   (가중치를 확률분포로 추정하고, 자동 L2 정규화 효과)
# - predict(X_test) : 학습된 가중치로 y 예측 (y_hat)
# - coef_ : 각 feature별 회귀계수(기울기)의 평균 추정치
# - intercept_ : 절편(bias)
# - sigma_ : 가중치의 공분산 행렬 (불확실성 추정 가능)
from sklearn.metrics import accuracy_score
# 정확도(Accuracy) 계산 함수
# - accuracy_score(y_true, y_pred)
#   -> 전체 샘플 중 예측이 맞은 비율을 계산
#   -> 공식: Accuracy = (맞춘 샘플 수) / (전체 샘플 수)
# - y_true : 실제 정답 라벨 (1차원 배열)
# - y_pred : 모델의 예측 라벨 (1차원 배열)
# 회귀 모델 출력(연속값)에는 바로 사용 불가
#  → 필요 시 np.round() 등으로 정수 라벨로 변환 후 사용


## 머신을 만들 때 할 일
# 1. 정규화: 단위 맞추기(표준정규분포: -1<= 마할라노비스거리 <=1, minMax법: 0<= (x-min)/(max-min)) <=1
# 2. 과적합 막기: train, test분리(훈련데이터와 테스트데이터 분리) train:test = 8:2, 9:1 정도
# 3. 머신: 기울기(W, weight, 가중치)값을 찾는 것(기울기는 차원만큼 나옴?), train데이터만 사용하여 구함(test데이터는 참여하지 않음)

if __name__=="__main__":
    iris =load_iris()
    # print(iris.keys())
    # print(iris.data.shape)
    X = iris.data
    y = iris.target
    # print(y) # 0: setosa, 1:virginica, 2: versicolor
    # print(len(y))

    # y = iris.target.reshape(-1, 1) # numpy에선 그냥 쓰는게 가능하지만 수학적으로는 (-1, 1)을 해주는게 맞음?

    ## 머신 구하는 공식
    # B = (X.T @ X)^-1 @ X.T @ y

    ## train, test 분리하기
    # Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42) # random_state는 data중 무작위로 뽑는 것을 의미함
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=77) # random_state는 data중 무작위로 뽑는 것을 의미함
    # print(Xtrain.shape)
    # print(Xtest.shape)

    ## 가중치 구하기(선형회귀(LR)의 최소제곱해(LSS)를 계산해서 가중치(W, 회귀계수 B)를 구하는 과정
    Weight = np.linalg.inv(Xtrain.T @ Xtrain) @ Xtrain.T @ ytrain #np.linalg.inv는 역행렬을 구하는 numpy라이브러리
    # print(Weight)

    # print('test data: ', Xtest[0])
    # print('실제 정답(taget, label?): ', ytest[0])
    # print('예측 정답: ', Weight @ Xtest[0])
    # print('예측 정답: ', Weight.T @ Xtest[0]) # y = iris.target.reshape(-1, 1)일 때

    N = 0
    print('test data: ', Xtest[N])
    print('실제 정답(taget, label?): ', ytest[N])
    print('예측 정답: ', Weight @ Xtest[N])
    # print(Weight.T @ Xtest[N]) # y = iris.target.reshape(-1, 1)일 때

    cov = EmpiricalCovariance().fit(X) # 데이터 X의 평균과 공분산을 계산해서 저장

    ## LinearRegression ( MLE(최대우도법, 최소제곱해) )
    machine = LinearRegression() # 선형회귀모델 객체 생성
    machine.fit(Xtrain, ytrain) # train 데이터로 Weight(가중치) 학습
    predicts = machine.predict(Xtest) # 학습된 Weight로 새로운 X의 y 예측
    # ^y = X @ W # ^y: y-hat(와이 햇)이라고 읽고 예측값(predicted value)를 의미
    # print(predicts)

    predict = machine.predict(Xtest[0].reshape(1, -1))[0] # Xtest[0] 하나만 구하기
    # print(predict)

    N = 0
    predict = machine.predict(Xtest[N].reshape(1, -1))[0]
    print('LinearRegression를 사용하여 구한 예측값: ', predict)

    ## 가중치 비교
    print('-----------------가중치 비교----------------')
    print('직접구한 가중치: ', Weight)
    print('LinearRegression에서 구한 가중치?: ', machine.coef_)

    ## BayesianRidge
    model = BayesianRidge()
    model.fit(Xtrain, ytrain)
    print('BayesianRidge로 구한 가중치?: ', model.coef_) # coef_는 상수라는 뜻?

    ## 예측값 비교
    print('---------------예측 값 비교----------------')
    N = 0
    # 정답
    print('실제 정답값: ', ytest[N])

    # numpy ( 직접 행렬식으로 구함 )
    print('예측 정답: ', Weight @ Xtest[N])

    # LinearRegression (MLE(최대우도법, 최소제곱해))
    predict = machine.predict(Xtest[N].reshape(1, -1))[0]
    print('LinearRegression: ', predict)

    # BayesianRidge
    predict = model.predict(Xtest[N].reshape(1, -1))[0]
    print('BayesianRidge예측값: ',predict)

    ## 정확도 비교
    print('---------------------예측값에 대한 정확도--------------------')

    predicts = machine.predict(Xtest)
    predicts_class = np.round(predicts).astype(int).reshape(-1)
    ytest = ytest.reshape(-1)
    accuracy = accuracy_score(ytest, predicts_class)
    print('LinearRegression정확도: ', accuracy)

    # BayesianRidge
    predicts = model.predict(Xtest)
    predicts_class = np.round(predicts).astype(int).reshape(-1)

    accuracy = accuracy_score(ytest, predicts_class)
    print('BayesianRidge정확도: ', accuracy)