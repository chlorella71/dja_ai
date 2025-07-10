import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
print("라이브러리 문제 없음")

def crawl_naver_reviews(product_name, max_pages=3):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    base_url = "https://search.shopping.naver.com/search/all"
    reviews= []

    for page in range(1, max_pages + 1):
        params = {
            "query": product_name,
            "pagingIndex": page,
            "pagingSize": 40,
        }
        response = requests.get(base_url,
                                params=params,
                                headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        product_cards= soup.select("div.basicList_info_area__17Xyo")

        if not product_cards:
            print(f"{page}페이지에 상품 없음 또는 구조 변경됨")
            break

        for card in product_cards:
            title_tag = card.select_one("a.basicList_link__1MaTN")
            price_tag = card.select_one("span.price_num__2WUXn")
            shop_tag = card.select_one("a.basicList_mall__sbVax")
            reviews.append({
                "제목":title_tag.text.strip() if title_tag else "",
                "가격":price_tag.text.strip() if price_tag else "",
                "쇼핑몰":shop_tag.text.strip() if shop_tag else "",
                "링크": title_tag["href"] if title_tag else ""
            })
        print(f"{page}페이지 완료")
        time.sleep(1)
    return pd.DataFrame(reviews)

if __name__=="__main__":
    keyword = "무선 이어폰"
    df = crawl_naver_reviews(keyword, max_pages=3)
    filename=f"{keyword.replace(' ', '_')}_naver_reviews.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"크롤링 완료: {filename} 저장됨")