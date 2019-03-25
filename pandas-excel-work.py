#! /usr/bin/python

import pandas as pd
import os
import string

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

# try the loop
for index, row in df1.iterrows():
     print("IP And Ports")
     print(row['ip'], row['ports'])
# assign the ips and ports to variables
     i = row['ip']
     ports = str(row['ports'])
     print(i)
     print(ports)
     if ports is None:
         continue
# make the ports into sub-list
     ports_list = ports.split(",")
     for port in ports_list:
# strip the spaces from the variable
         port = port.translate({ord(c): None for c in string.whitespace})
         print(port)
         print("nmap -Pn -p",' ',port,i)
# execute shell command
         os.system('nmap -Pn -p port i')
