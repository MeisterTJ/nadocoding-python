# 파일 시스템
# 파일 기본
import os
# print(os.getcwd())      # current working directory
# os.chdir("..")          # 부모 폴더로 이동
# os.chdir("..")          # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("rpa_basic")   # rpa_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..")          # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..")       # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/")         # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# open("파일경로") as f:
file_path = os.path.join(os.getcwd(), "my_file.txt")    # 절대 경로 생성
print(file_path)

# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r"C:\Users\chogd\PycharmProjects\nadocoding\rpa_basic\2_desktop\my_file.txt"))    # 여기서 my_file.txt는 제외된다.

# 파일 정보 가져오기
import time
import datetime

filepath = "checkbox.png"
# 파일의 생성 날짜
ctime = os.path.getctime(filepath)
print(ctime)                                                                # 1611233554.245961 과 같은 알 수 없는 숫자
print(datetime.datetime.fromtimestamp(ctime))                               # 2021-01-21 21:52:34.245961
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))   # 20210121 21:52:34

# 파일의 수정 날짜
mtime = os.path.getmtime(filepath)
print(datetime.datetime.fromtimestamp(mtime))

# 파일의 마지막 접근 날짜
atime = os.path.getatime(filepath)
print(datetime.datetime.fromtimestamp(atime))

# 파일 크기
size = os.path.getsize(filepath)
print(size, "bytes")    # 바이트 단위로 파일 크기 가져오기
