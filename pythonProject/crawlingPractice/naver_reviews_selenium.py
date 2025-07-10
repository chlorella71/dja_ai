from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 설정 ( 자동 설치 )
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # 브라우저 최대화
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 자동화 탐지 방지 스크립트 삽입
driver.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {
        'source':'''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        '''
    }
)

# 검색어 입력
query = "무선 이어폰"
url = f"https://search.shopping.naver.com/search/all?query={query}"
driver.get(url)

# 페이지 렌더링 대기
time.sleep(5)

# 테스트 출력
print(driver.title)
print(driver.current_url)

# 제품 제목 요소 추출
titles = driver.find_elements(By.CSS_SELECTOR, "a.product_link_TrAac")
for i, title in enumerate(titles[:10]):
    print(f"{i+1}. {title.text}")

# 종료
driver.quit()