from pymongo import MongoClient
import pandas as pd

# 접속 정보
username="kogo"
password = "111"
host ="43.203.208.21" #aws ec2 ip
port = 27017
db_name="mongodb_test"
auth_db = "admin"
# collection_name="products"
collection_name= "sales"

# 더미데이터
dummy_products = [
    {"name": "Laptop", "price": 1200000, "publisher": "삼성전자"},
    {"name": "Monitor", "price": 300000, "publisher": "LG전자"},
    {"name": "Keyboard", "price": 50000, "publisher": "로지텍"},
    {"name": "Mouse", "price": 25000, "publisher": "로지텍"},
    {"name": "Tablet", "price": 800000, "publisher": "애플"},
    {"name": "Smartphone", "price": 1000000, "publisher": "삼성전자"},
    {"name": "Speaker", "price": 70000, "publisher": "브리츠"},
    {"name": "Webcam", "price": 45000, "publisher": "로지텍"},
    {"name": "Printer", "price": 150000, "publisher": "캐논"},
    {"name": "External HDD", "price": 110000, "publisher": "WD"}
]

def conn_mongod():

    # uri
    uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?authSource={auth_db}"

    # MongoDB 연결
    mongo_client = MongoClient(uri)
    db = mongo_client[db_name]
    collection = db[collection_name] # pymongo 방식
    # return db
    return collection

if __name__ == "__main__":
    # db = conn_mongod()
    collection = conn_mongod()

    # products collection data 편집, mongodb방식
    # db.products.insert_one(
    #     {"name": "computer",
    #      "price": 500000,
    #      "publisher": "한림출판사"
    #      }
    # )

    # producs collection data 편집, pymongo방식
    #insert
    # collection.insert_one(
    #     {"name" : "keyboard",
    #      "price": 6000,
    #      "publisher": "희준"
    #      }
    # )
    # collection.insert_many(dummy_products)

    #delete
    # collection.delete_one(
    #     {"name": "keyboard"}
    # )

    #pandas로 데이터 조회하기
    data = collection.find(
        {
            "name": "computer"}
    )
    df = pd.DataFrame(data)
    # print(df)

    # excel의 Sales.xlsx를 pandas로 변환한뒤 mongodb에 넣기
    df = pd.read_excel("data/Sales.xlsx", sheet_name="판매")
    json = df.to_dict(orient="records")
    # collection.insert_many(json)
    data = collection.find({}, {})
    df = pd.DataFrame(data)
    print(df)

