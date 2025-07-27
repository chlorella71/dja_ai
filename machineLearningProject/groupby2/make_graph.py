from main import make_merged_df
from matplotlib_encoder import hangul_encoding
import matplotlib.pyplot as plt
import seaborn as sns

## 총판매금액 그래프 그리기
# 세로막대그래프 그리기
def make_vertical_bar(column_name):
    # 함수 불러와서 리턴값 변수에 담기
    merged_df = make_merged_df()

    # 수량, 단가, 할인율로 판매금액 구하기
    merged_df['판매금액'] = merged_df['수량'] * merged_df['단가'] * (1 - merged_df['할인율'])

    # 분류명으로 groupby하기
    category_table = merged_df.groupby(column_name)['판매금액'].sum().reset_index()

    # plt 사용전 한글인코딩하기
    hangul_encoding()  # 한글 인코딩

    # 시각화(분류별 총 판매금액)
    plt.figure(figsize=(10, 6))
    # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    sns.barplot(x=column_name, y='판매금액', hue=column_name, data=category_table, palette='magma', dodge=False)
    plt.title(f'{column_name}별 판매금액')
    plt.xlabel(column_name)
    plt.ylabel('판매금액')
    plt.xticks(rotation=45, ha='right')
    # plt.legend().remove()
    plt.tight_layout()
    plt.savefig('data/vertical_bar.png')
    plt.show()

# 가로막대그래프 그리기
def make_horizontal_bar(column_name):
    # 함수 불러와서 리턴값 변수에 담기
    merged_df = make_merged_df()

    # 수량, 단가, 할인율로 판매금액 구하기
    merged_df['판매금액'] = merged_df['수량'] * merged_df['단가'] * (1 - merged_df['할인율'])

    ## 분류명으로 groupby하기
    category_table = merged_df.groupby(column_name)['판매금액'].sum().reset_index()

    # plt 사용전 한글인코딩하기
    hangul_encoding()  # 한글 인코딩

    # 시각화(제품별 총판매금액)
    category_table = merged_df.groupby(column_name)['판매금액'].sum().reset_index()
    category_table = category_table.sort_values(by='판매금액', ascending=False) # orderby처럼 정렬하기
    plt.figure(figsize=(10,6))
    # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    sns.barplot(x='판매금액', y=column_name, hue=column_name, data=category_table, palette='magma', dodge=False)
    plt.title(f'{column_name} 판매금액')
    plt.xlabel('판매금액')
    plt.ylabel(column_name)
    # plt.xticks(rotation=45, ha='right')
    # plt.legend().remove()
    plt.tight_layout()
    plt.savefig('data/horizontal_bar.png')
    plt.show()

# 원형그래프 그리기
def make_pie_chart(column_name):
    # 함수 불러와서 리턴값 변수에 담기
    merged_df = make_merged_df()

    # 수량, 단가, 할인율로 판매금액 구하기
    merged_df['판매금액'] = merged_df['수량'] * merged_df['단가'] * (1 - merged_df['할인율'])

    ## 분류명으로 groupby하기
    category_table = merged_df.groupby(column_name)['판매금액'].sum().reset_index()

    # plt 사용전 한글인코딩하기
    hangul_encoding()  # 한글 인코딩

    # 도넛모양으로 프로모션별 판매금액 시각화하기
    category_table = merged_df.groupby(column_name)['판매금액'].sum().reset_index().sort_values(by='판매금액', ascending=False)
    plt.figure(figsize=(10, 6))
    # hue='', seaborn에서 색깔로 나누고 싶은 카테고리 범주
    plt.pie(category_table['판매금액'], labels=category_table[column_name], autopct='%1.1f%%', startangle=90,
            colors=sns.color_palette('pastel'))
    plt.title(f'{column_name}별 판매금액')
    plt.axis('equal')
    # plt.legend().remove()
    plt.tight_layout()
    plt.savefig('data/pie_chart.png')
    plt.show()