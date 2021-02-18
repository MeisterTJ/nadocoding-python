# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화
# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력 (참 잘했어요!)
# 3. 5초 대기 후 그림판 종료, 이때 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 한다.

import pyautogui
import sys
import pyperclip    # 한글 입력을 위해

pyautogui.hotkey("win", "r")    # 단축키 : win + r 입력
pyautogui.write("mspaint")      # 프로그램 명 입력
pyautogui.press("enter")        # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(1)
window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]  # 제목 없음 0번째 갖고온다.
if not window.isMaximized:  # 최대화
    pass
    # window.maximize()

pyautogui.sleep(0.5)

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text)
else:
    print("텍스트 버튼 찾기 실패")
    sys.exit()

# 흰 영역 클릭
# pyautogui.click(200, 300, duration=0.5)

# 이미지를 기준으로 상대 좌표로 이동해서 클릭
btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200, btn_brush.top + 300)

pyperclip.copy("참 잘했어요!")
pyautogui.hotkey("ctrl", "v")

# 2초 대기
pyautogui.sleep(2)

# 프로그램 종료
window.close()
pyautogui.sleep(1)

# N을 눌러서 저장 안함, 이미지 찾는 것보단 훨씬 정확하지
pyautogui.press("n")

