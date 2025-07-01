import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import StandardScaler



if __name__=="__main__":
    model = SentenceTransformer("jhgan/ko-sroberta-multitask")
    sentences = [
        "오늘 날씨 정말 좋네요!",
        "이 영화는 너무 슬펐어요.",
        "맛있는 점심을 먹으러 갑시다.",
        "프로젝트 마감이 얼마 남지 않아 걱정입니다."
    ]
    raw_embeddings = model.encode(sentences) # 어떤 모델에서 벡터를 만듬
    # print(raw_embeddings)
    # print(raw_embeddings.shape) # (벡터, 차원(유니크한값)), 이 유니크값들은 정규분포에서 벗어나지 않은 랜덤값임
    # print(np.mean(raw_embeddings)) # 평균
    # print(np.std(raw_embeddings)) # 표준편차?(분산)
    # 보통은 통계에서는 평균 0, 분산을 1로 주긴함

    scaler = StandardScaler()
    std_embeddings = scaler.fit_transform(raw_embeddings) # 정규화 => 이걸 학습시킴
    print(np.mean(std_embeddings))
    print(np.std(std_embeddings))