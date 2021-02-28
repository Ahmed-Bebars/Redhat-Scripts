#!/usr/bin/python
#############################################################################
#                    reformat partitioning                                  #
#                    COPYRIGHT (C) NOKIA, Egypt                             #
#                    Author: Ahmed Bebars                                   #
#                   for More info call: +201024614238                       #
#############################################################################
import paramiko
import sys
import difflib
import re
import datetime
import os
logDT = datetime.datetime.now().strftime('%Y-%m-%d')
log_file = open("/home/isdkuser/FTP_PUT/madgrf_1/logs/ftpserver_"+logDT+"_DIMTR.log", "a")
after_file = open("/home/isdkuser/FTP_PUT/madgrf_1/logs/after.txt", "w");
get_file = open("/home/isdkuser/FTP_PUT/madgrf_1/logs/get.txt", "w");
Host = '172.30.201.131';
user = 'rmtadm';
passwd = 'T3&123';
#start list processing
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
       ssh.connect(Host, username= user, password= passwd)
except paramiko.SSHException:
                  log_file.write (currentDT+"     "+"Connection Failed")
    		  quit()

stdin,stdout,stderr = ssh.exec_command("ls /opt/tpa/logs/metrics/csvfiles/*.csv")

for line in stdout.readlines():
        after_file.write (line.rstrip()+"\n")
after_file.close()
ssh.close()
#start compare files (Book Keeping)
text1 = open("/home/isdkuser/FTP_PUT/madgrf_1/logs/after.txt").readlines()
text2 = open("/home/isdkuser/FTP_PUT/madgrf_1/logs/before.txt").readlines()
for line in difflib.unified_diff(text1, text2):
        pattern = re.search("^-\/\w.*",line)
        if pattern:
                difffile=pattern.group(0).replace('-', '')
                
                get_file.write (difffile+"\n")
get_file.close()
#copy after file to before file
with open("/home/isdkuser/FTP_PUT/madgrf_1/logs/after.txt") as after:
    with open("/home/isdkuser/FTP_PUT/madgrf_1/logs/before.txt", "w") as before:
        for line in after:
            before.write(line)
    before.close()
after.close()
#start sftp process
ssh.connect('172.30.201.131', username='rmtadm', password='yt_xk39B')
sftp = ssh.open_sftp()
get_text = open("/home/isdkuser/FTP_PUT/madgrf_1/logs/get.txt").readlines()
for line in get_text:
        print(line.rstrip()+"nospace")
	filepath = line.rstrip()
	pattern2 = re.search("A[0-9].*",line.rstrip())
        if pattern2:
                getfile=pattern2.group(0)
        localpath = "/home/isdkuser/FTP_PUT/madgrf_1/testing/"+getfile
        currentDT = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write (currentDT+"     "+"source:"+filepath+","+"destination:"+localpath)
        sftp.get(filepath,localpath)
sftp.close()
ssh.close()
log_file.close()

