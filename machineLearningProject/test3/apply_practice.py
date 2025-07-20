import pandas as pd

def sales1(df):
    # print(df)
    # exit()
    sales_price = df['수량']*df["단가"]
    return sales_price


def sales2(수량, 단가):
    return 수량*단가

#유클리드 알고리즘
#피제수와 제수의 최대공약수는 제수와 그 나머지의 최대공약수와 같음
# def euclid(a, b):
#     while(1):
#         r = a%b
#         a=b
#         b=r
#         if r==0: break # 함수의 자식인 while문만 멈춤
#     print("Hello1")
#     return a
#     print("Hello2") # return은 함수를 멈추는 기능, 그래서 return 이후에는 함수가 실행되지 않음
# def euclid(a, b):
#     while(1):
#         r = a%b
#         a=b
#         b=r
#         if r==0: return a # return은 함수를 멈추는 기능, 그래서 return 이후에는 함수가 실행되지 않음
#     print("Hello1")
#     return a
#     print("Hello2")
def euclid(a, b):
    while (1):
        r = a % b
        a, b = b, r # 동시할당(다중할당, 튜플언패킹)
        if r == 0: return a


if __name__ == "__main__":
    # xlxs 파일 읽기
    df = pd.read_excel("data/Sales.xlsx", sheet_name="Sheet1")

    # column 이름 수정하기
    df.rename(columns={"Quantity": "수량", "UnitPrice":"단가"}, inplace=True)
    # print(df.keys())
    # exit()

    # apply 함수
    results = df.apply(sales1, axis=1)
    # print(results)

    # lambda 함수
    map = lambda a, b, c : (a+b+c)/3
    result = map(90, 89, 90)
    # print(result)

    f = lambda x, y: 2*x + 3*4 + 3
    result = f(2, 4)
    # print(result)

    # apply(), lambda활용하여 수량, 단가를 곱한 값 계산
    results= df.apply(lambda df: sales2(df['수량'], df['단가']), axis=1)
    # print(results)
    results = df.apply(lambda df: df['수량']*df['단가'], axis=1)
    # print(results)
    results = df.apply(lambda row: row['수량'] * row['단가'], axis=1)
    # print(results)

    # groubby 함수
    groups = df.groupby('제품코드')
    groups = df.groupby('고객코드')
    # print(groups)
    # for key, table in groups:
    #     print(key)
    #     print(table)

    df['판매가'] = df.apply(lambda row: row['수량']*row['단가'], axis=1)
    groups_sale_price = df.groupby('고객코드')['판매가'].sum()
    groups_sale_price = df.groupby('고객코드')['판매가'].max()
    groups_sale_price = df.groupby('고객코드')['판매가'].mean()
    # print(groups_sale_price)

    each_customer_sale_price_table= df.groupby('고객코드')['판매가'].sum().to_frame() # Series형태이므로 dataframe형태(table)로 변환?
    # print(each_customer_sale_price_table.max(axis=0))
    each_customer_sale_price_table= df.groupby('고객코드')['판매가'].sum().reset_index() # 고객코드가 index로 되어있으므로 index에서 제외하여 고객코드도 출력
    # print(each_customer_sale_price_table.max(axis=0))

    # 알고리즘
    gcd= euclid(32, 24)
    # print(gcd)

    # 동시할당(다중할당, 튜플언패킹)
    arrs = [1, 2, 3, 4]
    a, b, c, d = arrs
    print(a, b, c, d)
    a, b, *tmp = arrs # *는 list를 복제해서 풀어헤치는것
    print(a, b, c, d)
    print(a, b, tmp)