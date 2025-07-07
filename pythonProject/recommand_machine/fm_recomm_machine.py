import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from recommand_module import extract_high_rating_data
import os
from tqdm import tqdm


# --- 1. PyTorch Dataset 클래스 정의 ---
# 데이터를 모델에 효율적으로 공급하기 위한 커스텀 데이터셋
class RatingDataset(Dataset):
    def __init__(self, users, items, ratings):
        self.users = users
        self.items = items
        self.ratings = ratings

    def __len__(self):
        return len(self.users)

    def __getitem__(self, idx):
        return self.users[idx], self.items[idx], self.ratings[idx]


# --- 2. PyTorch Matrix Factorization 모델 정의 ---
# nn.Module을 상속받아 모델을 정의합니다.
class MatrixFactorization(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim):
        super(MatrixFactorization, self).__init__()
        # 사용자 임베딩 레이어
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        # 아이템 임베딩 레이어
        self.item_embedding = nn.Embedding(num_items, embedding_dim)

        # 가중치 초기화
        self.user_embedding.weight.data.uniform_(0, 0.05)
        self.item_embedding.weight.data.uniform_(0, 0.05)

    def forward(self, user_indices, item_indices):
        # 주어진 인덱스에 해당하는 임베딩 벡터를 가져옵니다.
        user_vector = self.user_embedding(user_indices)
        item_vector = self.item_embedding(item_indices)

        # 사용자 벡터와 아이템 벡터를 내적(dot product)하여 예측 평점을 계산합니다.
        # (batch_size, embedding_dim) * (batch_size, embedding_dim) -> (batch_size, 1)
        rating = (user_vector * item_vector).sum(1)
        return rating


# --- 3. LightFM을 대체하는 메인 함수 ---
def pytorch_mf_model(users_df, factors=32, minimum_num_ratings=4, epochs=20, lr=0.01):
    """
    PyTorch와 Matrix Factorization을 사용한 추천 시스템

    Args:
      users_df (pd.DataFrame): 사용자-영화-평점 데이터프레임
      factors (int): 잠재 요인(Embedding Dimension)의 수
      minimum_num_ratings (int): 필터링을 위한 최소 평점 개수
      epochs (int): 학습 반복 횟수
      lr (float): 학습률 (Learning Rate)

    Returns:
      pd.DataFrame: 각 사용자-영화 쌍에 대한 예측 점수 데이터프레임
    """

    # [수정 1] M1/M2 Mac의 GPU(MPS) 사용 설정
    # -----------------------------------------------------------------
    # if torch.backends.mps.is_available():
    #     device = torch.device("mps")
    #     print("MPS(Apple Silicon GPU)를 사용합니다.")
    if torch.backends.mps.is_available():
        device = torch.device("cuda")
        print("CUDA(NVIDIA GPU)를 사용합니다.")
    else:
        device = torch.device("cpu")
        print("MPS를 사용할 수 없어 CPU를 사용합니다.")

    # ================================
    # 1단계: 데이터 필터링 (원본 코드와 유사)
    # ================================
    user_counts = users_df["user_id"].value_counts()
    valid_users = user_counts[user_counts >= minimum_num_ratings].index
    movie_counts = users_df["movie_id"].value_counts()
    valid_movies = movie_counts[movie_counts >= minimum_num_ratings].index
    filtered_data = users_df[
        (users_df["user_id"].isin(valid_users)) & (users_df["movie_id"].isin(valid_movies))
        ].copy()

    # ================================
    # 2단계: 데이터 전처리 (PyTorch에 맞게 수정)
    # ================================
    # 사용자/아이템 ID를 0부터 시작하는 정수 인덱스로 변환
    user_ids = filtered_data['user_id'].unique()
    movie_ids = filtered_data['movie_id'].unique()
    user_to_idx = {user_id: i for i, user_id in enumerate(user_ids)}
    movie_to_idx = {movie_id: i for i, movie_id in enumerate(movie_ids)}

    # DataFrame에 인덱스 컬럼 추가
    filtered_data['user_idx'] = filtered_data['user_id'].map(user_to_idx)
    filtered_data['movie_idx'] = filtered_data['movie_id'].map(movie_to_idx)

    # PyTorch Dataset 및 DataLoader 생성
    dataset = RatingDataset(
        users=torch.LongTensor(filtered_data['user_idx'].values),
        items=torch.LongTensor(filtered_data['movie_idx'].values),
        ratings=torch.FloatTensor(filtered_data['rating'].values)
    )
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    # ================================
    # 3단계: PyTorch 모델 학습
    # ================================
    num_users = len(user_to_idx)
    num_items = len(movie_to_idx)
    model = MatrixFactorization(num_users, num_items, embedding_dim=factors).to(device)

    loss_fn = nn.MSELoss()  # 손실 함수: 평균 제곱 오차
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)  # 옵티마이저: Adam

    print("\nPyTorch 모델 학습 시작...")
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for users_idx, items_idx, ratings in dataloader:
            # 데이터를 지정된 장치(mps 또는 cpu)로 보냄
            users_idx, items_idx, ratings = users_idx.to(device), items_idx.to(device), ratings.to(device)

            optimizer.zero_grad()
            predictions = model(users_idx, items_idx)
            loss = loss_fn(predictions, ratings)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss / len(dataloader):.4f}")

    # ================================
    # 4단계: 전체 예측 평점 행렬 생성
    # ================================
    model.eval()
    with torch.no_grad():
        # 학습된 사용자/아이템 임베딩 행렬을 가져옴
        user_factors = model.user_embedding.weight.cpu().numpy()
        item_factors = model.item_embedding.weight.cpu().numpy()

        # 모든 사용자와 아이템 간의 내적을 통해 예측 평점 행렬 생성
        predicted_ratings_matrix = user_factors @ item_factors.T

    # DataFrame으로 변환
    predicted_ratings_df = pd.DataFrame(predicted_ratings_matrix, index=user_ids, columns=movie_ids)

    # 롱 포맷으로 변환
    unpivot_predicted_rating_df = predicted_ratings_df.stack().reset_index()
    unpivot_predicted_rating_df.columns = ["user_id", "movie_id", "predicted_rating"]

    return unpivot_predicted_rating_df


# --- 함수 사용 예시 ---
if __name__ == '__main__':
    users = extract_high_rating_data()
    # print(users)
    # exit()
    # # 샘플 데이터 생성
    # sample_users = pd.DataFrame({
    #     'user_id': ['u1', 'u1', 'u2', 'u2', 'u3', 'u3', 'u4', 'u4'],
    #     'movie_id': ['m1', 'm2', 'm2', 'm3', 'm1', 'm3', 'm2', 'm3'],
    #     'rating': [5, 4, 3, 5, 4, 5, 2, 4]
    # })

    # PyTorch MF 모델로 추천 받기
    predictions = pytorch_mf_model(users, factors=8, minimum_num_ratings=1, epochs=10)
    print("\n--- 최종 예측 결과 ---")
    print(predictions.head())