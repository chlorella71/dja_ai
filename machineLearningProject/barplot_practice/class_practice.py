# class : object(dictionary)를(ex. { 국어: 90, ... }) 생성하는 스키마(Schema: 설계도)
import pandas as pd

class Scores:
    # class 내장함수: __init__, __repr__, ... __함수이름__ 형태는 내장함수를 의미?
    def __init__(self, 이름, 국어, 영어, 수학, 과학): # initialize
        self.name = 이름
        self.kor = 국어
        self.eng = 영어
        self.math = 수학
        self.sci = 과학

    def __repr__(self): # represent
        return f'{self.name}'

    def __call__(self): # action
        return (self.kor + self.eng + self.math + self.sci)/4


    # dict 형태로 변환(DataFrame 만들때 유용)
    def to_dict(self):
        return {
            '이름': self.name,
            '국어': self.kor,
            '영어': self.eng,
            '수학': self.math,
            '과학': self.sci
        }

if __name__ == "__main__":
    scores= {'이름': 'john', '국어': 90, '영어': 80, '수학': 70, '과학': 60}
    # print(scores)
    scores = Scores('john', 90, 80, 70, 60)
    # print(scores.__dict__)

    ## __init__() 실행해보기
    john = Scores('john', 91, 81, 71, 61)
    peter = Scores('peter', 92, 82, 72, 62)
    print(john.__dict__)
    # print(peter.__dict__)

    table = [john.__dict__, peter.__dict__]
    # print(table)

    ## __repr__() 실행해보기
    print(john)
    # print(peter)

    ## __call__() 실행해보기
    # print(john())
    # print(peter())
    mean = john()
    print(mean)

    ## to_dict()를 이용해서 list comfrehension을 화용해서 DataFrame으로 변환
    students = [
        Scores('john', 91, 81, 71, 61),
        Scores('peter', 92, 82, 72, 62),
        Scores('sue', 93, 83, 73, 63)
    ]
    df = pd.DataFrame([student.to_dict() for student in students])
    # print(df)

