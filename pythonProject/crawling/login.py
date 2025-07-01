from bs4 import BeautifulSoup

from driver import chrome_driver
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    driver= chrome_driver()
    url = "https://www.coffeebeankorea.com/member/login.asp#loginArea"
    driver.get(url)
    driver.maximize_window()  # 창 최대화

    username = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[1]/input''')
    password = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[2]/input''')

    username.send_keys("chlorella71")
    time.sleep(2)
    password.send_keys("wns1751")
    time.sleep(2)

    driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/a''').click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤 최하단으로 내리기
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)