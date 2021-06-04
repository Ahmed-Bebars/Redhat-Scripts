#!/usr/bin/python
#############################################################################
#                    check OS partition                                     #
#                    						                                #
#                    Author: Ahmed Bebars, +201024614238                    #
#############################################################################
import paramiko
import sys
import datetime
import os
import re
#define needed variable
result_file = open("/home/omc/bebars/result.txt", "w")
result_file.close()
currentDT = datetime.datetime.now().strftime('%Y-%m-%d')
result_file = open("/home/omc/bebars/result.txt", "a")
result_file.write (currentDT+"\n");
winpartition=["C","D"]
winSpacelimit=4  #write which min limit accepted (GB)
#ssh function
def func_connect(ip,hostname,user,password,OS):
	result_file.write (hostname+"\n")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
        	ssh.connect(ip, username=user, password=password)
	except paramiko.SSHException:
                result_file.write (currentDT+"  "+"Connection Failed")
		quit()
	if OS == "Linux":
		stdin,stdout,stderr = ssh.exec_command("df -h | grep global")

		for line in stdout.readlines():
				result_file.write (line.rstrip()+"\n")
	if OS == "Windows":
		for disk in range(len(winpartition)):
			partition=winpartition[disk]
			wincmd="Get-CimInstance -ClassName Win32_LogicalDisk | where-Object -FilterScript {$_.DeviceID -Eq \""+partition+":\"} | select-object -Property @{'Name' = 'FreeSpace (GB)' ;Expression= { [int]($_.FreeSpace / 1GB) }}"
			stdin,stdout,stderr = ssh.exec_command(wincmd)
			result=stdout.readlines()
			freespace=re.search('[+-]?([0-9]*[.])?[0-9]+',str(result))
			if int(freespace.group(0)) < winSpacelimit:
				result_file.write("disk "+partition+" current free size "+ str(freespace(0))+" server name "+hostname)
	ssh.close()
#call ssh function
func_connect("x.x.x.x","narvm5","root","pass123","Linux")
func_connect("x.x.x.x","nar2vm5","root","pass123","Linux")
func_connect("x.x.x.x","VDA","administrator","Guisin","Windows")
result_file.close()