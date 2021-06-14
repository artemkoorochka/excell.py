# https://stackoverflow.com/questions/2942889/reading-parsing-excel-xls-files-with-python/50815107

import xlrd

file = 'related_import.xls'
# /home/bitrix/www/upload/koorochka/excel/
workbook = xlrd.open_workbook(file)
sheet_names = workbook.sheet_names()
worksheet = workbook.sheet_by_index(0)

print(sheet_names)
print(len(sheet_names))

print("Товар")
print(worksheet.cell(0,0).value)
print(worksheet.cell(1,0).value)
print(worksheet.cell(2,0).value)
print(worksheet.cell(3,0).value)

print("сопутка")



print("Cicle")

for i in range(1,worksheet._dimnrows):
    print(worksheet.cell(i,1).value)


print("Count")

print(worksheet._dimnrows)


