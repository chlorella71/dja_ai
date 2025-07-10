from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

query = "삼성전자"
url = f"https://twitter.com/search?q={query}&src=typed_query&f=live"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
time.sleep(5)  # 로딩 대기 시간 증가

for _ in range(5):  # 스크롤 횟수 증가
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

tweets = []
for tweet in soup.find_all('div', attrs={'data-testid': 'tweet'}):
    content_tags = tweet.find_all('span')
    full_text = " ".join([span.get_text() for span in content_tags])
    if full_text:
        tweets.append(full_text)

# 결과 확인
print(f"[INFO] 수집된 원시 트윗 수: {len(tweets)}")

df = pd.DataFrame(tweets, columns=['content'])
df.to_csv("samsung_tweets_selenium.csv", index=False, encoding='utf-8-sig')
print(f"[INFO] 저장 완료: samsung_tweets_selenium.csv ({df.shape[0]}개)")
