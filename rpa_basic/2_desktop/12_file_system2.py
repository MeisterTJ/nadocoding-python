import os

# 파일 목록 가져오기
print(os.listdir())         # 현재 폴더의 파일, 폴더 목록 가져오기
print(os.listdir(".."))     # 상위 폴더의 모든 폴더, 파일 목록 가져오기

# 파일 목록 가쟈오기 (하위 폴더 모두 포함)
result = os.walk("..")      # 주어진 폴더 밑에 있는 모든 목록
print(type(result))     # class generator

# generator는 root, 폴더, 파일들로 나뉜다.
for root, dirs, files in result:
    print("root:" , root, "\ndirs:" , dirs, "\nfiles:" , files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
name = "11_file_system.py"
result = list()
for root, dirs, files in os.walk("."):  # 현재 폴더(상대경로)
    if name in files:
        result.append(os.path.join(root, name))

print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
import fnmatch
pattern = "6*.py"    # 6으로 시작하고, .py 로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):      # 이름이 패턴과 일치하면
            result.append(os.path.join(root, name))

# .py로 끝나는 모든 파일의 상대경로를 리스트로 출력
print(result)
