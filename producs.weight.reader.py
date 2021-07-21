import xlrd

file = "producs.weight.xls"

workbook = xlrd.open_workbook(file)
worksheet = workbook.sheet_by_index(0)

test = worksheet.cell(1,1)

print(test)