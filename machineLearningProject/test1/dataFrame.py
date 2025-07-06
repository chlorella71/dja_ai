import pickle
import pandas as pd
import numpy as np

if __name__=="__main__":
    ## csv로 dat파일 읽어오기
    # df=pd.read_csv("data/ratings.dat", sep="::", engine="python")
    # print(df)

    ## df에 columns 만들어주기
    # df.columns=["userId", "movieId", "rating", "timestamp"]
    # print(df)

    ## dat파일 pkl형식으로 만들기
    # df.columns=["userId", "movieId", "rating", "timestamp"]
    # with open("data/ratings.pkl", "wb") as f: # wb는 write binary, 데이터를 binary형태(이진형식)로 쓰겠다는 뜻
    #     pickle.dump(df, f)

    ## pkl파일 읽어오기
    # with open("data/ratings.pkl", "rb") as f:
    #     df = pickle.load(f)
    # print(df)
    # print(df.head()) # 맨앞 5행 출력

    ## df형식을 pivot_table로 만들어 pivot_df에 담기
    # pivot_df = df.pivot_table(index="userId",
    #                           columns="movieId",
    #                           values="rating",
    #                           fill_value=0)
    # print(pivot_df)
    # print(pivot_df.head())

    # pivot_df를 pkl로 저장하기
    # with open("data/ratings.pkl", "rb") as f:
    #     df = pickle.load(f)
    # pivot_df = df.pivot_table(index="userId", columns="movieId", values="rating", fill_value=0)
    # with open("data/pivot_rating.pkl", 'wb') as f:
    #     pickle.dump(pivot_df, f)

    # pkl형식으로 저장한 pivot_df 읽어오기
    with open("data/pivot_rating.pkl", "rb") as f:
        pivot_df = pickle.load(f)
    # print(pivot_df)
    # print(pivot_df.head())

    ## 설계잘못함... 처음에 None만들었어야하는데 0으로 만듬...
    ## 그래서 0을 None으로 바꿔주기
    pivot_df.replace(0, np.nan, inplace=True) # replace는 원본을 바꾸지 않음, None은 pandas가 object로 인식하고 NaN으로 인식하지 못해서 np.nan을 이용해야함
    # print(pivot_df)

    # 각 movie의 rating의 평균을 계싼해서 None값을 각 평균값으로 채우기
    means = pivot_df.mean(axis=0)
    pivot_df.fillna(means, inplace=True)
    print(pivot_df)