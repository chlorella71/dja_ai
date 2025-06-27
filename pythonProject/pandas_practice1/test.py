import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/test.csv")
    # print(df)
    df['등급'] = df['acceleration'].apply(lambda x: x* 10)
    print(df)