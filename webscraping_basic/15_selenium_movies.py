import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language":"ko-KR,ko"    # 한글 페이지를 받아올 수 있다.
}
url = "https://play.google.com/store/movies/top"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify())    # html 문서를 예쁘게 출력

# 영화 제목들 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)