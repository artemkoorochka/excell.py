import xlrd
# /home/bitrix/www/upload/koorochka/excel/
file = 'related_import.xls'

workbook = xlrd.open_workbook(file)
sheet_names = workbook.sheet_names()
worksheet = workbook.sheet_by_index(0)
current = 0
json = ''

json += "{"
for i in range(1,worksheet._dimnrows):
    if str(worksheet.cell(i,1).value) != '':
        if str(worksheet.cell(i,0).value) != '':
            current = worksheet.cell(i,0).value
        json += "'{}':'{}'".format(current, worksheet.cell(i,1).value)
        if i < (worksheet._dimnrows - 1):
            json += ","
json += "}"
print(json)