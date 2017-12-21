from user import User
import json


class Technician(User):
    def __init__(self):
        User.__init__(self)


    def add_device(self, id, dtype, location, state, OVERALL_REVIEW,NUM_REVIEWS,tech_id, *args) :
        query = "insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values({}, '{}', {}, {}, {}, {}, {})".format(id, dtype, location, state, OVERALL_REVIEW, NUM_REVIEWS, tech_id)
        #query = "insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id) + ",'" +str(dtype)+ "',"+str(location) + "," + str(state)+","+ str(OVERALL_REVIEW)+ "," + NUM_REVIEWS + "," + str(tech_id) + ")"
        print(query)
        self.db.executeNonQuery(query)
        query= "update TECHNICIAN set POINTS=POINTS+2 where ID={}".format(tech_id)
        self.db.executeNonQuery(query)
        come=int(int(id)/10000000)
        if (come==5):
            self.add_pc(id,*args)
        elif (come==7):
            self.add_ic(id,*args)


    def add_pc(self, id,*args):
		#query = "insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ("+str(id)+"," + str(args[0]) + "," + str(args[1])+"," + str(args[2]) + ")"
        query = "insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ({},'{}','{}','{}')".format(id,args[0],args[1],args[2])
        #print(query)
        self.db.executeNonQuery(query)



    def add_pc_os(self, pc_id, os_id):
        query = "insert into HAS_OS(PC_ID , OS_ID ) values( " + str(pc_id) + "," + str(os_id) + ")"
        #print(query)
        self.db.executeNonQuery(query)
        


    def add_pc_software(self, pc_id, software_id):
        query = "insert into  HAS_SOFTWARE(PC_ID , SOFTWARE_ID ) values( " + str(pc_id) + "," + str(software_id) + ")"
        self.db.executeNonQuery(query)



    def add_ic(self, id,*args) :
        query = "insert into ICS(ID,CODE)values( "+str(id)+",'" + str(args[0]) + "')"
        self.db.executeNonQuery(query)


    def update_devicestate(self, id, state):
        query = "  update DEVICE set STAT =" + str(state) + "where ID =" + str(id) 
        #print(query)
        self.db.executeNonQuery(query)


    def update_devicerate(self, id, rate) :
        query = " update DEVICE set OVERALL_REVIEW+=" + str(rate) + " ,NUM_REVIEWS+=1 where ID =" + str(id)
        self.db.executeNonQuery(query)


    def remove_device(self, id) :
        query = "delete from device where ID=" + str(id)
        #print(query)
        self.db.executeNonQuery(query)
        return

    def add_os(self, name, link) :
        try:
            id = (self.db.executeQuery('select max(ID) from os')[0][0]) + 1
        except TypeError:
            id = 1
        query = "insert into  OS(ID,NAME,LINK ) values(" + str(id) + "," + " '"+str(name) +"'"+ "," +" '"+ str(link)+" '" + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return

    def add_software(self, name, link) :
        try:
            id = (self.db.executeQuery('select max(ID) from software')[0][0]) + 1
        except TypeError:
            id = 1
        query = "insert into SOFTWARE(ID,NAME,LINK ) values(" + str(id) + "," +"'"+ str(name)+"'" + "," +"'" +str(link)+"'" + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return

    def add_ictype(self, Gate , link) :
        try:
            query = "insert into  IC_TYPE(CODE,link ) values(" +str(Gate) + "," + "'"+str(link)+"'" + ")"
        except TypeError:
            id = 1
        #print(query)
        self.db.executeNonQuery(query)
        return

    def retrieveDemand_Tech(self, techID):
        query= "update TECHNICIAN set POINTS=POINTS+4 where ID={}".format(techID)
        self.db.executeNonnQuery(query)
        query = 'SELECT STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED, INUSE FROM DEMAND join DEVICE on ID = DEVICE_ID WHERE TECH_ID = {}'.format(techID)
        #print (query)
        data = self.db.executeQuery(query)
        
        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][2] = str(data[i][2])
            data[i][3] = str(data[i][3])
        return json.dumps(data)

    def getSoftware(self):
        query = 'SELECT * from SOFTWARE'
        data = self.db.executeQuery(query)
        return json.dumps(data)

    def getOS(self):
        query = 'SELECT * from OS'
        data = self.db.executeQuery(query)
        return json.dumps(data)
        
    def setInUse(self, sID, dID, sDate):
        query = "UPDATE DEMAND SET INUSE = 1 where STUDENT_ID = {} and DEVICE_ID = {} and START_TIME = CONVERT(datetime2, '{}')".format(sID, dID, sDate)
        self.db.executeNonQuery(query)

