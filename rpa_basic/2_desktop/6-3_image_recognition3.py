# 이미지 처리 - 대기
import pyautogui

# 자동화 대상이 바로 보여지지 않는 경우, 대상이 뜰 때까지 대기한다.
# 일정 시간동안 기다리기 (Timeout)
import time
import sys

def find_target(img_file, timeout=30):
    start = time.time()  # 시작 시간 설정
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:  # 10초 동안 못 찾으면 프로그램을 종료할 것이다.
            break
    return target       # 타겟을 돌려준다.


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()


my_click("checkbox.png", 3)