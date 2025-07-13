# pip install pandas openpyxl
import pandas as pd

if __name__ == "__main__":
    # pass

    # Sales.xlsx 가져오기
    sales_df = pd.read_excel("data/Sales.xlsx", sheet_name="Sheet1") # sibling(형제관계)는 데이터를 바로 읽어올 수 있음
    # print(sales_df)
    # exit()

    # Details.xlsx 가져오기
    detail_df = pd.read_excel("data/Details.xlsx", sheet_name=None) # sheet_name=None은 모든 시트 가져오기

    # 각 시트를 df프레임으로 만들기, Sales.xlsx는 시트가 1개여서 할 필요 없었음
    promo_df=detail_df["프로모션"]
    channel_df=detail_df["채널"]
    region_df=detail_df["지역"]
    product_df=detail_df["제품"]
    category_df=detail_df["분류"]
    date_df=detail_df["날짜"]
    subcategory_df = detail_df["제품분류"]
    customer_df=detail_df["고객"]

    # 필드명만 출력해보기
    # print(sales_df.keys())
    # print(channel_df.keys())

    # 이름이 같은 필드를 연결해서 Sales.xlsx에 Details.xlsx 병합
    sales_df = pd.merge(sales_df, channel_df, on="채널코드", how="left")
    # print(sales_df.keys())
    sales_df = pd.merge(sales_df, product_df, on="제품코드", how="left")
    # print(sales_df.keys())
    sales_df = pd.merge(sales_df, subcategory_df, on="제품분류코드", how="left")
    # print(sales_df.keys())
    sales_df = pd.merge(sales_df, category_df, on="분류코드", how="left")
    # print(sales_df.keys())
    sales_df = pd.merge(sales_df, customer_df, on="고객코드", how="left")
    # print(sales_df.keys())
    sales_df = pd.merge(sales_df, region_df, on="지역코드", how="left")
    # print(sales_df.keys())
    sales_df = pd.merge(sales_df, promo_df, on="프로모션코드", how="left")
    # print(sales_df.keys())

    # 날짜는 날짜코드가 존재하지않습니다. 그래서 날짜필드 자체를 날짜타입으로 전환해서 merge합니다
    sales_df["날짜"] = pd.to_datetime(sales_df["날짜"])
    # print(sales_df)
    sales_df = pd.merge(sales_df, date_df, on="날짜", how="left")
    # print(sales_df.keys())

    # 지역_x, 지역_y가 같은 컬럼인지 확인
    # print(sales_df[['지역_x', '지역_y']])

    # 필요한 필드만 추출
    fields= ['날짜', 'Quantity', 'UnitPrice', '지역_x', '채널명', '색상', '원가', '제품분류코드', '제품분류명', '분류명', '고객명', '성별', '생년월일', '시도', '구군시', '프로모션', '할인율']
    # print(*fields)
    # print([*fields])

    # salse_df를 필요한 필드만 남기기
    sales_df = sales_df[[*fields]]
    # print(sales_df.keys())

    # Quantity, UnitPrice 이름 바꾸고 salse_df를 최종 view테이블로 수정
    sales_df.rename(columns= {"Quantity": "수량", "UnitPrice":"단가", "지역_x":"지역"}, inplace=True)
    print(sales_df)

    # 단가와 수량에 할인율을 곱한 판매가 계산하기
    sales_df["판매가"] = sales_df["단가"] * sales_df["수량"] * (1-sales_df["할인율"])
    # print(sales_df)