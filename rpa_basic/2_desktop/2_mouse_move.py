import pyautogui

# 마우스 이동 (절대 좌표)
pyautogui.moveTo(200, 100)      # 지정한 위치(가로 x, 세로 y) 로 마우스를 이동
pyautogui.moveTo(100, 200, duration=0.25)       # 0.25초 동안 이동

# 현재 좌표 찍기
print(pyautogui.position())

# 상대 좌표로 이동 : 현재 커서 위치로부터
pyautogui.move(500, 100, duration=0.5)
print(pyautogui.position())