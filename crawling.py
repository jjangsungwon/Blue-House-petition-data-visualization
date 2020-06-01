from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

for i in range(1, 11):
    # driver.get("https://www1.president.go.kr/petitions/best?page=1")  # 국민 청원 1 페이지
    driver.get("https://www1.president.go.kr/petitions/best?page=" + str(i))  # 1 ~ 10 페이지
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    result_list = []  # 국민 청원 제목을 담기 위한 리스트

    # 국민 청원 제목 가져오기
    for i in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
        print(i.find("div", class_="bl_subject").text[3:].strip())
        result_list.append(i.find("div", class_="bl_subject").text[3:].strip())
    time.sleep(5)  # 너무 빠르게 읽어오면 중간에 못 읽어오는 게 생길 수 있다.
