from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import pandas as pd

if __name__ == "__main__":
    page = 1
    data = []
    columns = []
    try:
        while (1):
            url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            if not soup.find_all("strong")[-1].text.isdigit():
                break
            trs = soup.find("table").find_all("tr")[1:]
            if page == 1:
                ths = soup.find("table").find_all("tr")[0].find_all("th")
                columns = [th.text for idx, th in enumerate(ths) if idx != 4]
            table = [[td.text for idx, td in enumerate(tr.find_all("td")) if idx != 4] for tr in tqdm(trs)]
            data += table

            page += 1
    except Exception:
        print(Exception)
    df = pd.DataFrame(data, columns=columns)
    print(df)


# if __name__ =="__main__":
#     url ="https://www.coffeebeankorea.com/menu/list.asp?category=13"
#     html = requests.get(url).text
#     # print(html)
#     soup = BeautifulSoup(html, "html.parser")
#     # print(soup)
#     dd = soup.find("dd")
#     # print(dd)
#     datum = soup.find("dd").text
#     # print(datum)
#     data = soup.find_all("dd")
#     # print(len(data))
#     # arrs = []
#     # for datum in data:
#     #     arrs.append(datum.text.strip()) #strip()은 java의 trim()같은거
#     arrs = [datum.text.strip() for datum in data]
#     # print(arrs)
#     arrs = [datum.text.strip() for idx, datum in enumerate(data) if idx % 2 == 0]
#     # print(len(arrs))
#     arrs2 = [datum.text.strip() if idx%2==0 else "홀수" for idx, datum in enumerate(data)]
#     # print(len(arrs2))
#     ul = soup.find("ul")
#     # print(ul)
#     ul = soup.find("ul").find("li")   # 트리구조
#     # print(ul)
#     ul = soup.find("ul").find("li").find("a").text
#     # print(ul)
#     data = soup.find("body")
#     # print(data)
#     data = soup.find("body").find("form")
#     # print(data)
#     data = soup.find("body").find("form").find("fieldset")
#     # print(data)
#     data = soup.find("body").find("form").find("fieldset").find("legend")
#     # print(data)
#     data = soup.find("body").find("form").find("fieldset").find("legend").text
#     # print(data)
#     data = soup.find("body").find_all("form")
#     # print(data)
#     # print(len(data))
#     data = soup.find("body").find_all("form")[0]
#     # print(data)
#     data = soup.find("body").find_all("form")[0].find("input")
#     # print(data)
#
#     page=1
#     # page = 46
#     try:
#         while (1):
#             url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="  # 할리스커피
#             #page +=1
#             # print(page)
#             html = requests.get(url).text
#             soup = BeautifulSoup(html, 'html.parser')
#             # print(soup)
#             # print(soup.find("strong"))
#             # print(soup.find_all("strong"))
#             # print(soup.find_all("strong")[-1]) # 맨마지막꺼 찾기
#             # print(soup.find_all("strong")[-1].text)
#             # print(len(soup.find_all("table")))
#             # print(soup.find("table").find_all("tr"))
#             # print(soup.find("table").find_all("tr")[0].find("th")) # 테이블의 칼럼명 가져오기
#
#             # print(soup.find("table").text)
#             # print(soup.find("table").find_all("tr")[0].find_all("th")[0].text)
#             # print(soup.find("table").find_all("tr")[1].find_all("td")[0].text)
#             columns = [th.text.strip() for th in soup.find("table").find("tr").find_all("th")]
#             # print(columns)
#             # print([td.text.strip() for td in soup.find("table").find_all("tr")[1].find_all("td")])
#             # for tr in soup.find("table").find_all("tr"):
#             #     print([td.text.strip() for td in tr.find_all("td")])
#             rows= [[td.text.strip() for td in tr.find_all("td")] for tr in soup.find("table").find_all("tr")]
#             # print(rows)
#
#         # exit()
#         # if not soup.find_all("strong")[-1].text.isdigit():
#         #     break
#         # print(page)
#         # exit()
#         page += 1
#     except Exception as e:
#         print(e)
#
#     # arr1 = [1, 3]
#     # arr2 = [2, 4]
#     # print(arr1+arr2)

