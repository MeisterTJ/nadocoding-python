# 키보드 캡처 프로그램
import keyboard
import time
from PIL import ImageGrab


def screenshot():
    # 현재 시간을 가져온다. (_20200601_102030)
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(cur_time))    # image_20200601_102030.png


# 핫키를 누르면 함수 실행
# keyboard.add_hotkey("F9", screenshot)
# keyboard.add_hotkey("a", screenshot)
keyboard.add_hotkey("ctrl+shift+s", screenshot)

# 사용자가 esc 를 누를 때까지 프로그램 수행
keyboard.wait("esc")