#! /usr/bin/python

import pandas as pd
import os
import sys
import subprocess
import shlex
import nmap

# get excel name dynamically
excel_file = sys.argv[1]
# excel_file = 'test-py.xlsx'
print(excel_file)
ip_data = pd.read_excel(excel_file)

# printing the first few lines
x = ip_data.head()
print(x)
# make the list of subnets
az_ip_list = ['10.244.159.0/27', '10.244.159.32/27', '10.244.152.0/22', '10.244.208.0/24']

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
         nm = nmap.PortScanner()
         nm_results = nm.scan(hosts=i,ports=port,arguments='-Pn')
         print(nm.command_line())
         for proto in nm[i].all_protocols():
             lport = nm[i][proto].keys()
             for port in lport:
                 print ('port : {}\tstate : {}'.format(port, nm[i][proto][port]['state']))
         
