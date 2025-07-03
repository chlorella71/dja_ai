from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
import torch

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ["http://localhost:3000"] 등 프론트 주소 #"localhost:5173"
    allow_credentials=True,
    allow_methods=["*"],  # 모든 메서드 허용: GET, POST, OPTIONS 등
    allow_headers=["*"],  # 모든 헤더 허용
)

model_path = "../save_model"

class SentimentRequest(BaseModel):
    text: str

def make_classifier():
    try:
        device = 0 if torch.cuda.is_available() else -1 # python의 삼항연산자, gpu사용여부
        sentiment_classifier = pipeline(
            'sentiment-analysis',
            model=model_path,
            tokenizer=model_path,
            device = device,
        )
    except Exception as error:
        print(f"모델 로드 중 에러 발생: {error}")
        sentiment_classifier = None
    return sentiment_classifier



# sentiment_classifier = None # 모델 심는 곳
@app.post("/post/predict") # 장고는 localhost:8000
def predict_sentiment(request: SentimentRequest):
    print(request.text)
    sentiment_classifier = make_classifier()
    if sentiment_classifier is None:
        return {"error": "서버 내부 오류: 모델이 로드되지 않았습니다."}
    try:
        result = sentiment_classifier(request.text)
        # return result[0]
        return {"greeting": result}
    except Exception as error:
        return {"error": f"예측 중 에러 발생: {error}"}


@app.get("/get/predict")
def hello():
    return {"status":"Sentiment analysis server!!!!"}



if __name__ == "__main__":
    pass