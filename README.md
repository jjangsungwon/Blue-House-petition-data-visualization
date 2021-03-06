# Blue-House-petition-data-visualization
### 청와대 국민청원 데이터 시각화

[청와대 국민 청원](https://www1.president.go.kr/petitions) 사이트의 데이터를 시각화함으로써 현재 주요 이슈들을 한눈에 볼 수 있다.

<br>

## 구현 과정

1. Crawling 
   - 추천순 목록  1 ~ 10 페이지에 해당하는 청원의 제목 정보를 가져온다.
   - BeautifulSoup, selenium, webdriver 사용
2. 파일 쓰기, 읽기
   - openpyxl를 이용하여 제목 정보를 엑셀(xlsx)에 저장하고 읽는다.
3. 자연어 처리
   - KoNLPy를 이용하여 제목을 단어 단위로 분리한다.
4. 시각화
   - matplotlib와 Counter를 활용하여 막대그래프를 그린다.
   - Wordcloud를 활용하여 Wordcloud를 그린다.

<br>

|           구현 사항            | 구현 여부 |
| :----------------------------: | :-------: |
| 국민 청원 데이터 수집 |     O     |
|       데이터 엑셀에 저장       |     O     |
|      데이터 엑셀에서 읽기      |     O     |
|          자연어 처리           |     O     |
|         단어 숫자 세기         |     O     |
|       막대그래프 그리기       |     O     |
|        Wordcloud 그리기        |     O     |

<br>

## 구현 결과
![result](https://github.com/jjangsungwon/Blue-House-petition-data-visualization/blob/master/img/result.png?raw=true)
