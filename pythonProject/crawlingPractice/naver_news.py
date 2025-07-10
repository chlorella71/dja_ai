import requests
from bs4 import BeautifulSoup

query = "삼성전자"
url = f"https://search.naver.com/search.naver?where=news&query={query}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

for idx, a_tag in enumerate(soup.select("a.news_tit"), 1):
    print(f"{idx}. {a_tag.text.strip()} — {a_tag['href']}")
