#!/bin/sh
#------------------------------------------------------------------------
#
#       COPYRIGHT (C) NOKIA, Egypt
#       Author: NOKIA Core Support
#       Date: 14-02-2021
#       Purpose: check OS Partition status
#
#
#------------------------------------------------------------------------
cat /dev/null >| /home/omc/bebars/partition-report.txt
To_Email="hesham.khalil@orange.com"

for node in narvm{3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,44,45,66,67,20,21,22,23}
 do
        vm=($(ssh -q $node df -h| grep [8-9][0-9]% | awk '{print $5","$6}'))
         if [ ${#vm[@]} -eq 0 ]
          then echo "partition size in normal state" >> /home/omc/bebars/partition-report.txt
         else
                for element in "${vm[@]}"
                do
                        echo "$node      $element" >> /home/omc/bebars/partition-report.txt
                done
         fi
 done

/home/omc/CustomizedScripts/sendEmail-v1.56/sendEmail -f ran_partition@orange.com -t $To_Email -u "Partition Size status"  -m "please find attached file" -a /home/omc/bebars/partition-report.txt

