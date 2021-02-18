from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # 키를 직접 입력하기 위해 필요

# 상위폴더에 chromedriver.exe가 존재한다.
browser = webdriver.Chrome("../chromedriver.exe")
browser.get("http://naver.com") # 네이버로 접속
elem = browser.find_element_by_class_name("link_login") # 로그인 버튼
elem.click()    # 로그인 버튼을 실제로 클릭한다.
browser.back()  # 뒤로 가기
browser.forward()
browser.refresh()   # 새로 고침
elem = browser.find_element_by_id("query")  # 네이버 검색 입력창
elem.send_keys("나도 코딩")  # 글자를 보낸다.
elem.send_keys(Keys.ENTER)  # 엔터 키를 입력
elem = browser.find_elements_by_tag_name("a")    # 태그에 맞는 엘리먼트들을 가져온다.
for e in elem:
    e.get_attribute("href")     # a href 를 가져온다.

# XPATH로 element를 찾기 
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()    # 찾은 elem을 클릭 
browser.close()     # 현재 열린 탭만 닫는다.
browser.quit()      # 브라우저 전체를 종료한다.