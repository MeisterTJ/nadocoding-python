# 구글 무비 스크롤에 따른 영화 순위 정보 가져오기
from selenium import webdriver
import time

browser = webdriver.Chrome("../chromedriver.exe")

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기 스크립트를 실행한다.
# browser.execute_script("window.scrollTo(0, 1080)")  # 1920 x 1080

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

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

# 셀레니움 브라우저 객체의 페이지 소스를 BeautifulSoup으로 읽을 수 있다.
soup = BeautifulSoup(browser.page_source, "lxml")

# 스크롤 되기 전 영화들과, 스크롤 된 후 영화들의 태그가 살짝 다르다.
# div 클래스 이름에 두 가지 조건을 리스트로 달았다. 두 이름 중에 하나만 매칭되면 된다.
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})

# 위의 코드에서는 "ImZGtf mpg5gc"안에 "Vpfmgd"가 있을 경우 같은 것을 두번 가져오는 문제가 있어서 조건을 축소
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))

# 영화 제목들 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " <할인되지 않은 영화 제외>")
        continue

    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 영화 정보 링크
    link = "https://play.google.com" + movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"링크 : ", link)
    print("-" * 80)

browser.quit()
