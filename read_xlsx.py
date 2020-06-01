from openpyxl import load_workbook

read_workbook = load_workbook("./bluehouse.xlsx")
read_cell = read_workbook.active
result_list = []

# 엑셀 150줄까지 읽는다.
for i in range(1, 151):
    result_list.append(read_cell.cell(i, 1).value)

for i in result_list:
    print(i)