# 다음 무비 년도별 관객 최상위 영화 가져오기
import requests
from bs4 import BeautifulSoup

# user-agent를 안쓰면 타임아웃이 걸린다.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

for year in range(2015, 2020):  # 2015~2019년 까지
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})
    for idx, image in enumerate(images):
        # print(image["src"])   # url에 https가 붙은 것도 있고 아닌 것도 있다.
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url, headers=headers)
        image_res.raise_for_status()

        # 바이너리 쓰기로 연다
        with open("movie_{}_{}.jpg".format(year, idx + 1), "wb") as f:
            f.write(image_res.content)  # 리소스가 가지고 있는 content 정보를 쓴다.

        if idx >= 4:    # 상위 5개 이미지까지만 다운로드 받는다.
            break