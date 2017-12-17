import datetime
from user import User
import json



class Student(User):
    def __init__(self):
        User.__init__(self)
        return

    #INSERT INTO DEMAND TABLE FUNC.
    def insertDemand(self, stID, devID, startT, endT):

        #gets overlaps between new demand and accepted demands
        query = "SELECT* FROM DEMAND WHERE DEVICE_ID = {} AND RESERVED = 1 AND ((START_TIME <= convert(datetime2, '{}') AND END_TIME >= convert(datetime2, '{}')) OR (START_TIME <= convert(datetime2, '{}') AND END_TIME >= convert(datetime2, '{}')) \
                    OR (START_TIME >= convert(datetime2, '{}') AND END_TIME <= convert(datetime2, '{}')) OR  (START_TIME <= convert(datetime2, '{}') AND END_TIME >= convert(datetime2, '{}')))".format(devID, startT, startT, endT, endT, startT, endT, startT, endT)
        table = self.db.executeQuery(query)
        for i in range(len(table)):
            table[i] = list(table[i])
            table[i][2] = str(table[i][2])
            table[i][3] = str(table[i][3])

        #if no overlaps demand is inserted and accepted (reserved = 1)
        if len(table) == 0:
            query = "INSERT INTO DEMAND VALUES ({}, {}, convert(datetime2, '{}'), convert(datetime2, '{}'), 1, 0)".format(stID, devID, startT, endT)
            #print (query)
            try:
                self.db.executeNonQuery(query)
            return json.dumps(1)

        #if there's an overlap (only one) we check the time 
        elif len(table) == 1 and datetime.datetime.now() > table[0][2] and (not table[0][5]):
            query = "INSERT INTO DEMAND VALUES ({}, {}, convert(datetime2, '{}'), convert(datetime2, '{}'), 1, 0)".format(stID, devID, startT, endT)
            try:
                self.db.executeNonQuery(query)
            return json.dumps(1)
                                                            
        else:
            query = "INSERT INTO DEMAND VALUES ({}, {}, convert(datetime2, '{}'), convert(datetime2, '{}'), 0, 0)".format(stID, devID, startT, endT)
            #print (query)
            try:
                self.db.executeNonQuery(query)
            #return json.dumps(table)
            return json.dumps(0)
    
    

    def retrieveDemand_St(self, stID):
        query = 'SELECT* FROM DEMAND WHERE STUDENT_ID = {}'.format(stID)
        #print (query)
        data = self.db.executeQuery(query)
        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][2] = str(data[i][2])
            data[i][3] = str(data[i][3])
        return json.dumps(data) 

    #this function adds a review to the database
    def insertReview(self, sid, deviceid, opinion, rate, date):
        query = "insert into REVIEW (STUDENT_ID, DEVICE_ID, R_TIME, OPINION, RATE) values ({}, {}, convert(datetime2, '{}'), '{}', {})".format(sid, deviceid, date, opinion, rate)
        self.db.executeNonQuery(query)
		
	

     #REMOVE FROM DEMAND TABLE FUNC.
    def removeDemand(self, stID, devID, startT):
        query = "DELETE FROM DEMAND WHERE STUDENT_ID = {} AND DEVICE_ID = {} AND START_TIME = CONVERT(datetime2, '{}')".format(stID, devID, startT)
        self.db.executeNonQuery(query)
        #return query