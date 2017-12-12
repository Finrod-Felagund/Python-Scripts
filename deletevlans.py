#!/usr/bin/env python

import getpass
import sys
import telnetlib

#The script will call a file devicesips for ip address, and delete vlan.dat file#   
#After script executin, a reload from console line is a MUST#                                                     
#Same credentials on all switches#

user = raw_input("Username: ")  #enter username once for all targeted switches
password = getpass.getpass()    #enter password once for all targeted switches

f = open ("devicesips")    #open file named devicesips,default optin is read only#

for line in f:  #Ip address called from the file#
    print "Configuring Switch " + (line)
    HOST = line #Telnet to hosts in devicesips#
    tn = telnetlib.Telnet(HOST)    #tn is the variable for the telnet session#

    tn.read_until("Username: ") #Loop asks for a username#
    tn.write(user + "\n")       #Pass the user variable defined at start of the script#
    if password:
        tn.read_until("Password: ")
        tn.write(password +"\n")    #Pass the password variable defined at the startof the script#


    tn.write("delete vlan.dat\n")
    tn.write("\n")
    tn.write("\n")

    tn.write("wr\n")

    tn.write("reload\n")    #RELOAD ONLY ALLOWED FROM CONSOLE LINE!!#
    tn.write("\n")

    tn.write("exit\n")

    print tn.read_all()    #Read all data until EOF; block until connection closed.#
