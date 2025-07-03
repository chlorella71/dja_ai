from datasets import load_dataset
import pandas as pd
import pickle
from db_conn.postgres_db import conn_postgres_db





if __name__ == "__main__":
    # pass
    with open("../data/datasets.pkl", "rb") as f:
        data = pickle.load(f)
    df = pd.DataFrame(data['train'])
    print(df[["document", "label"]])
    df = df[["document", "label"]]
    # conn_postgres_db(df, "kogo", 111, "mydb","cosine_similarity_table")