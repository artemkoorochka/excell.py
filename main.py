import xlrd

workbook = xlrd.open_workbook('test.xls')
sheet_names = workbook.sheet_names()

print(sheet_names)
print(len(sheet_names))