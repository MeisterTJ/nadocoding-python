import requests

url = "http://nadocoding.tistory.com"

# 웹페이지에서 웹스크래핑이라는걸 감지하여 잘못된 정보를 줄 수가 있다. 그래서 useragent를 헤더에 붙여서 접속할 필요가 있다.
# whatismybrowser.com에서 볼 수 있는 user-agent 값
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()      # 문제가 생기면 오류를 내뱉고 프로그램을 끝낸다.

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
