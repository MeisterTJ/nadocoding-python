import os

# 주어진 경로가 파일인지 폴더인지 확인
print(os.path.isdir(".."))              # True
print(os.path.isfile("7_window.py"))    # True

print(os.path.isdir("checkbox.png"))
print(os.path.isfile("checkbox.png"))

# 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면?
print(os.path.isfile("run_btnnnn.png")) # False

# 주어진 경로가 존재하는지? (파일, 폴더 둘 다 확인 가능)
if os.path.exists("checkbox.png"):
    print("파일 또는 폴더가 존재합니다.")
else:
    print("존재하지 않습니다.")


# 파일 만들기
# open("new_file.txt", "a").close()   # 빈 파일을 생성한다.

# 파일명 변경하기
# os.rename("new_file.txt", "hello_world.txt")

# 파일 삭제하기
# os.remove("hello_world.txt")

# 폴더 만들기
# os.mkdir("new_folder")  # 현재 경로 기준으로 폴더 생성
# os.mkdir("c:/users/chogd/test")     # 절대 경로 기준으로 폴더 생성

# os.makedirs("new_folders/a/b/c")       # 하위 폴더를 가지는 폴더 생성

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder_rename")   # 폴더 안이 비었을때만 삭제 가능

import shutil   # shell utilities
# 폴더 안이 비어 있지 않아도 완전 삭제 가능, 모든 파일이 삭제될 수 있으므로 주의!!
# shutil.rmtree("new_folders")