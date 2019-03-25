#! /usr/bin/python

import pandas as pd

excel_file = 'test-py.xlsx'
ip_data = pd.read_excel(excel_file)

# printing the first few lines
x = ip_data.head()
print(x)

