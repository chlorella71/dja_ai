import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, pearsonr, spearmanr
from korean_encoding import korean_font_config

korean_font_config()

# p-value(상관계수) 계산 함수(유의성 판단)
def corr_pvals(X: pd.DataFrame, method='pearson') -> pd.DataFrame:
    cols = X.columns
    P = pd.DataFrame(index=cols, columns=cols, dtype=float)
    for i, ci in enumerate(cols):
        for j, cj in enumerate(cols):
            x, y = X[ci], X[cj]
            mask = x.notna() & y.notna()
            if mask.sum() < 3:
                P.iloc[i, j] = np.nan
                continue
            if method == 'pearson':
                _, p = pearsonr(x[mask], y[mask])
            else:
                _, p = spearmanr(x[mask], y[mask])
            P.iloc[i, j] = p
    return P

# 상관 높은 페어 Top-N 뽑기(중복/대각 제외)
def top_corr_pairs(corr: pd.DataFrame, n=10):
    corr_abs = corr.abs()
    mask = np.triu(np.ones_like(corr_abs, dtype=bool), k=1) # 위 삼각행렬(대각 제외)
    pairs = corr_abs.where(mask).stack().sort_values(ascending=False)
    return pairs.head(n)

# (선택) p-value를 임계치로 필터해서 중요 페어만 보기
ALPHA=0.5
def significant_pairs(corr: pd.DataFrame, pvals: pd.DataFrame, alpha=ALPHA, topn=10):
    corr_abs = corr.abs()
    # 상삼각 + 유의한 페어만
    mask = (np.triu(np.ones_like(corr_abs, dtype=bool), k=1)) & (pvals.values < alpha)
    sig = pd.DataFrame(corr_abs.where(mask)).stack().sort_values(ascending=False)
    return sig.head(topn)

if __name__ == "__main__":
    df = pd.read_csv('data/Automobile_data.csv')
    # field_name을 한글로 번역하기
    field_translation = {
        "symboling": "위험등급",
        "normalized-losses": "정규화손실",
        "make": "제조사",
        "fuel-type": "연료종류",
        "aspiration": "흡기방식",
        "num-of-doors": "문의개수",
        "body-style": "차체형태",
        "drive-wheels": "구동방식",
        "engine-location": "엔진위치",
        "wheel-base": "축거",
        "length": "길이",
        "width": "너비",
        "height": "높이",
        "curb-weight": "공차중량",
        "engine-type": "엔진유형",
        "num-of-cylinders": "실린더수",
        "engine-size": "엔진배기량",
        "fuel-system": "연료시스템",
        "bore": "실린더내경",
        "stroke": "피스톤행정",
        "compression-ratio": "압축비",
        "horsepower": "마력",
        "peak-rpm": "최대회전수",
        "city-mpg": "도심연비(mpg)",
        "highway-mpg": "고속도로연비(mpg)",
        "price": "가격"
    }
    # DataFrame에 적용하기
    df.rename(columns=field_translation, inplace=True)
    # print(df)

    # 도심연비(mpg) 출력해보기
    # print(df['도심연비(mpg)'].unique()) # unique한 값 출력
    # print(df['도심연비(mpg)'].shape) # 개수 출력
    # print(sorted(df['도심연비(mpg)'].unique())) # unique값을 정렬해서 출력

    df.loc[(df['도심연비(mpg)'] > 9) & (df['도심연비(mpg)'] < 20), '도심연비(mpg)'] = 10
    df.loc[(df['도심연비(mpg)'] > 19) & (df['도심연비(mpg)'] < 30), '도심연비(mpg)'] = 20
    df.loc[(df['도심연비(mpg)'] > 29) & (df['도심연비(mpg)'] < 40), '도심연비(mpg)'] = 30
    df.loc[(df['도심연비(mpg)'] > 39) & (df['도심연비(mpg)'] < 50), '도심연비(mpg)'] = 40

#--- 구동방식과 도심연비(mpg)의 관계 파악하기
    # 카이제곱으로 구해서 횟수를 헤아려서 횟수에 의미가 있는지 분석, chi2
    # 카이제곱은 범주데이터를 학습할때 유의미성을 계산?
    # print(df['구동방식'])
    table = pd.crosstab(df['구동방식'], df['도심연비(mpg)'])
    table = pd.crosstab(df['구동방식'], df['고속도로연비(mpg)'])
    # print(table)
    chi2, p_value, dof, expected = chi2_contingency(table)
    # print(f'{p_value:0.10f}') # 0.05 보다 작으면 상관관계 있음

