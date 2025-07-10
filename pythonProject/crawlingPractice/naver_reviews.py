import requests
import time
import random

# 실제 브라우저처럼 자연스러운 헤더
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.naver.com/",
    "DNT": "1"  # Do Not Track
}

#url 인코딩( 공백 -> %20 등)
query = "무선 이어폰"
query_encoded = requests.utils.quote(query)
url = f"https://search.shopping.naver.com/search/all?query={query_encoded}"

# 요청전에 딜레이(사람처럼)
time.sleep(random.uniform(3,6)) #3~6초 랜덤 딜레이

response = requests.get(url, headers=headers)

with open("sample.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("sample.html 저장완료")