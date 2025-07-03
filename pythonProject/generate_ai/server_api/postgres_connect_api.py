from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import torch
import psycopg2



app = Flask(__name__) # name은 현재 파일 이름

CORS(app) # CORS 해제

conn_params = {
  "host": "localhost",
  "database": "mydb",
  "user": "kogo",
  "password": "111"
}


def load_model(sentence):
    try:
        query = f'''SELECT document, similarity(lower('{sentence}'),
                       lower(document)) AS similarity_score
                       FROM cosine_similarity_table
                       ORDER BY similarity_score DESC
                       LIMIT 10;'''
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result
    except Exception as error:
        # print(error)
        return jsonify({"error":f"예측 중 에러 발생: {error}"})

@app.route("/predict", methods=['POST']) #methods=['GET', 'POST'] 여러개 쓰기 가능
def predict_sentiment():
    try:
        data = request.get_json() # request라이브러리를 사용
        text = data["text"] #frontend에서 text에 object형식으로 데이터를 심어서 json파일로 보낸걸 받음?, 이 문장을 model에 전달해주면 됨 ?
        print(text)
        result = load_model(text)
        # return jsonify({"label": "hello"})
        print(result)
        return jsonify({"label": result[0]})
    except Exception as error:
        return jsonify({"error": f"예측 중 에러 발생: {error}"})

@app.route("/predict", methods=["GET"]) #아마 default가 get일 것임
def hello():
    return jsonify({"greet": "hello"})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) #flask Port : 5000
