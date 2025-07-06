import pickle

import pandas as pd


if __name__=="__main__":
    ## ratings.pkl 가져오기
    with open("data/ratings.pkl", "rb") as f:
        rating_df = pickle.load(f)
    # print(rating_df)

    ## 조건(4.0이상)주고 loc으로 뽑기
    rating_df = rating_df.loc[rating_df["rating"]>=4.0, "userId": "rating"] # 조건주고 필요한칼럼(지정or 범위)만 loc으로 가져오기
    # print(rating_df)
    # print(rating_df.shape) # 개수 출력

    ## 10000index까지 loc으로 출력
    # rating_df = rating_df.loc[:10000]
    # print(rating_df)
    # print(rating_df.shape) # 10000개가 출력되지 않는 이유 : drop하면서 데이터가 사라졌지만 index는 남아있으므로 10000째 index에서 멈춘것

    ## 10000개 가져오기(iloc)
    # rating_df = rating_df.iloc[:10000] #iloc으로 자동지정된 index로 10000개 출력됨
    # print(rating_df.shape)

    # pivot으로 다시 만들어서 가져오기
    pivot_df = rating_df.pivot_table(index="userId",
                                     columns="movieId",
                                     values="rating",
                                     fill_value=None)
    # print(pivot_df)

    ## pivot테이블의 평균 구하기
    means=pivot_df.mean()
    print(means)

    # axis 지정해서(movie들의 평균) 평균값 넣기
    # means=pivot_df.mean(axis=0)
    # pivot_df.fillna(means, inplace=True)
    # print(pivot_df)