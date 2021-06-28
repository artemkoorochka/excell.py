import xlrd
import sys

# /home/bitrix/www/upload/koorochka/excel/
file = sys.argv[1]
# file = "test17.xls"
# file = "sort.xls"

workbook = xlrd.open_workbook(file)
worksheet = workbook.sheet_by_index(0)
json = ''

json += "["
for i in range(1,worksheet._dimnrows):
    if str(worksheet.cell(i,1).value) != '':
        json += "{"
        json += '"kod":"{}", "sort":"{}"'.format(worksheet.cell(i,0).value,  worksheet.cell(i,1).value)
        json += "}"
        if i < (worksheet._dimnrows - 1):
            json += ","
json += "]"
print(json)