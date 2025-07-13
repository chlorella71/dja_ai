
# def average(국어, 영어, 수학):
#     avg= (국어 + 영어 + 수학)/3
#     return avg

## destructuring unpacking
# def average(*scores):
#     # print(scores)
#     avg = (scores[0]+scores[1]+scores[2])/3
#     return avg

## default값 설정, object구조
# def average(국어=70, 영어=70, 수학=70):
#     print(영어)
#     avg = (국어+영어+수학)/3
#     return avg


def average(**obj):
    print(obj)


if __name__ == "__main__":
    # result=average(90, 85, 95)
    # print(result)

    ## destructuring unpacking
    # scores = [90, 85, 95]
    # result= average(*scores)
    # print(result)

    # scores = [90, 85, 95]
    # result = average(*scores)
    # print(result)

    ## default값 설정
    # result=average()
    # print(result)
    # result=average(90)
    # print(result)
    # result=average(영어=80)

    # scores = {"국어": 90, "수학": 95, "영어": 85} # object는 순서가 바뀌어도 상관없음
    # result = average(**scores)
    # print(result)

    scores = {"국어": 90, "영어": 85, "수학": 95}
    result = average(**scores)
    print(result)



