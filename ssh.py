#!/usr/bin/python
#############################################################################
#                    check global partition                                 #
#                    COPYRIGHT (C) NOKIA, Egypt                             #
#                    Author: Ahmed Bebars, +201024614238                    #
#############################################################################
import paramiko
import sys
import datetime
import os
#define needed variable
result_file = open("/home/omc/bebars/result.txt", "w")
result_file.close()
currentDT = datetime.datetime.now().strftime('%Y-%m-%d')
result_file = open("/home/omc/bebars/result.txt", "a")
result_file.write (currentDT+"\n");
#ssh function
def func_connect(ip,hostname,user,password):
	result_file.write (hostname+"\n")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
        	ssh.connect(ip, username=user, password=password)
	except paramiko.SSHException:
                log_file.write (currentDT+"  "+"Connection Failed")
		quit()

	stdin,stdout,stderr = ssh.exec_command("df -h | grep global")

	for line in stdout.readlines():
        	result_file.write (line.rstrip()+"\n")
	ssh.close()
#call ssh function
func_connect("10.58.94.10","narvm5","root","Nokia!123")
func_connect("10.58.95.205","nar2vm5","root","Nokia_123")
result_file.close()
