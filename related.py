import xlrd
import sys

# /home/bitrix/www/upload/koorochka/excel/
file = sys.argv[1]
# file = "related_sample.xls"
# file = "related_sample_4.xls"

start = 1
product = 0
related = 2
sort = 4
count = 0

workbook = xlrd.open_workbook(file)
worksheet = workbook.sheet_by_index(0)
json = ''

json += "["

for i in range(0, len(worksheet.col_values(product, start))):
    if worksheet.col_values(product,start)[i] != '':
        if i > count:
            json += ","
        json += "{"
        json += '"product":"{}", "related":"{}", "sort":"{}"'.format(worksheet.col_values(product,start)[i],
                                                                     worksheet.col_values(related,start)[i],
                                                                     worksheet.col_values(sort,start)[i])
        json += "}"
        count = count + 1

json += "]"
print(json)