#!/usr/bin/env python

from netmiko import ConnectHandler

#This script ssh to multiple switches and configure two types of ports; access ports & Trunk ports# 
#The configuration commands are in another file that will be called in this script# 

iosv_l2_s1 = {    #configuration (device type, IP add., username and password) for switch1#
    'device_type': 'cisco_ios',
    'ip': 'IP Address',
    'username': 'username',
    'password': 'password',
}

iosv_l2_s2 = {    #configuration (device type, IP add., username and password) for switch 2#
    'device_type': 'cisco_ios',
    'ip': 'IP Address',
    'username': 'username',
    'password': 'password',
}

iosv_l2_s3 = {    #configuration (device type, IP add., username and password) for switch 3#
    'device_type': 'cisco_ios',
    'ip': 'IP Address',
    'username': 'username',
    'password': 'password',
}



with open('ios_configs') as f:    #using 'with' statement, open a file called ios_configs which contains configuration commands#
    lines = f.read().splitlines()    #each line in ios_configs will be read and spilt into a list#
print lines

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)    #connect to all devices defined in all_devices#
    output = net_connect.send_config_set(lines)    #devices are configured as spacified b the list created by 'with' statement#The list created by 'with' statement is called here#
    print output 