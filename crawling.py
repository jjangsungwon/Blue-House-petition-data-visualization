from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www1.president.go.kr/petitions/best?page=1")  # 국민 청원 사이트
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 국민 청원 제목을 담기 위한 리스트
result_list = []

# 국민 청원 제목 가져오기
for i in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
    print(i.find("div", class_="bl_subject").text[3:].strip())
    result_list.append(i.find("div", class_="bl_subject").text[3:].strip())