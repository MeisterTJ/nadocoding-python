# 가우스 전자
import requests
from bs4 import BeautifulSoup

# 가우스 전자 url
url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})

# 가우스 전자 제목들 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()    # td 아래의 a에 있는 텍스트
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : {0:>5.2f}".format(total_rates))
print("평균 점수 : {0:>5.2f}".format(total_rates / len(cartoons)))
