import requests

# res = requests.get("http://naver.com")
res = requests.get("http://www.google.com")
print("응답코드 : ", res.status_code)  # 200 이면 정상

# if res.status_code == requests.codes.ok:  # 200
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status()      # 문제가 생기면 오류를 내뱉고 프로그램을 끝낸다.
print("웹 스크래핑을 진행합니다")  # 정상일 경우

# 받아온 res의 text를 파일로 출력한다.
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
