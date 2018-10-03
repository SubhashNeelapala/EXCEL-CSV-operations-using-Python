
#Reading data from excel file and writing it to csv file

import xlrd
import csv
def csv_from_excel():

    wb = xlrd.open_workbook('test.xls')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('data.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in xrange(sh.nrows):
        # print rownum
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
csv_from_excel()