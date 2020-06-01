from openpyxl import load_workbook
from konlpy.tag import Kkma
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


read_workbook = load_workbook("./bluehouse.xlsx")
read_cell = read_workbook.active

# 엑셀 150줄까지 읽는다.
list_excel = []
for i in range(1, 151):
    list_excel.append(read_cell.cell(i, 1).value)

# 자연어 처리
kkma = Kkma()
list_temp = []

for row in list_excel:
    list_temp = list_temp + kkma.nouns(row)

# 한글자로 이루어진 것은 제거한다(정확하지 않은 단어일 확률이 높다)
result_list = []
for i in list_temp:
    if len(i) == 1:
        continue
    else:
        result_list.append(i)

#print(collections.Counter(result_list))
#print(collections.Counter(result_list).most_common(5))  # 상위 5개
result_list = dict(collections.Counter(result_list).most_common(20))  # 상위 20개

# 시각화
# 문자, 숫자 분리 (그래프를 그리기 위해서)
list_string = []
list_number = []
for s, n in result_list.items():
    list_string.append(s)
    list_number.append(n)

# 한글 깨짐 방지
plt.rcParams["font.family"] = 'Malgun Gothic'

label = list_string
index = np.arange(len(label))
plt.bar(index, list_number)
plt.title("my title")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.xticks(index, label)
plt.xticks(rotation=60)
plt.show()
