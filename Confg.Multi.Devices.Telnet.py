

import getpass
import sys
import telnetlib

HOST = "ip address"
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")     #NOT IF USER PRIVLEGE 15
tn.write(b"password\n")   #NOT IF USER PRIVLEGE 15

tn.write(b"conf t\n")
tn.write(b"no ip domain-lookup\n")
tn.write(b"end\n")
#tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))    #Read all data until EOF; block until connection closed.




HOST = "ip address"
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")      #NOT IF USER PRIVLEGE 15
tn.write(b"password\n")    #NOT IF USER PRIVLEGE 15


tn.write(b"conf t\n")
tn.write(b"no ip domain-lookup\n")
tn.write(b"end\n")
#tn.write(b"wr\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))    #Read all data until EOF; block until connection closed.




HOST = "ip address"
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")     #NOT IF USER PRIVLEGE 15#
tn.write(b"password\n")   #NOT IF USER PRIVLEGE 15#


tn.write(b"conf t\n")
tn.write(b"no ip domain-lookup\n")
tn.write(b"end\n")
#tn.write(b"wr\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))    #Read all data until EOF; block until connection closed.
