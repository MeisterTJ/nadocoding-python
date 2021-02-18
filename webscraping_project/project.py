# 비서 만들기
# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다.
# 2. 헤드라인 뉴스 3건을 가져온다.
# 3. IT 뉴스 3건을 가져온다.
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.

import requests
import re
from bs4 import BeautifulSoup


def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(index, title, link):
    print("{}. {}".format(index + 1, title))
    print("(링크 : {})".format(link))


# 날씨 정보
def scrape_weather():
    print("[오늘의 날씨]")
    soup = create_soup("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8")
    # 흐림, 어제보다 00도 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    # 현재, 최저, 최고 온도
    cur_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")  # 도씨 글자는 출력하지 않는다.
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()  # 최저 온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()  # 최고 온도

    # 오전, 오후 강수 확률
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip() # 오전 강수 확률
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()  # 오후 강수 확률

    # 미세먼지, 초미세먼지
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()    # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text()    # 초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(cur_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


# 네이버 뉴스 헤드라인
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)  # 3개만 가져온다.
    for idx, news in enumerate(news_list):
        title = news.div.a.get_text().strip()
        link = url + news.div.a["href"]
        print_news(idx, title, link)
    print()


# IT 뉴스 가져오기
def scrape_it_news():
    print("[IT 뉴스]")
    url ="https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)  # 3개만 가져온다.
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img: # 이미지가 있다면
            a_idx = 1   # img 태그가 있으면 1번째 img 태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(idx, title, link)
    print()


# 오늘의 영어회화 가져오기
def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")

    # # 반은 한글지문, 반은 영어지문, 영어지문부터 출력
    for sentence in sentences[len(sentences)//2:]:  # // 은 나눗셈을 int로 출력한다.
        print(sentence.get_text().strip())
    print("\n(한글 지문)")
    for sentence in sentences[0:len(sentences)//2]:  # // 은 나눗셈을 int로 출력한다.
        print(sentence.get_text().strip())
    print()


# 이 프로그램을 직접 실행할 때만 이 부분을 호출
if __name__ == "__main__":
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()