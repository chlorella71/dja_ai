import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

query = "삼성전자"
url = f"https://news.google.com/search?q={query}&hl=ko&gl=KR&ceid=KR:ko"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = []

# 구글 뉴스의 기사 제목 클래스는 'Nyt84d' (2025년 기준)
for article in soup.select("a.DY5T1d"):
    title = article.text.strip()
    link = article["href"]
    if not link.startswith("http"):
        link = "https://news.google.com" + link[1:]
    articles.append({"title": title, "link": link})

df = pd.DataFrame(articles)
filename = f"google_news_{query}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
df.to_csv(filename, index=False, encoding='utf-8-sig')

print(f"[INFO] 크롤링 완료: {len(df)}개 뉴스 기사 저장 -> {filename}")
