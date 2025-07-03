from sqlalchemy import create_engine

print("1.Hello World!!!")

def conn_postgres_db(df, id, pw, db, table_name):
    url_conn = f"postgresql+psycopg2://{id}:{pw}@localhost:5432/{db}" # 포스트그리 연동 아이디:비번@주소/db이름
    conn= create_engine(url_conn)
    df.to_sql(name=f'{table_name}', con=conn, if_exists="replace", index=False)


if __name__ == "__main__":
    print("2.Hello World!!!")
    conn_postgres_db(df, "postgres", 111, "mydb")