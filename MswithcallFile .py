#!/usr/bin/env python

import getpass
import sys
import telnetlib

#The script will call a file devicesips for ip address, in this case I'm using the same username and password                                                                                on the switches, I'm only goona be prompted for that once#
#If however the cridintials were difirent on each switch, It's better to add the authentication prompt as part                                                                                of the loop#


user = raw_input("Username: ")  #enter username once for all targeted switches
password = getpass.getpass()    #enter password once for all targeted switches

f = open ("devicesips")    #open file named devicesips

for line in f:  #Ip address called from the file#
    print "Configuring Switch " + (line)
    HOST = line #Telnet to hosts in devicesips#
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ") #Loop asks for a username#
    tn.write(user + "\n")       #Pass the user variable defined at start of the script#
    if password:
        tn.read_until("Password: ")
        tn.write(password +"\n")        #Pass the password variable defined at the startof the script#

    tn.write("conf t\n")

    for n in range (2,21):      #Subloop (loop within a loop), for number of vlans interation#
        tn.write("Vlan " + str(n) + "\n")       #configure vlan#
        tn.write("name PYTHON_VLAN_ " + str(n) + "\n")  ##name the vlan#

    tn.write("end\n")
	#tn.write("wr\n)				
    tn.write("exit\n")

    print tn.read_all()