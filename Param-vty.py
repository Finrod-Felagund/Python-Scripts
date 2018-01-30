import paramiko
import time

#script uses paramiko to ssh into network devices and apply configs#
#configuring vty lines to exclusively accept ssh connections#  

ip_address = "ip address"
username = "user name"
password = "password"

ssh_client = paramiko.SSHClient()    #use the paramiko clinet, not the server component#
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    
    #    ...
	#This is a multi-line comment.
	#paramiko rejects unknown ssh keys, 
	#so simply accept public key from the switch; 
	#THIS IS NOT recommended for production environments
	#  ...
	
ssh_client.connect(hostname=ip_address,username=username,password=password)
    #    ...
	#This is a multi-line comment.
	#connect tp the ip address specified, 
    #using the user name and password defined 
	#at the beginning of the script 	
	#    ...

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()    #send shell commands to the switch#

remote_connection.send("configure terminal\n")
remote_connection.send("line vty 0 15\n")
remote_connection.send("transport input ssh\n")
remote_connection.send("transport output ssh\n\n")
remote_connection.send("end\n")
remote_connection.send("wr\n")


remote_connection.send("end\n")    #exit the session# 

time.sleep(1)    #adds delay; sleeping for 1 sec before outputting the session# 
output = remote_connection.recv(65535)    #output information to the console# 
print output

ssh_client.close    #make sure the ssh client connection is closed# 