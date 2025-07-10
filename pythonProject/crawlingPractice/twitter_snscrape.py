import snscrape.modules.twitter as sntwitter
import pandas as pd
import ssl
import certifi
import urllib3
from datetime import datetime
import time

# ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# query = "삼성전자 since:2024-06-01 until:2024-07-01"
query = "삼성전자"
max_tweets = 10
tweets = []

print(f"[INFO] 수집시작: {datetime.now()}")
print(f"[INFO] 쿼리: {query}")

try:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break

        tweets.append({
            'date': tweet.date,
            'username': tweet.user.username,
            'content': tweet.content,
            'url': tweet.url
        })
        print(f"[+] {i+1}개 수집됨: {tweet.date} - {tweet.content[:40]}...")

        time.sleep(0.5)

        # if i % 100 ==0:
        #     print(f"[INFO] 수집 진행률: {i} / {max_tweets}")
except Exception as e:
    print("[ERROR] 크롤링 도중 오류 발생:", e)

print(f"[INFO] 수집 완료: {len(tweets)}개 트윗")

if len(tweets) == 0:
    print("트윗을 수집하지 못함. 쿼리를 단순하게 바꾸거나 VPN/환경 점검을 권장")
else:
    df = pd.DataFrame(tweets)
    df.drop_duplicates(subset='content', inplace=True) #중복제거
    df.to_csv("samsung_tweets.csv", index=False, encoding='utf-8-sig')
    print(f"[INFO] 저장 완료: samsung_tweets.csv ({df.shape[0]}개)")