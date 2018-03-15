#!/usr/bin/env python

from netmiko import ConnectHandler

#In this script, will ssh to multiple devices using netmiko and create vlans via loop#

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


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]    #This variable contains all targeted devices#

for devices in all_devices:    #Run the loop in all devices contained in the variable#
    net_connect = ConnectHandler(**devices)    #connect to these devices[iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]#
    for n in range (8,10):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output