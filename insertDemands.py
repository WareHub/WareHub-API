import json 
import requests
import sys
import random
import datetime


datastudents = requests.get('http://warehub-api.azurewebsites.net/retrive_table/student')
datastudents = json.loads(datastudents.text)
students_id = []
for s in datastudents:
    students_id.append(s[0])

datatech = requests.get('http://warehub-api.azurewebsites.net/retrive_table/device')
datatech = json.loads(datatech.text)
device_id = []
for s in datatech:
    device_id.append(s[0])
#file = open(“testfile.txt”) 
 
startT = datetime.datetime.now()
endT =datetime.datetime.now()+datetime.timedelta(hours=2)
for i in range (1000):
    query = "INSERT INTO DEMAND VALUES ({}, {}, convert(datetime2, '{}'), convert(datetime2, '{}'), 1, 0)".format(random.choice(students_id), random.choice(device_id), startT, endT)
    startT+=datetime.timedelta(hours=2)
    endT+=datetime.timedelta(hours=2)
    print (query)
    
    #file.write(query) 
