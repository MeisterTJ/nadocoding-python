import pyautogui

# 화면 캡쳐
img = pyautogui.screenshot()
img.save("screenshot.png")      # 파일로 저장

pixel = pyautogui.pixel(508,308)
print(pixel)    # 픽셀의 RGB 값을 찍어준다.
print(pyautogui.pixelMatchesColor(28, 18, (34,167,242)))    # 픽셀 위치의 색상이 매치되는지 확인