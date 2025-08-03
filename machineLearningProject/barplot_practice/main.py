import pandas as pd
import matplotlib.pyplot as plt
from korean_encoding import korean_font_config

def make_line_graph(year):
    import pandas as ad
    df = pd.read_csv('data/sales.csv')
    # df.info()
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df['날짜'] = pd.to_datatime(df['날짜'])
    df['년도'] = df['날짜'].dt.year
    df['월'] = df['날짜'].dt.month
    df['판매금액'] = df['단가'] * df['수량'] * (1 - df['할인율'])
    feature_names = ['년도', '월', '판매금액']
    # ...



if __name__ == "__main__":
    korean_font_config()
    df = pd.read_csv('data/book_cp949.csv', encoding='cp949')
    # print(df)

    df = pd.read_csv('data/sales.csv')
    # print(df)
    ## df.info(): Pandas Dataframe의 요약정보를 출력하는 메서드
    ## 데이터 탐색(EDA) 초반에 데이터 구조를 빠르게 확인할 때 사용할 수 있음
    # df.info() # object(문자열), int64(정수), float64(유리수), datetime(날짜타입), null/non-null(데이터 빈값이 있는가?)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    # print(df)

    ## 2018.1 ~ 12 ~ 2022.1 ~ 12 년도별 월별 판매액 추이 구하기
    # 날짜 => 년도, 월, 판매금액
    df['날짜'] = pd.to_datetime(df['날짜'])
    # .dt 접근자: Pandas에서 datetime타입 column전용 속성/메서드를 제공하는 기능중 하나
    df['년도'] = df['날짜'].dt.year
    df['월'] = df['날짜'].dt.month
    df['판매금액'] = df['단가'] * df['수량'] * (1-df['할인율'])
    # print(df)

    # print(df.keys())
    feature_names = ['년도', '월', '판매금액']
    year_month_sales_df = df[feature_names]
    # print(year_month_sales_df)
    # df column명을 변수에 담아 활용하기
    year, month, salePrice = '년도', '월', '판매금액'
    # groupby()는 집계함수(sum())과 같이 사용, 자동 생성되는 인덱스를 제거(reset_index())하여 최종 df 생성
    year_month_sales_df = df[feature_names].groupby([year, month]).sum().reset_index()
    # print(year_month_sales_df)
    year_month_sales_df = df[feature_names]\
        .groupby([year, month])[salePrice].sum()\
        .reset_index()
    years = year_month_sales_df['년도'].unique() # '년도'별 unique한 값만 출력
    # print(years)

    ## 그래프 틀 만들기
    ## fig: 전체 캔버스
    ## ax: 실제 차트를 그리는 영역
    ## figsize(가로inch, 세로inch): 도화지 크기 설정
    fig, ax = plt.subplots(figsize=(12, 8))

    ## 2018년도 월별 판매액 그래프 그리기
    line_data = year_month_sales_df[year_month_sales_df[year] == 2018] # 날짜 타입은 숫자타입으로 인식?
    # print(line_data)
    x, y = line_data[month], line_data[salePrice]
    # print(x)
    # print(y)
    ax.plot(x, y, label='2018', marker='.', markersize=5)
    # plt.show()

    ## 2019년도 월별 판매액 그래프 그리기
    line_data = year_month_sales_df[year_month_sales_df[year] == 2019]
    x, y = line_data[month], line_data[salePrice]
    ax.plot(x, y, label='2019', marker='.', markersize=5)
    # plt.show() # plt.show()를 최종적으로 한번에 하면 년도별 그래프가 합쳐서 보여짐

    ## for문 활용하여 '년도'별 월 판매금액 선형 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 8))
    for item in years:
        line_data = year_month_sales_df[year_month_sales_df[year] == item]
        x, y = line_data[month], line_data[salePrice]
        ax.plot(x, y, label=item, marker='.', markersize=5)
    ax.set_title('년도별 월별 판매총액 추이 그래프', fontsize=15)
    ax.set_xlabel(month, fontsize=14)
    ax.set_ylabel(salePrice, fontsize=14)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()