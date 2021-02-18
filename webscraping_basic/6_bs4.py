import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# html 문서를 lxml 파서를 통해서 beautifulsoup 객체로 만든다.
soup = BeautifulSoup(res.text, "lxml")
print(soup.title)             # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text())  # 네이버 만화 > 요일별  웹툰 > 전체웹툰
print(soup.a)                 # soup이 가지고 있는 것들 중에 처음으로 발견되는 a
print(soup.a.attrs)           # a에 들어있는 attribute들을 나열한다.
print(soup.a["href"])         # a의 href 에 해당하는 값을 가져온다.

# 위는 우리가 스크래핑하려는 페이지를 잘 알고 있을때에 보통 쓰는 방식

# class 값이 Nbtn_upload 인 element 찾기
print(soup.find("a", attrs={"class":"Nbtn_upload"}))   # 조건에 해당하는 첫번째 엘리먼트를 찾아온다.
print(soup.find(attrs={"class":"Nbtn_upload"}))        # 위와 똑같이 가져온다.

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())   # rank1의 a href 안의 텍스트를 가져온다.
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# print(rank1.parent)     # 부모 및 부모가 포함한 모든 내용을 출력
rank2 = rank1.find_next_sibling("li")   # 조건에 해당하는 sibling을 찾는다.
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())


# 한 번에 모든 것을 가져오기
# print(rank1.find_next_siblings("li"))

# a tag 안에 text가 정확히 일치하는 것을 가져온다. 없으면 None
webtoon = soup.find("a", text="고수-2부 129화")
print(webtoon)
