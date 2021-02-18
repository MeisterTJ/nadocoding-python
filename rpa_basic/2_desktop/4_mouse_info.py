import pyautogui
# pyautogui.mouseInfo()   # MouseInfo 툴을 띄운다.

# 마우스가 자동으로 움직일때 마우스를 구석탱이로 움직이면 FailSafeException이 뜨면서 프로그램을 종료시킬 수 있다.
# FAILSAFE를 false로 하면 이 옵션을 끄는 것이다. 추천하지는 않는다.
# pyautogui.FAILSAFE = False

pyautogui.PAUSE = 1     # 모든 동작에 1초씩 sleep 적용

for i in range(10):
    pyautogui.move(100, 100)