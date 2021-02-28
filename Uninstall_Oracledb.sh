#!/bin/bash
#############################################################################
#                    Prerequisite Install Oracle DataBase                   #
#                    COPYRIGHT (C) NOKIA, Egypt                             #
#                    Author: Ahmed Bebars, +201024614238                    #
#############################################################################
set -x

sudo -S su - oracle bash -c "cd /opt/nokia/dbadmin/scripts/ ; ./dbControl.sh stop"
sleep 200
sudo -S su - oracle bash -c "cd /opt/nokia/dbadmin/scripts/ ; ./dbStatus.sh >> /tmp/db_status"

dbstatus=$(cat /tmp/db_status)

if [ "$dbstatus" == "SHUTDOWN" ]

	then
	 systemctl -a | grep -i ora
	 systemctl stop oracle-ohasd.service
	 systemctl stop systemd-journal-flush.service
	 systemctl stop systemd-tmpfiles-clean.service
	 systemctl stop systemd-tmpfiles-clean.timer
	 systemctl disable oracle-ohasd.service
	 systemctl disable systemd-journal-flush.service
	 systemctl disable systemd-tmpfiles-clean.service
	 systemctl disable systemd-tmpfiles-clean.timer
 	 systemctl mask oracle-ohasd.service
	 systemctl mask systemd-journal-flush.service
	 systemctl mask systemd-tmpfiles-clean.service
	 systemctl mask systemd-tmpfiles-clean.timer
	 systemctl -a | grep -i ora
	for pid in `ps -ef | grep -i oracle | grep -v grep  | grep -v root| awk '{print $2}'`; do kill -9 $pid; done
	pkill -9 -u oracle
	rm -rf /u01/*
	rm -rf /u02/*
	rm -rf /u03/*
	rm -rf /u04/*
	rm -rf /u05/*
	rm -rf /home/oracle
	rm -rf /opt/nokia/dbadmin
	rm -rf /etc/oracle
	rm -rf /opt/ORCLfmap
	rm -f /etc/oratab
	rm -f /etc/oraInst.loc
	rm -rf /tmp/OraInstall*
	rm -rf /tmp/deinstall*
	rm -rf /tmp/install.dir.*
	rm -rf /var/tmp/.oracle
	rm -f /var/spool/mail/oracle
	rm -f /var/spool/cron/oracle
	rm -f /usr/local/bin/dbhome
	rm -f /usr/local/bin/oraenv
	rm -f /usr/local/bin/coraenv
	rm -rf /tmp/hsperfdata_oracle
	userdel oracle
	groupdel oracle
	groupdel oinstall
	groupdel osasm
	groupdel dba
	
	ipcrm -a
	find / -nouser
fi

