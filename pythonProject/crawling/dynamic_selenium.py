from bs4 import BeautifulSoup
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time  # 시간 지연
import pandas as pd
from driver import chrome_driver

if __name__=="__main__":
    url = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=41&sido=&gugun=&store="
    driver = chrome_driver() # 항상 살아서 움직여야하기 때문에 맨 위에 둠
    driver.get(url)
    time.sleep(2)
    # driver.find_element(By.LINK_TEXT, '2').click()  # s가 붙으면 여러개
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # time.sleep(2)
    # exit()

    page = 46
    data = []
    columns = []
    while(1):
        try:
            if page%10 != 1:
                driver.find_element(By.LINK_TEXT, f'{page}').click()  # s가 붙으면 여러개
                time.sleep(2)
                #//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[10]/img
                #//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[11]/img
            if page % 10 == 1 and page !=1:
                if page == 11:
                    driver.find_element(By.XPATH,
                                        '''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[10]/img''').click()
                    time.sleep(2)
                else:
                    driver.find_element(By.XPATH, '''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[11]/img''').click()
                    time.sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            trs = soup.find("table").find_all("tr")[1:]
            if page == 46:
                ths = soup.find("table").find_all("tr")[0].find_all("th")
                columns = [th.text for idx, th in enumerate(ths) if idx != 4]
            table = [[td.text for idx, td in enumerate(tr.find_all("td")) if idx != 4] for tr in tqdm(trs)]
            data += table

            print(table)
            time.sleep(2)
            page += 1



            # url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="
            # driver.get(url)
            # time.sleep(2)
            # if page == 1:
            #     ths = soup.find("table").find_all("tr")[0].find_all("th")
            #     columns = [th.text for idx, th in enumerate(ths) if idx != 4]
            # table = [[td.text for idx, td in enumerate(tr.find_all("td")) if idx != 4] for tr in tqdm(trs)]
            # data += table

            # page += 1
        # except Exception as e:
        #     print(e)
        except Exception as e:
            print(e)
            print("page:",page)
            break

    df = pd.DataFrame(data, columns=columns)
    print(df)

    # page = 1
    # url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="
    # driver = chrome_driver()
    # driver.get(url)
    # time.sleep(1) # 인간처럼 행동하지 않으면 차단당하기 때문?

