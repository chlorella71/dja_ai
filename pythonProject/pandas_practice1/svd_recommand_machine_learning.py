import pandas as pd
import numpy as np
import pickle

if __name__ == "__main__":
    # ratings = pd.read_csv("data/ratings.dat", sep='::', engine='python') # csv파일과 dat파일의 구분자가 다르기 때문, 구분자를 다르게 처리하기떄문에 엔진을 다른 걸 쓰려고 할 수 있기 때문에 engine도 명시해줘야 함
    # print(ratings)
    # with open("data/ratings.pkl", 'wb') as file: #file은 변수, wb: write binary, .pkl : 확장자
    #     pickle.dump(ratings, file) # dump는 linux 명령어
    with open("data/ratings.pkl", "rb") as file:
        ratings = pickle.load(file)
    # print(ratings)

    ratings.columns=["user_id", "movie_id", "rating", "time"]
    # print(ratings)
    rating_pivot = ratings.pivot_table(index="user_id",
                                       columns="movie_id",
                                       values="rating",
                                       fill_value=0)
    print(rating_pivot)