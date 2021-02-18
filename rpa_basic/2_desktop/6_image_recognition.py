# 이미지 처리
import pyautogui

# file 메뉴를 찍은 스크린샷을 기반으로 스크린내에서 위치를 찾아서 클릭하도록 하는 프로그램

file_menu = pyautogui.locateOnScreen("file_menu.png")   # 이미지를 화면 내에서 찾아서 정보를 반환한다.
print(file_menu)    # Box(left=39, top=9, width=30, height=22)  <= 이미지와 동일한 부분이 어느위치이고, 어떤 크기인지 출력
# pyautogui.moveTo(file_menu)
pyautogui.click(file_menu)

# 이미지를 찾지 못하면 None, pyautogui는 해상도에 영향을 받는다.

# 이미지와 똑같은 부분이 2개 이상일 경우
# w3schools 의 체크박스 이미지이다.
for i in pyautogui.locateAllOnScreen("checkbox.png"):     # 이미지와 똑같은 모든 정보를 가져온다.
    print(i)
    pyautogui.click(i, duration=0.25)

