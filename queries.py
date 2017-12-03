from dbmanager import DBManager
import datetime
class Demand_Basics(object):
    def __init__(self):
        self.db=DBManager()
        return

    #INSERT INTO DEMAND TABLE FUNC.
    def insertDemand(self, stID, devID, startT, endT):

        #gets overlaps between new demand and accepted demands
        query = 'SELECT* FROM DEMAND WHERE DEVICE_ID = {} AND (START_TIME < {} AND END_TIME > {}) OR (START_TIME < {} AND END_TIME > {}) \
                    OR (START_TIME > {} AND END_TIME < {}) AND RESERVED = 1'.format(devID, startT, startT, endT, endT, startT, endT)
        table = db.executeQuery(query)

        #if no overlaps demand is inserted and accepted (reserved = 1)
        if len(table) == 0:
            query = 'INSERT INTO DEMAND (STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED) VALUES ({}, {}, {}, {}, 1)'.format(stID, devID, startT, endT)
            #print (query)
        return db.executeNonquery(query)

        #if there's an overlap (only one) we check the time 
        elif len(table) == 1 and datetime.datetime.now() > table[0][2] and (not table[0][5]):
            
            query = 'INSERT INTO DEMAND (STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED) VALUES ({}, {}, {}, {}, 1)'.format(stID, devID, startT, endT)
            return db.executeNonquery(query)
                                                            
        else:
            query = 'INSERT INTO DEMAND (STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED) VALUES ({}, {}, {}, {}, 0)'.format(stID, devID, startT, endT)
            print (query)
            data = manager.executeQuery(query)
            return json.dumps(data) 
    
    #REMOVE FROM DEMAND TABLE FUNC.
    def removeDemand(self, stID, devID, startT):
        query = 'DELETE FROM DEMAND WHERE STUDENT_ID = {} AND DEVICE_ID = {} AND START_TIME = {}'.format(stID, devID, startT)
        print (query)
        return db.executeNOnQuery(query)

    def retrieveDemand_St(self, stID):
        query = 'SELECT* FROM DEMAND WHERE START_TIME = {}'.format(stID)
        #print (query)
        data = manager.executeQuery(query)
        return json.dumps(data) 

    def retrieveDemand_Tech(self, techID):
        query = 'SELECT STUDENT_ID, DEVICE_ID, START_TIME, END_TIME FROM DEMAND, DEVICE WHERE TECH_ID = {}'.format(techID)
        print (query)
        data = manager.executeQuery(query)
        return json.dumps(data) 

dem = Demand_Basics()
dem.insertDemand(1234, 24, 11, 12)
dem.removeDemand(1234, 24, 11)
dem.retrieveDemand_St(1234)
dem.retrieveDemand_Tech(2)

    
    
