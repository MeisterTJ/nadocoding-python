# UserAgent 정보 넣기
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")   # 백그라운드에서 이 크기의 크롬창이 띄워졌다고 가정한다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome("../chromedriver.exe", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

