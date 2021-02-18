import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]  # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")    # 12345를 입력
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")     # pyautogui는 한글 처리가 안된다. 아무것도 안나옴

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)   # 방향키, 문자, 엔터 입력

# 특수 문자
# shift 4 - > $
# pyautogui.keyDown("shift")      # shift 키를 누른 상태에서
# pyautogui.press("4")            # 숫자 4를 입력하고
# pyautogui.keyUp("shift")        # shift 키를 뗀다

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")         # 전체 선택

# 간편한 조합키
# ctrl 누르고 > alt 누르고 > shift 누르고 > a 누르고 > a 떼고 > shift 떼고 > alt 떼고 > ctrl 떼고
# pyautogui.hotkey("ctrl", "alt", "shift", "a")

pyautogui.hotkey("ctrl", "a")

import pyperclip

pyperclip.copy("나도코딩")  # "나도코딩" 글자를 클립보드에 저장, 이걸 붙여넣기 하면 된다.
pyautogui.hotkey("ctrl", "v")


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


# win : ctrl + alt + del    # 화면 전환하면서 자동화를 끝내는 방법
# mac : cmd + shift + option + q