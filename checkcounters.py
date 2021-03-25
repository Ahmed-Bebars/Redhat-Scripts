#----------------------------------------------------------------------------------------------------#
#                                           NOKIA Script,25/3/2021                                   #
#                                    Author: Ahmed Bebars, +201024614238                             #
#              use to parse LTE performance file and detect which measurements active 15 interval    #
#----------------------------------------------------------------------------------------------------#
import xml.etree.ElementTree as ET
import re
import json
import glob
result_file=open("C:\\Users\\bebars\OneDrive - Nokia\\Operations & Care\\Orange\\RAN\\Counter count code\\result_15min.txt",'w')
result_file.close()
result_file=open("C:\\Users\\bebars\OneDrive - Nokia\\Operations & Care\\Orange\\RAN\\Counter count code\\result_15min.txt",'a')
arr = glob.glob("C:\\Users\\bebars\OneDrive - Nokia\\Operations & Care\\Orange\\RAN\\Counter count code\\*.xml")
for file in arr:
    #print(i)
    result_file.write(file+"\n")
    tree = ET.parse(file)
    root = tree.getroot()
    count = 0
    for form in root.findall("./PMSetup/PMMOResult/MO/DN"):
        match = re.match("PLMN-PLMN\/MRBTS-[0-9]*\/LNBTS-[0-9]*$",form.text)
        if match and count == 0:
            count+=1
            #print(form.text)
            result_file.write(form.text+"\n")
    for child in root.iter():
        #print(child.tag, child.attrib)
        if len(child.attrib) == 2:
            #print (child.attrib)
            json_str = json.dumps(child.attrib)
            resp = json.loads(json_str)
            interval =resp['interval']
        if len(child.attrib) == 1 :
            #print (child.attrib)
            json_str = json.dumps(child.attrib)
            resp = json.loads(json_str)
            if interval == "15":
                #print("interval:"+interval+","+"Measurement:"+resp['measurementType'])
                result_file.write("interval:"+interval+","+"Measurement:"+resp['measurementType']+"\n")


