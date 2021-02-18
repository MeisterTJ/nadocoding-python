import pyautogui

# 50, 20
# while True:
#     pyautogui.sleep(1)  # 대기
#     print(pyautogui.position())

pyautogui.sleep(1)
# pyautogui.click(50, 20, duration=1)     # 1초 동안 좌표로 이동한 후에 클릭한다.
# pyautogui.click()   # 아무 인자도 없으면 제자리에서 클릭한다.
# pyautogui.mouseDown()   # 누른 상태, 드래그에서 사용
# pyautogui.move(50, 100, duration=1)
# pyautogui.mouseUp()     # 뗀 상태

# pyautogui.doubleClick() # 더블 클릭
# pyautogui.click(clicks=500)   # clicks 만큼 클릭한다
# pyautogui.rightClick()
# pyautogui.middleClick()     # 휠 클릭
# pyautogui.drag(100, 0, duration=0.25)   # 드래그, 너무 빠른 동작으로 드래그 수행이 안될 경우 duration 값을 설정한다.
# pyautogui.dragTo(1200, 500, duration=0.25)  # 절대좌표로 드래그

pyautogui.scroll(300)   # 위 방향으로 300만큼 스크롤, 음수이면 아래 방향으로 스크롤