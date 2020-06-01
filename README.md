# Blue-House-petition-data-visualization
### 청와대 국민청원 데이터 시각화

[청와대 국민 청원](https://www1.president.go.kr/petitions) 사이트의 데이터를 시각화함으로써 현재 주요 이슈들을 한 눈에 볼 수 있다.

<br>

## 구현 과정

1. Crawling 
   - 추천순 목록  1 ~ 10 페이지에 해당하는 청원의 제목 정보를 가져온다.
   - BeautifulSoup, selenium, webdriver 사용
2. 파일 쓰기
   - openpyxl를 이용하여 제목 정보를 엑셀(xlsx)에 저장한다.
3. 자연어 처리
   - KoNLPy를 이용하여 제목을 단어 단위로 분리한다.
4. 시각화
   - matplotlib와 Count를 활용하여 막대 그래프를 그린다.
   - Wordcloud를 활용하여 Wordcloud를 그린다.

<br>

|           구현 사항            | 구현 여부 |
| :----------------------------: | :-------: |
| 국민 청원 데이터 수집 (크롤링) |     O     |
|       데이터 엑셀에 저장       |     O     |
|      데이터 엑셀에서 읽기      |     O     |
|          자연어 처리           |     O     |
|         단어 숫자 세기         |     O     |
|       막대 그래프 그리기       |     O     |
|        Wordcloud 그리기        |     O     |

<br>

## 구현 결과

![](C:\Users\sw\Documents\Blue-House-petition-data-visualization\img\wordcloud-cloud(white).png)

<br>

![](C:\Users\sw\Documents\Blue-House-petition-data-visualization\img\wordcloud-default.png)

<br>



## 추후 계획

사실 현재는 크롤링을 구현한 것이 아니라 스크래핑을 구현한 상황이다.
따라서 github action을 통해 자동으로 크롤링을 하도록 하여 주기적으로 주요 이슈들을 파악할 수 있도록 할 예정이다.