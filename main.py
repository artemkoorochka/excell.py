import xlrd

workbook = xlrd.open_workbook('test.xls')

worksheet = workbook.sheet_by_index(0)

print(worksheet.cell(1, 0).value)