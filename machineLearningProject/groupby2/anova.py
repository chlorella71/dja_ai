import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway # F-통계량(ANOVA)

if __name__=="__main__":
    # csv파일 읽어서 dataframe으로 변환
    df = pd.read_csv('data/marketing_campaign.csv', sep='\t')
    # columns_name 출력해보기
    # print(df.keys())
    # Education(교육수준)과 MntWines(와인소비량?)의 상관관계를 구하기 위해 따로 빼기
    col1 = 'Education'
    col2 = 'MntWines'
    # 결측치(NaN) 제거
    df_clean = df.dropna(subset=[col1, col2]).copy() # 복제본으로 만들기
    # print(df_clean[col1].unique())
    category = ['Basic', '2n Cycle', 'Graduation', 'Master', 'PhD'] # 정렬하기

    #df_clean[df_clean[col1] == item][col2]
    #category의 item과 같은 col1의 col2를 []리스트에 담은 리스트 만들기?
    groups = [ df_clean[df_clean[col1] == item][col2] for item in category]
    # print(groups)
    # print(groups[0]) # col1이 Basic인 col2들 출력
    # print(len(groups))

    # f-통계, p-value 구하기(scipy 라이브러리 사용)
    f_statistic, p_value = f_oneway(*groups) # *groups: 리스트의 요소를 풀어서 함수의 각 인자로 전달
    print(f_statistic)
    # print(p_value)
    print(f'{p_value:.24f}')

    # 시각화
    from matplotlib_encoder import hangul_encoding
    hangul_encoding()
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col1, y=col2, data=df_clean, order=category)
    plt.title(f'{col1}(교육수준)에 따른 {col2}(와인구매분포)')
    plt.xlabel(col1, fontsize=12)
    plt.ylabel(col2, fontsize=12)
    plt.tight_layout()
    plt.savefig('data/anova_boxplot.png')
    plt.show()
