# 이미지 처리 - 속도개선, 이미지 검색의 시간을 줄여본다.
import pyautogui

# 화면 우측 하단에 있는 이미지일 경우에는 시간이 좀 걸리기도한다. 좌측 상단에서부터 찾아서 그런듯하다.

# 속도 개선
# 1. GrayScale : 그레이스케일로 검색하면 30% 정도 개선, 정확도가 조금 떨어질 수 있음
# eventlog = pyautogui.locateOnScreen("eventlog.png", grayscale=True)

# 2. 범위 지정 : region=(x, y, width, height)
# eventlog = pyautogui.locateOnScreen("eventlog.png", region=(1700, 700, 220, 380))

# 3. 정확도 조정 : 정확도를 약간 떨어뜨린다, 몇 퍼센트 이상이면 같은 이미지로 간주한다.
# opencv를 설치해야 한다. pip install opencv-python
eventlog = pyautogui.locateOnScreen("eventlog.png", confidence=0.5)     # condifence의 기본값은 99%

pyautogui.click(eventlog)