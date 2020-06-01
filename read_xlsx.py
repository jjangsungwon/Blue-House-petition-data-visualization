from openpyxl import load_workbook
from konlpy.tag import Kkma
import collections

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

print(collections.Counter(result_list))
print(collections.Counter(result_list).common(5))  # 상위 5개
