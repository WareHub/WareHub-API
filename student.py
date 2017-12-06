import datetime
from user import User



class Student(User):
    def __init__(self):
        User.__init__(self)
        return

    #INSERT INTO DEMAND TABLE FUNC.
    def insertDemand(self, stID, devID, startT, endT):

        #gets overlaps between new demand and accepted demands
        query = "SELECT* FROM DEMAND WHERE DEVICE_ID = {} AND RESERVED = 1 AND ((START_TIME < '{}' AND END_TIME > '{}') OR (START_TIME < '{}' AND END_TIME > '{}') \
                    OR (START_TIME > '{}' AND END_TIME < '{}'))".format(devID, startT, startT, endT, endT, startT, endT)
        table = self.db.executeQuery(query)

        #if no overlaps demand is inserted and accepted (reserved = 1)
        if len(table) == 0:
            query = "INSERT INTO DEMAND (STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED) VALUES ({}, {}, '{}', '{}', 1)".format(stID, devID, startT, endT)
            #print (query)
            self.db.executeNonquery(query)

        #if there's an overlap (only one) we check the time 
        elif len(table) == 1 and datetime.datetime.now() > table[0][2] and (not table[0][5]):
            
            query = "INSERT INTO DEMAND (STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED) VALUES ({}, {}, '{}', '{}', 1)".format(stID, devID, startT, endT)
            self.db.executeNonquery(query)
                                                            
        else:
            query = "INSERT INTO DEMAND (STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED) VALUES ({}, {}, '{}', '{}', 0)".format(stID, devID, startT, endT)
            #print (query)
            self.db.executeNonquery(query)
            return json.dumps(table) 
    
    

    def retrieveDemand_St(self, stID):
        query = 'SELECT* FROM DEMAND WHERE STUDENT_ID = {}'.format(stID)
        #print (query)
        data = self.db.executeQuery(query)
        return json.dumps(data) 

    #this function adds a review to the database
    def insertReview(self, sid, deviceid, opinion, rate):
        date = self.db.executeQuery('select GETDATE()')
        query = "insert into REVIEW (STUDENT_ID, DEVICE_ID, R_TIME, OPINION, RATE) values ({}, {}, {}, '{}', {})".format(sid, deviceid, date, opinion, rate)
        self.db.executeNonQuery(query)
		
	

     #REMOVE FROM DEMAND TABLE FUNC.
    def removeDemand(self, stID, devID, startT):
        query = "DELETE FROM DEMAND WHERE STUDENT_ID = {} AND DEVICE_ID = {} AND START_TIME = '{}'".format(stID, devID, startT)
        self.db.executeNonQuery(query)

    
    
