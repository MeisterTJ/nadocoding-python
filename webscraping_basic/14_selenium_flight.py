# 네이버 항공권
from selenium import webdriver

# 로딩 대기 구현을 위해 임포트하는 것들
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 대기용
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("../chromedriver.exe")
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)  # url로 이동

# 가는날 선택 글자로 찾는다.
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # 이번달에서 선택
browser.find_elements_by_link_text("28")[0].click()  # 이번달에서 선택

browser.find_element_by_class_name("btn_trip").click()

browser.find_elements_by_link_text("27")[0].click()  # 다음달에서 선택
browser.find_elements_by_link_text("28")[1].click()  # 다음달에서 선택

# 제주도 선택, xpath에 큰 따옴표 중복되는것을 작은 따옴표로 변경해서 처리한다.
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 첫번째 결과 출력 다만 로딩이 길어서 바로 가져오면 문제가 생긴다.
# 로딩이 끝날 때까지 기다려야 한다.
try:
    # 최대 10초를 기다리되 그전에 XPATH에 해당하는 엘리먼트가 감지되면 대기를 끝낸다. 시간이 지나면 에러가 난다.
    # By에는 ID, class, name, link_text 등도 사용이 가능하다.
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# elem.click()
