#!/usr/bin/env python

from netmiko import ConnectHandler

#In this script, will ssh to the router using netmiko and configure a loopback interface for management purposes#

iosv = {
    'device_type': 'cisco_ios',    #specify device type, In this script, will be using cisco ios#
    'ip': 'IP',
    'username': 'username',
    'password': 'password',
     #'port' : port number,    #optional, defaults to 22#
     #'secret': 'secret',    #optional, defaults to ' ' (not used)#
     #'verbose': False,    #optional, defaults to False#
}


net_connect = ConnectHandler(**iosv)    #connect to the device and execute commands#
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output    #(net_connect.send_command) commands is used for show commands in ios#

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output