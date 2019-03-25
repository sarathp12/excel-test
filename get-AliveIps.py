#! /usr/bin/python

# Import modules
import subprocess
import ipaddress

# make the list of subnets
az_ip_list = ['10.244.159.0/27', '10.244.159.32/27', '10.244.152.0/22', '10.244.208.0/24']

for item in az_ip_list:
    print item
    ip_net = ipaddress.ip_network(u'{}'.format(item))
# get all hosts on that network
    all_hosts = list(ip_net.hosts())
    print (all_hosts)
# Configure subprocess to hide the console window
#info = subprocess.STARTUPINFO()
#info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#info.wShowWindow = subprocess.SW_HIDE

# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface
    for i in range(len(all_hosts)):
           output = subprocess.Popen(['ping', '-n', '1', '500', str(all_hosts[i])], stdout=subprocess.PIPE)
    
           if "Destination host unreachable" in output.decode('utf-8', errors='ignore').lower():
                 print(str(all_hosts[i]), "is Offline")
           elif "Request timed out" in output.decode('utf-8'):
                 print(str(all_hosts[i]), "is Offline")
           else:
                 print(str(all_hosts[i]), "is Online")
