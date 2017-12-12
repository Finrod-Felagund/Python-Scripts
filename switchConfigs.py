#!/usr/bin/env python

import getpass
import telnetlib

#The script will pull the configurations of switches and save them to a file#

user = raw_input("Username: ")  #enter username once for all targeted switches
password = getpass.getpass()    #enter password once for all targeted switches

f = open ("devicesips")    #open file named devicesips,default option is read only#

for line in f:    #Ip address called from the file#
    print "Getting running-config for " + (line)
    HOST = line    #Telnet to hosts in devicesips#
    tn = telnetlib.Telnet(HOST)    #tn is the variable for the telnet session#

    tn.read_until("Username: ") #Loop asks for a username#
    tn.write(user + "\n")       #Pass the user variable defined at start of the script#
    if password:
        tn.read_until("Password: ")
        tn.write(password +"\n")    #Pass the password variable defined at the startof the script#

    tn.write("terminal length 0\n")    #This command will show all output in one go, instaed of hitting space for each page of configs#
    tn.write("show run\n")
    tn.write("exit\n")

    readoutput = tn.read_all()    #This variable reads all output from telnet sessin(tn variable)#
	
#next script opens file(Switch+IP) and saves the running-configs to it#
    saveoutput = open("Switch " + HOST, "w")    #here I need the variable to read/write, hence w#
    saveoutput.write(readoutput)
    saveoutput.write("\n")
    saveoutput.close