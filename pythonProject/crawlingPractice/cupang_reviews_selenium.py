from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

def chrome_driver():
    userAgent = generate_user_agent()
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    chrome_options.page_load_strategy = 'normal'
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument(f'user-agent={userAgent}')  # ✅ 수정된 부분
    chrome_options.add_argument('--lang=ko_KR')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-browser-side-navigation')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_options.add_argument("--headless=new")  # GUI 없이 실행 시


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    stealth(driver,
            languages=["ko-KR", "ko"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source":"""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    driver.implicitly_wait(5)
    return driver

if __name__ == "__main__":
    driver = chrome_driver()

    keyword="무선 이어폰"
    encoded_keyword= keyword.replace(" ", "+")
    url = f"https://www.coupang.com/np/search?q={encoded_keyword}"

    driver.get(url)
    time.sleep(5) # 페이지 로딩 대기
    print(driver.title)

    if "Access denied" in driver.title or "Coupang" not in driver.title:
        print("Cloudflare 또는 쿠팡 차단 탐지됨")
        driver.quit()
        exit()

    items = driver.find_elements(By.CSS_SELECTOR, "li.search-product")

    data = []
    for i, item in enumerate(items[:10]): # 상위 10개만 추출
        try:
            name = item.find_element(By.CSS_SELECTOR, "div_name").text
            price = item.find_element(By.CSS_SELECTOR, "strong.price-value").text
            link = item.find_element(By.CSS_SELECTOR, "a.search-product-link").get_attribute("href")
            full_link = "https://www.coupang.com"+link
            print(f"{i+1}. {name} | {price}원 | {full_link}")
            data.append({
                "상품명": name,
                "가격": price,
                "링크": full_link
            })
        except:
            continue

    driver.quit()

    df = pd.DataFrame(data)
    df.to_csv("쿠팡_무선이어폰_상품목록.csv", index=False, encoding="utf-8-sig")
    print("크롤링 완료, CSV 저장됨: 쿠팡_무선이어폰_상품목록.csv")