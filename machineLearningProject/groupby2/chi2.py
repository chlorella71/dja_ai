import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency


if __name__=="__main__":
    # pass
    df = pd.read_csv("data/marketing_campaign.csv", sep='\t')
    # print(df)
    # print(df.keys())
    # print(df['Marital_Status'].unique())
    # print(df['Response'].unique())

    col1 = "Marital_Status" # 결혼상태
    col2 = 'Response'   # 응답 여부(0: No, 1: Yes)

    df_clean = df.dropna(subset=[col1, col2]) # 결측치(NaN) 제거
    table = pd.crosstab(df_clean[col1], df_clean[col2]) #col1, col2로 구성된 교차빈포도(cross-tabulation talbe)만들기
    # print(table)

    # 카이제곱값, p-value 구하기
    chi2, p_value, _, _ = chi2_contingency(table)
    # print(chi2)
    # print(p_value)
    # print(f'p-값: {p_value:.9f}') # 소수점 이하 9자리까지 계산
    # p-value가 0.05보다 작으면 상관성이 높음, 0.05보다 크면 상관성이 없음.

    # 시각화
    from matplotlib_encoder import hangul_encoding
    hangul_encoding() # 한글 인코딩
    plt.figure(figsize=(10,6))
    # sns.countplot(data=데이터프레임, x=범주형컬럼명)
    # seaborn 라이브러리의 countplot 함수: 범주형데이터의 변수(카테고리)의 빈도수(개수)를 막대그래프로 그려줌
    sns.countplot(data=df_clean, x=col1, hue=col2)
    plt.title(f'{col1}(결혼상태)에 따른 {col2}(응답률)')
    plt.xlabel(col1)
    plt.ylabel('고객 수')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title=col2, labels=['No(거절)', 'Yes(수락)'])
    plt.tight_layout()
    plt.savefig('data/chi2_marital_status_response.png')
    plt.show()