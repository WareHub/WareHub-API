import json 
import requests
import sys
import random
import datetime
import string

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
 
startT = datetime.datetime.now()
endT =datetime.datetime.now()+datetime.timedelta(hours=2)
for i in range (300):
    query = "insert into REVIEW (STUDENT_ID, DEVICE_ID, R_TIME, OPININON, RATE) values ({}, {}, convert(datetime2, '{}'), '{}', {})".format(random.choice(students_id), random.choice(device_id), startT, ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)), random.choice(range(6) ))
    startT+=datetime.timedelta(hours=2)
    endT+=datetime.timedelta(hours=2)
    print (query)
    
    #file.write(query) 
