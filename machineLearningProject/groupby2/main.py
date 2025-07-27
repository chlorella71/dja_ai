import pandas as pd
import openpyxl

# xlsx => openpyxl
def make_merged_df():
    # Details.xlsx파일 읽어서 dataframe으로 변환
    Detail_df = pd.read_excel("data/Details.xlsx", sheet_name=None)  # sheet_name=None, 시트 다가져오기
    # sheet_name=None일때는 excel파일의 모든 sheet를 딕셔너리 형태로 읽어옴
    # { '시트1':DataFrame, '시트2':DataFrame, ... }
    # 그래서 []안에는 '시트이름'이 지정됨
    product_df = Detail_df["제품"]
    region_df = Detail_df["지역"]
    promotion_df = Detail_df["프로모션"]
    channel_df = Detail_df["채널"]
    date_df = Detail_df["날짜"]  # 날짜, 날짜 코드가 없음. 그래서 날짜타입으로 전환?
    date_df['날짜'] = pd.to_datetime(date_df['날짜'])
    customer_df = Detail_df["고객"]
    category_df = Detail_df["분류"]
    product_category_df = Detail_df["제품분류"]

    # Sales.xlsx파일 읽어서 dataframe으로 변환
    # sheet_name='시트이름' 또는 sheet_name=0은 특정 시트만 읽어옴
    # 반환값은 단일 DataFrame임, []안에는 '칼럼이름'이 지정됨
    Sale_df = pd.read_excel("data/Sales.xlsx", sheet_name="Sheet1")
    Sale_df['날짜'] = pd.to_datetime(Sale_df['날짜'])

    # merge, 왼쪽, 오른쪽, on="공통필드", how"left"
    merged_df = pd.merge(Sale_df, product_df, on="제품코드", how='left')
    merged_df = pd.merge(merged_df, product_category_df, on="제품분류코드", how='left')
    merged_df = pd.merge(merged_df, category_df, on="분류코드", how="left")
    merged_df = pd.merge(merged_df, customer_df, on="고객코드", how="left")
    merged_df = pd.merge(merged_df, region_df, on="지역코드", how="left")
    merged_df = pd.merge(merged_df, channel_df, on="채널코드", how="left")
    merged_df = pd.merge(merged_df, promotion_df, on="프로모션코드", how="left")
    merged_df = pd.merge(merged_df, date_df, on="날짜", how="left")
    # print(merged_df.keys())  # column의 key값들을 확인하고 필요한 columns만 추출
    feature_names = ['날짜', 'Quantity', '지역_x',
                     '제품명', '색상', '원가', '단가', '제품분류명', '분류명',
                     '고객명', '성별', '생년월일', '시도', '구군시', '채널명', '프로모션', '할인율']
    merged_df = merged_df[feature_names]  # feature_names리스트에 담긴 columns들만 남기고 나머지 버리기
    merged_df.rename(columns={'Quantity': '수량', '지역_x': '지역'}, inplace=True)  # columns_name 변경하기
    # print(merged_df.head())  # 맨 앞 데이터 5개만 추출하기
    return merged_df


if __name__ == "__main__":
    # pass
    merged_df = make_merged_df()
    # print(merged_df)

    #excel파일로 변환해서 저장, index=False는 index값을 첫번째열로 생성하지 않기
    # merged_df.to_excel('data/merged_sales.xlsx', index=False)