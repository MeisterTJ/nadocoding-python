import pyautogui

# fw = pyautogui.getActiveWindow()    # 현재 활성화된 창 (VSCode)
# print(fw.title)                     # 현재 활성화된 창의 타이틀 이름을 출력한다.
# print(fw.size)                      # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom)     # 창의 좌표 정보
# pyautogui.click(fw.left + 10, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)        # 모든 윈도우 가져오기

# 타이틀을 포함하는 윈도우들을 가져오기
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if not w.isActive:  # 현재 활성화가 되지 않았다면
    w.activate()    # 활성화 (맨 앞으로 가져오기)

if not w.isMaximized:   # 현재 최대화가 되지 않았다면
    w.maximize()        # 최대화

pyautogui.sleep(1)

w.restore()             # 최대화를 한 후에 원복을 한다.
w.close()               # 윈도우 닫기