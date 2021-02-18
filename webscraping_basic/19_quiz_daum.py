# 퀴즈 (다음 부동산)
import requests
from bs4 import BeautifulSoup

# 다음 송파 헬리오시티 url
url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
    # f.write(soup.prettify())

# tbl을 찾고, tbody를 찾고 그 아래의 모든 tr을 가져온다.
data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for idx, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(idx + 1))
    print("거래 : ", columns[0].get_text().strip())   # 스트립으로 불필요한 빈칸 제거
    print("면적 : ", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 : ", columns[2].get_text().strip(), "(만원)")
    print("동 : ", columns[3].get_text().strip())
    print("층 : ", columns[4].get_text().strip())