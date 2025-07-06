import pandas as pd


def add(a, b):
    return a+b

def printf(국어):
    return 국어


if __name__== "__main__":
    # for문 돌리기
    # for i in range(1, 4): # row
    #     for j in range(i): # columns
    #         print('*', end='')
    #     print(end='\n') # print()과 같음

    ## list에 넣기
    # table = []
    # for i in range(1, 4):
    #     row = []
    #     for j in range(i):
    #         row.append("*") # 배열에 값추가
    #     table.append(row)
    # print(table)

    ## for문
    # row= []
    # for _ in range(5):
    #     row.append('*')
    # print(row)

    ## comfrehension
    # row = ['*' for _ in range(5)]
    # print(row)

    ## if문
    # row=[]
    # for item in range(10):
    #     if item%2==0:
    #         row.append(item)
    # print(row)

    ## comfrehension
    # row = [item for item in range(10) if item%2==0]
    # print(row)

    ## 삼항연산자
    # item = 5
    # result= "짝수" if item%2==0 else "홀수"
    # print(result)

    # row=[]
    # for item in range(10):
    #     if item%2==0:
    #         row.append("짝수")
    #     else:
    #         row.append("홀수")
    # print(row)

    # row= ["짝수" if item%2==0 else "홀수" for item in range(10)]
    # print(row)

    ## 2중 for문
    # row = ['*' for j in range(5)]
    # table = [['*' for j in range(i)] for i in range(1, 4)]
    # print(row)
    # print(table)

    ## table = [['*' for j in range(i)] <여기에 if도 넣을 수 잇음> for i in range(1, 4)]
    # table = [['*' for j in range(i) if j % 2 == 0] for i in range(1, 4)]
    # print(table)

    ## add()함수 호출
    # result = add(10, 11)
    # print(result)

    ## 함수 3번 호출(10, 11), (23, 45), (78, 100)
    # result1 = add(10, 11)
    # result2 = add(23, 45)
    # result3 = add(78, 100)
    # print(result1, result2, result3)

    ## map 사용
    # list1 = [10, 23, 78]
    # list2 = [11, 45, 100]
    # results = map(add, list1, list2)
    # print(list(results)) # 그냥 찍으면 results의 object hash값이 출력됨, list로 변환해줘야함

    df =pd.DataFrame()
    df["국어"] = [89,100,98]
    # print(df)
    result = df["국어"].apply(printf) # pandas의 map은 apply
    print(result)
    exit()