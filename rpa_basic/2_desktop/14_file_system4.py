# 파일 시스템4
import os
import shutil

# 파일 복사하기
# shutil.copy("checkbox.png", "test_folder")  # 원본 경로, 대상 경로
# shutil.copy("checkbox.png", "test_folder/copy_checkbox.png")    # 원본 경로, 대상 경로(파일 이름 명시)

# copyfile은 항상 파일명만 쓸 수 있다.
shutil.copyfile("checkbox.png", "test_folder/copy_checkbox2.png")

# copy, copyfile : 메타정보 복사 x, 아예 새로운 파일
# copy2 : 메타정보 복사 O, 파일이 갖고 있는 정보(생성날짜, 수정된 날짜 등)을 그대로 복사
shutil.copy2("checkbox.png", "test_folder")
shutil.copy2("checkbox.png", "test_folder/copy_checkbox2.png")


# 폴더 복사
# shutil.copytree("test_folder", "test_folder2")      # 원본 폴더 경로, 대상 폴더 경로

# 폴더 이동
# 폴더가 없으면 폴더명이 변경되는 효과
shutil.move("test_folder", "test_folder2")  # 왼쪽 폴더를, 오른쪽 폴더로 이동