#--- 데이터 정규화하기
    #df['실린더수']를 영어에서 숫자로 바꾸기
    # print(df['실린더수'].unique())
    cylinder = {
        'four':4,
        'six':6,
        'five':5,
        'three':3,
        'twelve':12,
        'two':2,
        'eight':8
    }
    # df['실린더수'] = df['실린더수'].replace(cylinder)
    df['실린더수'] = df['실린더수'].map(cylinder) # map도 되고 replace도 되는듯
    # print(df['실린더수'].unique())

    # 문의개수
    # print(df['문의개수'].unique())
    # print(df.info())
    df = df[df['문의개수'] != '?']
    # print(df)
    count_door = {
        'two':2,
        'four':4,
        '?':0
    }
    df['문의개수'] = df['문의개수'].map(count_door)
    # print(df['문의개수'].unique())
    # print(df['문의개수'])

    # 정규화손실
    # print(df['정규화손실'].unique())
    df = df[df['정규화손실'] != '?']
    # print(df)

    # 가격
    # print(df['가격'].unique())
    df['가격'] = df['가격'].astype('int64')
    # print(df.info())

    # 마력
    # print(df['마력'].unique())
    df['마력'] = df['마력'].astype('int64')
    # print(df.info())

    # 최대회전수
    # print(df['최대회전수'].unique())
    df['최대회전수'] = df['최대회전수'].astype('int64')
    # print(df.info())

    # 실린더내경
    # print(df['실린더내경'].unique())
    # df['실린더내경'] = df['실린더내경'].astype('float64')
    bores = {
        '3.19' :3.19,
        '3.13' :3.13,
        '3.5' :3.5,
        '3.31' :3.31,
        '2.91' :2.91,
        '3.03' :3.03,
        '2.97' :2.97,
        '3.34' :3.34,
        '3.6' :3.6,
        '2.92':2.92,
        '3.15' :3.15,
        '3.63' :3.63,
        '3.08' :3.08,
        '?' :0.0,
        '3.39' :3.39,
        '3.76' :3.76,
        '3.58' :3.58,
        '3.46' :3.46,
        '3.17' :3.17,
        '3.35' :3.35,
        '2.99':2.99,
        '3.33' :3.33,
        '3.43' :3.43,
        '3.7' :3.7,
        '3.61' :3.61,
        '3.94' :3.94,
        '3.54' :3.54,
        '2.54' :2.54,
        '3.62' :3.62,
        '3.05' :3.05,
        '3.27':3.27,
        '3.24' :3.24,
        '3.01' :3.01,
        '3.78':3.78
    }
    df['실린더내경'] = df['실린더내경'].map(bores)
    # print(df['실린더내경'].unique())

    # 숫자 데이터만 뽑아보기
    field_translation = [
        "위험등급",
        "문의개수",
        "축거",
        "길이",
        "너비",
        "높이",
        "공차중량",
        "실린더수",
        "엔진배기량",
        "실린더내경",
        "압축비",
        "마력",
        "최대회전수",
        "도심연비(mpg)",
        "고속도로연비(mpg)",
        "가격"
    ]
    df = df[field_translation]
    # print(df.keys())

#--- 상관계수와 heatmap 구해보기
    corr_pearson = df.corr(method='pearson')
    corr_spearman = df.corr(method='spearman')

    # 상관계수 구하기
    p_pearson = corr_pvals(df, method='pearson')
    p_spearman = corr_pvals(df, method='spearman')
    # print(p_pearson)
    # print(p_spearman)

    # heatmap 저장
    plt.figure(figsize=(12,10))
    sns.heatmap(
        corr_pearson, annot=True, fmt=".2f",
        linewidths=.5, square=True, cbar_kws={'shrink': .8}
    )
    plt.title('피어슨 상관계수 히트맵')
    plt.tight_layout()
    plt.savefig("data/corr_pearson_heatmap.png", dpi=150)
    plt.close()

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        corr_spearman, annot=True, fmt=".2f",
        linewidths=.5, square=True, cbar_kws={'shrink': .8}
    )
    plt.title("스피어만 상관계수 히트맵")
    plt.tight_layout()
    plt.savefig('data/corr_spearman_heatmap.png', dpi=150)
    plt.close()

    # (선택) 군집형으로 재배열한 클러스터맵(패턴 보기 좋음)
    cg = sns.clustermap(corr_spearman, figsize=(12,12), annot=True, fmt='.2f', cbar_kws={'shrink': .8})
    cg.savefig('data/corr_spearman_clustermap.png', dpi=150)
    plt.close()

    # 상관 높은 페어 Top-N 뽑기(중복/대각 제외)
    # print("\n[피어슨 상관 Top 10]")
    # print(top_corr_pairs(corr_pearson, n=10))

    # print("\n[스피어만 상관 Top 10]")
    # print(top_corr_pairs(corr_spearman, n=10))

    # (선택) p-value를 임계치로 필터해서 중요 페어만 보기
    print("\n[피어슨 유의한 페어 Top 10 (p<0.05)]")
    print(significant_pairs(corr_pearson, p_pearson, alpha=0.05, topn=10))

    print("\n[스피어만 유의한 페어 Top 10 (p<0.05)]")
    print(significant_pairs(corr_spearman, p_spearman, alpha=0.05, topn=10))


    # 마력과 도심연비(mpg)의 상관관계 구해보기 - anova사용


