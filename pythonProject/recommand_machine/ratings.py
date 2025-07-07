import pickle
import pandas as pd

if __name__=="__main__":
    df = pd.read_csv("data/ratings.dat", sep="::", engine="python", names=["userId", "movieId", "rating", "timestamp"])
    with open("data/ratings.pkl", "wb") as f:
        pickle.dump(df, f)


