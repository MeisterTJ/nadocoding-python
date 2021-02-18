import time
from selenium import webdriver

browser = webdriver.Chrome("../chromedriver.exe")

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("ruinarts")
browser.find_element_by_id("pw").send_keys("12345")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 바로 다음 동작을 수행하지 않고, 페이지 전환을 기다리기 위해 슬립을 한다.
time.sleep(1)

# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)  # 페이지에 있는 모든 소스를 그대로 출력한다.

# 7. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit()  # 브라우저 전체 종료