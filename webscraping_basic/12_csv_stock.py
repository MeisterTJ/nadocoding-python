# csv 네이버 금융
import csv
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="    # 네이버 시가 총액 페이지

filename = "시가총액1-200.csv"

# excel에서 깨지지 않기 위해 utf-8-sig로 인코딩한다.
f = open(filename, "w", encoding="utf-8-sig", newline="")    # 자동 개행을 막기 위해서 newline을 넣는다.
writer = csv.writer(f)

# split 함수로 탭으로 구분한 것들이 리스트로 들어간다.
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ...]
writer.writerow(title)

for page in range(1, 5):    # 1 ~ 4 페이지
    res = requests.get(url + str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:    # 각 종목
        cols = row.find_all("td")
        if len(cols) <= 1: # 의미 없는 데이터는 스킵한다.
            continue

        # strip 함수는 문자열의 맨앞, 맨뒤의 whitespace를 제거한다.
        data = [col.get_text().strip() for col in cols]
        print(data)
        writer.writerow(data)

