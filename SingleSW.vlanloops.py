#!/usr/bin/env python

import getpass
import sys
import telnetlib

HOST = "IP_Address"
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user.encode('ascii') + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password.encode('ascii') + "\n")



tn.write("conf t\n")
        #watch your spacing
for n in range (3,11):          #number of vlans interation#
        tn.write("vlan " + str(n) + "\n")               #make n type Int., cause can't mix object types (vlan;Str , n; Int.), therefore you put Str. before n
        tn.write(b"name Python_Vlan_" + str(n) + "\n")	#name each vlan ceated as; Python_Vlan(n)#

tn.write("end\n")
#tn.write("wr\n)
tn.write("exit\n")
#no write all for testing

print tn.read_all()    #Read all data until EOF; block until connection closed.#
