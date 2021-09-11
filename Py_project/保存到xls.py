from requests import models
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')

for i in range(0, 9) :
    for j in range(0, i + 1) :
        worksheet.write(i, j, '%d * %d = %d'%(i + 1, j + 1, (i + 1) * (j + 1)))

workbook.save("99表.xls")