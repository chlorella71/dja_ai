from make_graph import make_vertical_bar, make_horizontal_bar, make_pie_chart
import matplotlib.pyplot as plt

if __name__=="__main__":

    # column_name = "분류명"
    # column_name = "제품명"
    column_name = '프로모션'

    # 세로막대그래프 그리기
    make_vertical_bar(column_name)

    # 가로막대그래프 그리기
    make_horizontal_bar(column_name)

    # 원형그래프 그리기
    make_pie_chart(column_name)

