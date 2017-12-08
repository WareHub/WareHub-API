from user import User


class Technician(User):

    def __init__(self):
        User.__init__(self)



    def add_device(self, id, dtype, location, state, OVERALL_REVIEW,NUM_REVIEWS,tech_id, *args) :
        query = "insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id) + "," +str(dtype)+ ","+str(location) + "," + str(state)+","+ OVERALL_REVIEW+ "," + NUM_REVIEWS + "," + str(tech_id) + ")"
        print(query)
        self.db.executeNonQuery(query)
        come=int(int(id)/10000000)
        if (come==5):
            self.add_pc(id,*args)
        elif (come==7):
            self.add_ic(id,*args)

                     
    	
        return
    def add_pc(self, id,*args):
		#query = "insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ("+str(id)+"," + str(args[0]) + "," + str(args[1])+"," + str(args[2]) + ")"
        query = "insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ({},'{}','{}','{}')".format(id,args[0],args[1],args[2])
        #print(query)
        self.db.executeNonQuery(query)

        return


    def add_pc_os(self, pc_id, os_id):
        query = "insert into HAS_OS(PC_ID , OS_ID ) values( " + str(pc_id) + "," + str(os_id) + ")"
        #print(query)
        self.db.executeNonQuery(query)
        return
        

    def add_pc_software(self, pc_id, software_id):
        query = "insert into  HAS_SOFTWARE(PC_ID , SOFTWARE_ID ) values( " + str(pc_id) + "," + str(software_id) + ")"
        self.db.executeNonQuery(query)
        #print(query)
        return

    def add_ic(self, id,*args) :
        query = "insert into ICS(ID,CODE)values( "+str(id)+",'" + str(args[0]) + "')"
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
        print(query)
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
