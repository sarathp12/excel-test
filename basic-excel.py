#! /usr/bin/python

import xlrd
import pandas as pd

workbook = xlrd.open_workbook("test-py.xlsx")
worksheet = workbook.sheet_by_index(0)

df = pd.read_excel('test-py.xlsx')
#print(df.sheet_names)
df1 = df[df.columns[5:7]].dropna()
df1.columns = ['ip','ports']
print("Head")
#print(df1.head(10))
for index, row in df1.iterrows():
        print("IP And PORTS")
        print(row['ip'], row['ports'])
        ports = str(row['ports'])
        if ports is None:
            continue
        ports_list = ports.split(",")
        for port in ports_list:
            print("nmap -Pn -p ",row['ip'],' ',port) 
        print("----------------------------------------")
#print("the value at row 8 and column 6 is : {0}".format(worksheet.cell(8,6).value))

# extract the whole column
# print the two columns line by line
#worksheet.cell_value(0, 0)
#for i in range(worksheet.nrows):
#    print(worksheet.cell_value(i, 5))
#    print(worksheet.cell_value(i, 6))

# assign the excel values to variables
#worksheet.cell_value(0, 0)
#for i in range(worksheet.nrows):
#    x = worksheet.cell_value(i, 5)
#    print(x)
#    y = worksheet.cell_value(i, 6)
#    print(y)
# convert float value to integer
#    z = list(map(y))
#    print(z)


