from main import make_merged_df #main.py(모듈이름)에 정의된 make_merged_df함수 불러오기
from matplotlib_encoder import hangul_encoding
import matplotlib.pyplot as plt
import seaborn as sns
# warnings.filterwarnings('ignore') # 경고메세지 보고싶지 않을때

# 분류명으로 groupby()된 테이블 확인해보기
def view_grouped_table(column_name):
    # pass
    from main import make_merged_df
    merged_df = make_merged_df()
    for key, table in merged_df.groupby(column_name):
        print(key)
        print(table)

# 세로막대그래프 그리기
def make_vertical_bar():
    # 함수 불러와서 리턴값 변수에 담기
    merged_df = make_merged_df()
    # print(merged_df)

    # 수량, 단가, 할인율로 판매금액 구하기
    merged_df['판매금액'] = merged_df['수량'] * merged_df['단가'] * (1 - merged_df['할인율'])
    # print(merged_df['판매금액'])
    # print(merged_df.keys())
    # print(merged_df)

    ## 분류명으로 groupby하기
    # 분류명 확인하기
    # print(merged_df['분류명'].unique())
    # 분류명당 총 판매금액 구하기
    category_table = merged_df.groupby('분류명')['판매금액'].sum().reset_index()
    # print(category_table)

    # 분류명으로 groupby()된 테이블 확인해보기
    # view_grouped_table('분류명')

    # plt 사용전 한글인코딩하기
    hangul_encoding()  # 한글 인코딩

    # 시각화(분류별 총 판매금액)
    plt.figure(figsize=(10, 6))
    # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    sns.barplot(x='분류명', y='판매금액', hue='분류명', data=category_table, palette='magma', dodge=False)
    plt.title('분류명별 판매금액')
    plt.xlabel('분류명')
    plt.ylabel('판매금액')
    # plt.xticks(rotation=45, ha='right')
    plt.legend().remove()
    # plt.tight_layout()
    plt.show()

# 가로막대그래프 그리기
def make_horizontal_bar():
    # 함수 불러와서 리턴값 변수에 담기
    merged_df = make_merged_df()
    # print(merged_df)

    # 수량, 단가, 할인율로 판매금액 구하기
    merged_df['판매금액'] = merged_df['수량'] * merged_df['단가'] * (1 - merged_df['할인율'])
    # print(merged_df['판매금액'])
    # print(merged_df.keys())
    # print(merged_df)

    ## 분류명으로 groupby하기
    # 분류명 확인하기
    # print(merged_df['분류명'].unique())
    # 분류명당 총 판매금액 구하기
    category_table = merged_df.groupby('분류명')['판매금액'].sum().reset_index()
    # print(category_table)

    # 분류명으로 groupby()된 테이블 확인해보기
    # view_grouped_table('분류명')

    # plt 사용전 한글인코딩하기
    hangul_encoding()  # 한글 인코딩

    # 시각화(제품별 총판매금액)
    category_table = merged_df.groupby('제품명')['판매금액'].sum().reset_index()
    category_table = category_table.sort_values(by='판매금액', ascending=False) # orderby처럼 정렬하기
    plt.figure(figsize=(10,6))
    # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    sns.barplot(x='판매금액', y='제품명', hue='제품명', data=category_table, palette='magma', dodge=False)
    plt.title('제품명별 판매금액')
    plt.xlabel('판매금액')
    plt.ylabel('제품명')
    # plt.xticks(rotation=45, ha='right')
    # plt.legend().remove()
    # plt.tight_layout()
    plt.show()


if __name__=="__main__":
    # 함수 불러와서 리턴값 변수에 담기
    merged_df = make_merged_df()
    # print(merged_df)

    # 수량, 단가, 할인율로 판매금액 구하기
    merged_df['판매금액'] = merged_df['수량'] * merged_df['단가'] * (1-merged_df['할인율'])
    # print(merged_df['판매금액'])
    # print(merged_df.keys())
    # print(merged_df)

    ## 분류명으로 groupby하기
    #분류명 확인하기
    # print(merged_df['분류명'].unique())
    #분류명당 총 판매금액 구하기
    category_table = merged_df.groupby('분류명')['판매금액'].sum().reset_index()
    # print(category_table)

    # 분류명으로 groupby()된 테이블 확인해보기
    # view_grouped_table('분류명')

    # plt 사용전 한글인코딩하기
    hangul_encoding() # 한글 인코딩

    # 시각화(분류별 총 판매금액)
    # category_table = merged_df.groupby('분류명')['판매금액'].sum().reset_index()
    # plt.figure(figsize=(10, 6))
    # # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    # sns.barplot(x='분류명', y='판매금액', hue='분류명', data=category_table, palette='magma', dodge=False)
    # plt.title('분류명별 판매금액')
    # plt.xlabel('분류명')
    # plt.ylabel('판매금액')
    # plt.xticks(rotation=45, ha='right')
    # # plt.legend().remove()
    # plt.tight_layout()
    # plt.show()

    # 시각화(제품별 총판매금액)
    # category_table = merged_df.groupby('제품명')['판매금액'].sum().reset_index()
    # category_table = category_table.sort_values(by='판매금액', ascending=False) # orderby처럼 정렬하기
    # plt.figure(figsize=(10,6))
    # # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    # sns.barplot(x='판매금액', y='제품명', hue='제품명', data=category_table, palette='magma', dodge=False)
    # plt.title('제품명별 판매금액')
    # plt.xlabel('판매금액')
    # plt.ylabel('제품명')
    # # plt.xticks(rotation=45, ha='right')
    # # plt.legend().remove()
    # # plt.tight_layout()
    # plt.show()

    # 도넛모양으로 프로모션별 판매금액 시각화하기
    category_table = merged_df.groupby('프로모션')['판매금액'].sum().reset_index().sort_values(by='판매금액', ascending=False)
    plt.figure(figsize=(10, 6))
    # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    plt.pie(category_table['판매금액'], labels=category_table['프로모션'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    plt.title('프로모션별 판매금액')
    plt.axis('equal')
    # plt.legend().remove()
    plt.tight_layout()
    plt.show()



    ## 내가 gpt로 해봄
    # 히스토그램 만들어보기
    # category_table = merged_df.groupby('분류명')['판매금액'].sum().reset_index()
    # plt.hist(category_table['판매금액'])

    # 막대그래프로 시각화해보기
    # category_table = merged_df.groupby('분류명')['판매금액'].sum().reset_index()
    # plt.figure(figsize=(10, 6))
    # plt.bar(category_table['분류명'], category_table['판매금액'], color='skyblue')
    # plt.xticks(rotation=45, ha='right')
    # plt.xlabel('분류명')
    # plt.ylabel('총 판매금액')
    # plt.title('분류별 총 판매금액')
    # plt.tight_layout()
    # plt.show()


