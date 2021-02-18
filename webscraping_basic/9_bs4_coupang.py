# 쿠팡
# GET : URL에 적어서 보낸다 (? 뒤에)
# POST : http body에 숨겨서 보낸다. 크기가 큰 데이터 등에 적합, 게시판 글 (id나 pwd는 숨겨야하지)

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="

# user-agent를 안쓰면 타임아웃이 걸린다.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# li tag 중에서 search-product로 시작하는 class 들을 다 가져온다.
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
for item in items:
    # 광고로 들어온 제품은 제외한다.
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다>")
        continue

    # 상품 명
    name = item.find("div", attrs={"class": "name"}).get_text()

    # Apple 사 노트북은 제외한다.
    if "Apple" in name:
        print(" <Apple 상품 제외합니다>")
        continue

    # 가격
    price = item.find("strong", attrs={"class": "price-value"}).get_text()

    rating = item.find("em", attrs={"class":"rating"})
    if rating:
        rating = rating.get_text()

    else:   # 평점이 없을 수 있다.
        rating = "평점 없음"
        print(" <평점 없는 상품 제외합니다>")
        continue

    # 평점 수
    rating_count = item.find("span", attrs={"class": "rating-total-count"})
    if rating_count:    # 평점 수가 없다.
        rating_count = rating_count.get_text()  # 출력 값이 (26) 이런 식
        rating_count = rating_count[1:-1]   # 괄호를 벗기는 방법
        # print("리뷰 수", rating_count)
    else:
        rating_count = "평점 수 없음"
        print(" <평점 수 없는 상품 제외합니다>")
        continue

    # 여기까지 왔다는 것은 평점과 평점 수가 존재하는 것
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    if float(rating) >= 4.5 and int(rating_count) >= 100:
        print(name, price, rating, rating_count)
