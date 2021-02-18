# 구글 무비를 백그라운드에서 돌리고 스크롤을 내린 후 스크린샷을 찍어서 파일로 저장
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")   # 백그라운드에서 이 크기의 크롬창이 띄워졌다고 가정한다.

browser = webdriver.Chrome("../chromedriver.exe", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

interval = 2  # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 화면 가장 아래로 스크롤 내리기 문서의 총 높이만큼 스크롤
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    cur_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == cur_height:
        break
    prev_height = cur_height

browser.get_screenshot_as_file("background_google_movie.png")
browser.quit()
