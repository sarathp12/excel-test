#! /usr/bin/python

import xlrd

workbook = xlrd.open_workbook("test-py.xlsx")
worksheet = workbook.sheet_by_index(0)

print("the value at row 8 and column 6 is : {0}".format(worksheet.cell(8,6).value))

# extract the whole column

worksheet.cell_value(0, 0)
for i in range(worksheet.nrows):
    print(worksheet.cell_value(i, 6))
