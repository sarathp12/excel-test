#! /usr/bin/python

from netaddr import IPNetwork
import ipaddress

# make the list of subnets
az_ip_list = ['10.244.159.0/27', '10.244.159.32/27', '10.244.152.0/22', '10.244.208.0/24']

#for item in az_ip_list:
#	print(item)
#	for ip in IPNetwork(u'item'):
#		print('%s' % ip)


# new code to generate ips from subnet
for item in az_ip_list:
        print(item)
        ip_net = ipaddress.ip_network(u'{}'.format(item))
	for ip in ip_net:
		print(ip)
#       net4 = ipaddress.ip_network(u'item')
#	for x in net4.hosts():
#     		print(x)
 	  
