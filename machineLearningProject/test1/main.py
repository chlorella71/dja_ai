# import 하는곳
from xml.sax.handler import feature_namespaces

import pandas as pd
from sklearn.datasets import load_iris

# 함수짜는곳

scores = [
    {"이름": "John", "국어":98, "영어":87, "수학":100},
    {"이름": "Sue", "국어":89, "영어":78, "수학":99},
    {"이름": "Peter", "국어":78, "영어":67, "수학":88},
    {"이름": "Susan", "국어":33, "영어":44, "수학":55},
]

scores = [
    ["John", 98, 87, 100],
    ["Sue", 89, 78, 99],
    ["Peter", 78, 67, 188],
    ["Susan", 33, 44, 155],
]

def print_hi(name):
    print(f'Hi, {name}')

# 실행하는 곳
if __name__ == '__main__':
    print_hi('PyCharm')
    df = pd.DataFrame(scores, columns=["이름", "국어", "영어", "수학"])
    # print(df)

    iris = load_iris()
    # print(iris)
    # print(iris.keys())
    # print(iris.feature_names)

    df = pd.DataFrame(iris.data, columns =iris.feature_names)
    print(df)

    iris=load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    df.drop(1, axis=0, inplace=True)
    print(df.iloc[1])




