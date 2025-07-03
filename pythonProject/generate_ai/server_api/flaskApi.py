from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import torch



app = Flask(__name__) # name은 현재 파일 이름

CORS(app) # CORS 해제

def load_model():
    sentiment_classifier= None
    try:
        device = 0 if torch.cuda.is_available() else - 1 # 삼항연산자
        sentiment_classifier = pipeline(
            'sentiment-analysis',
            model = "../save_model",
            tokenizer = "../save_model",
            device = device,
        ) # tuple식으로 함수 전달하기
        return sentiment_classifier
    except Exception as error:
        # print(error)
        return jsonify({"error":f"예측 중 에러 발생: {error}"})

@app.route("/predict", methods=['POST']) #methods=['GET', 'POST'] 여러개 쓰기 가능
def predict_sentiment():
    sentiment_classifier = load_model()
    if sentiment_classifier is None:
        return jsonify({"error":"서버내부오류: 모델이 로드되지않았음"})
    try:
        data = request.get_json() # request라이브러리를 사용
        text = data["text"] #frontend에서 text에 object형식으로 데이터를 심어서 json파일로 보낸걸 받음?, 이 문장을 model에 전달해주면 됨 ?
        print(text)
        result = sentiment_classifier(text)
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
