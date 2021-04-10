import paramiko
import sys
import os.path
from os import path
#needed parameters
print ("this script developped for any OS windows,linux,MAC,Unix using ssh, for more info call me +201024614238 Ahmed Bebars")
resultfile= open("C:\\Users\\bebars\\Desktop\\D\\resultfile.txt", 'w')
ip_array = []
IPpath = input ("Enter your IP file path : ")
if os.path.isfile (IPpath):
	with open(IPpath) as f:
	  ip_array = f.readlines()
username = input("Enter username : ")
password = input("Enter password : ")
path = input("Enter your command file path : ")
#check file before start
if (os.path.isfile (path) and os.path.isfile (IPpath)) :
	for ip in range(len(ip_array)):
		HOST=ip_array[ip]
		port=22
		cmdfile = open (path,"r")
		listOfLines = cmdfile.readlines()
		cmdfile.close()
		for cmd in listOfLines:
				ssh=paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(HOST,port,username,password)
				stdin,stdout,stderr=ssh.exec_command(cmd)
				#env_dict={"LC_TELEPHONE":'hostname',"LC_MEASUREMENT":"MILES_APART"}
				#stdin , stdout, stderr = ssh.exec_command('$LC_TELEPHONE; echo "..."; echo $LC_MEASUREMENT',environment=env_dict)
				#print (stdout.read())
				outlines=stdout.readlines()
				resultfile.write(''.join(outlines))

else:
	print ("please check IP file and cmd file, may be you enter wrong path or you enter path only without file name")
#resultfile.write(''.join(outlines))
resultfile.close()
ssh.close()