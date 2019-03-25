#! /usr/bin/python

import pandas as pd

excel_file = 'test-py.xlsx'
ip_data = pd.read_excel(excel_file)

# printing the first few lines
x = ip_data.head()
print(x)

# print the excel sheets
ip_data_sheet1 = pd.read_excel(excel_file, sheetname=0, index_col=0)
y = ip_data_sheet1.head()
print(y)

# dynamically choose the columns
df = pd.read_excel('test-py.xlsx')
df1 = df[df.columns[5:7]].dropna()
df1.columns = ['ip','ports']
print(df1)
