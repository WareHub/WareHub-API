from user import User
import json

class Technician(User):

    def __init__(self):
        User.__init__(self)



    def add_device(self, id, dtype, location, state, tech_id, *args) :
        query = "insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id) + "," +str(dtype)+ ","+str(location) + "," + str(state)+","+  str(0) + "," + str(0) + "," + str(tech_id) + ")"
        print(query)
        #self.db.executeCommand(query)
        if (id>50000000 and id < 60000000):
            add_pc(id,*args)
        elif (id > 70000000):
            add_ic(id,*args)

                     
    	
        return
    def add_pc(self, id,*args) :
        query = "insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ("+str(id)+"," + str(args[0]) + "," + str(args[1])+"," + str(args[2]) + ")"

        #print(query)
        self.db.executeNonQuery(query)

        return


    def add_pc_os(self, pc_id, os_id) :
        query = "insert into HAS_OS(PC_ID , OS_ID ) values( " + str(pc_id) + "," + str(os_id) + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return
        

    def add_pc_software(self, pc_id, software_id) :
        query = "insert into  HAS_SOFTWARE(PC_ID , SOFTWARE_ID ) values( " + str(pc_id) + "," + str(software_id) + ")"
        #print(query)
        return

    def add_ic(self, id,*args) :
        query = "insert into ICS(ID,CODE)values( "+str(id)+"," + str(args[0]) + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return

    def update_devicestate(self, id, state) :
        query = "  update DEVICE set STAT =" + str(state) + "where ID =" + str(id) 
        #print(query)
        self.db.executeNonQuery(query)
        return

    def update_devicerate(self, id, rate) :
        query = " update DEVICE set OVERALL_REVIEW+=" + str(rate) + " ,NUM_REVIEWS+=1 where ID =" + str(id)
        #print(query)
        self.db.executeNonQuery(query)

        return


    def remove_device(self, id) :
        query = "delete from device where ID=" + str(id)
        #print(query)
        self.db.executeNonQuery(query)
        return

    def add_os(self, id, name, link) :
        query = "insert into  OS(ID,NAME,LINK ) values(" + str(id) + "," + " '"+str(name) +"'"+ "," +" '"+ str(link)+" '" + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return

    def add_software(self, id, name, link) :
        query = "insert into SOFTWARE(ID,NAME,LINK ) values(" + str(id) + "," +"'"+ str(name)+"'" + "," +"'" +str(link)+"'" + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return

    def add_ictype(self, Gate , link) :
        query = "insert into  IC_TYPE(CODE,link ) values(" +str(Gate) + "," + "'"+str(link)+"'" + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return

    def retrieveDemand_Tech(self, techID):
        query = 'SELECT STUDENT_ID, DEVICE_ID, START_TIME, END_TIME, RESERVED, INUSE FROM DEMAND join DEVICE on ID = DEVICE_ID WHERE TECH_ID = {}'.format(techID)
        #print (query)
        data = self.db.executeQuery(query)
        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][2] = str(data[i][2])
            data[i][3] = str(data[i][3])
        return json.dumps(data)


