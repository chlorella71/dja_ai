import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from scipy.spatial.distance import mahalanobis






if __name__ == '__main__':

    # 데이터 로드 및 준비
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['label'] = iris.target
    # df["label_name"] = None
    df["label_name"] = np.where(df['label']== 0, iris.target_names[0],
                                np.where(df['label']== 1, iris.target_names[1],
                                iris.target_names[2]))
    for num in [0, 1, 2]:
        df.loc[df['label'] == num, 'label_name'] = iris.target_names[num]

    # 데이터 분할
    # setosa
    setosa = df[df['label_name'] == "setosa"]
    setosa_data = setosa.iloc[:45]
    setosa_pred_data_five = setosa.iloc[45:]

    # versicolor
    versicolor = df[df['label_name'] == "versicolor"]
    versicolor_data = versicolor.iloc[:45]
    versicolor_pred_data_five = versicolor.iloc[45:]

    # virginica
    virginica = df[df['label_name'] == "virginica"]
    virginica_data = virginica.iloc[:45]
    virginica_pred_data_five = virginica.iloc[45:]

    # --- [수정] np.mean() 대신 Pandas의 .mean() 메소드 사용 ---
    # .mean()은 각 열의 평균을 Series로 반환하므로, .values로 NumPy 배열을 추출합니다.
    setosa_mean = setosa_data.iloc[:, :4].mean().values
    versicolor_mean = versicolor_data.iloc[:, :4].mean().values
    virginica_mean = virginica_data.iloc[:, :4].mean().values

    # --- [수정] np.cov() 대신 Pandas의 .cov() 메소드 사용 ---
    # .cov()는 공분산 행렬을 DataFrame으로 반환하므로, .values로 NumPy 배열을 추출합니다.
    setosa_cov = setosa_data.iloc[:, :4].cov().values
    setosa_inv_cov = np.linalg.inv(setosa_cov)

    versicolor_cov = versicolor_data.iloc[:, :4].cov().values
    versicolor_inv_cov = np.linalg.inv(versicolor_cov)

    virginica_cov = virginica_data.iloc[:, :4].cov().values
    virginica_inv_cov = np.linalg.inv(virginica_cov)

    # 테스트할 하나의 데이터 포인트 (원래 setosa 품종)
    test_point = virginica_pred_data_five.iloc[3, :4].values
    # print(f"테스트 데이터 포인트: {test_point}\n")

    # 각 품종의 분포로부터의 마할라노비스 거리 계산
    m_setosa_dist_setosa = mahalanobis(test_point, setosa_mean, setosa_inv_cov)
    m_setosa_dist_versicolor = mahalanobis(test_point, versicolor_mean, versicolor_inv_cov)
    m_setosa_dist_virginica = mahalanobis(test_point, virginica_mean, virginica_inv_cov)

    df.rename(columns={"label":"target"})
    print(df.keys())
    print(df.shape)
    print("--- Setosa 데이터와 각 품종 분포와의 거리 ---")
    print(f"vs Setosa     : {m_setosa_dist_setosa:.4f}")
    print(f"vs Versicolor : {m_setosa_dist_versicolor:.4f}")
    print(f"vs Virginica  : {m_setosa_dist_virginica:.4f}")


# ---------------------------------------------------------------

# import pandas as pd
# import numpy as np
# from sklearn.datasets import load_iris
# from scipy.spatial.distance import mahalanobis
#
#
# if __name__ == '__main__':
#     iris = load_iris()
#     df = pd.DataFrame(iris.data, columns=iris.feature_names)
#     df['label'] = iris.target
#     df['label_name'] = None
#     for num in [0,1,2]:
#         df.loc[df['label'] == num, 'label_name'] = iris.target_names[num]
#     # df.loc[df['label'] == 0, 'label_name'] = iris.target_names[0]
#     # df.loc[df['label'] == 1, 'label_name'] = iris.target_names[1]
#     # df.loc[df['label'] == 2, 'label_name'] = iris.target_names[2]
#     #setosa
#     setosa = df[df['label_name'] == 'setosa'] #label_name 붙이기
#     setosa_data = setosa.loc[:44]
#     setosa_pred_data_five = setosa.loc[45:]
#     #versicolor
#     versicolor = df[df['label_name'] == 'versicolor']
#     versicolor_data = versicolor.loc[:44]
#     versicolor_pred_data = versicolor.loc[45:]
#     #virginica
#     virginica = df[df['label_name'] == 'virginica']
#     virginica_data = virginica.loc[:44]
#     virginica_pred_data_five = virginica.loc[45:]
#     #mean, 평균
#     setosa_mean = np.mean(setosa_data.iloc[:, :4])
#     versicolor_mean = np.mean(versicolor_data.iloc[:, :4])
#     virginica_mean = np.mean(virginica_data.iloc[:, :4])
#     #cov, 공분산
#     setosa_cov = np.cov(setosa_data.iloc[:, :4])
#     versicolor_cov = np.cov(versicolor_data.iloc[:, :4])
#     virginica_cov = np.cov(virginica_data.iloc[:, :4])
#     #linalg.inv, 역?, 나누기는 역수를 곱함
#     setosa_inv_cov = np.linalg.inv(setosa_cov)
#     versicolor_inv_cov = np.linalg.inv(versicolor_cov)
#     virginica_inv_cov = np.linalg.inv(virginica_cov)
#     #mahalanobis
#     # 이건 코드 오류남
#     # x = setosa_pred_data_five.iloc[0, :4].values # 특성 4개만 선택하고 1차원으로 평탄화해서 넘겨줘야함?
#     # m_setosa_dist_setosa= mahalanobis(x, setosa_mean, setosa_inv_cov)
#     # m_setosa_dist_versicolor= mahalanobis(x, versicolor_mean, versicolor_inv_cov)
#     # m_setosa_dist_virginica= mahalanobis(x, virginica_mean, virginica_inv_cov)
#     # df[df['label'] == 0] = iris.target[0]
#     # labels = iris.target
#     # df = pd.read_csv("data/iris.csv")
#
#     # print(m_setosa_dist_setosa)
#     # print(m_setosa_dist_versicolor)
#     # print(m_setosa_dist_virginica)
#     # print(setosa_pred_data_five.iloc[0, :].values)
#     # print(setosa_inv_cov)
#     # print(setosa_mean)
#     # print(len(setosa_data))
#     # print(setosa_pred_data_five)
#     # print(setosa)
#     # print(iris.target_names)
#     # print(iris.feature_names)
#     # print(iris.data)
#     # print(y)
#     # print(df)

# ---------------------------------------------------------------

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import pandas as pd
#
#
# df = pd.read_csv("data/test.csv")
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print(df[(df['weight'] >= 4000) & (df['acceleration'] >= 14) & (df['horsepower'] >= 150)])
#     print(df[(df['weight']>=4000) & (df['acceleration']>=14)])
#     print(df[df['weight']>=4000])
#     print(df[['weight', 'grade']])
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
