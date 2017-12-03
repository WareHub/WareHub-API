import user


class Technician(user.User):
    def add_device(id, dtype, location, state, tech_id, *args) :
        query = "insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id) + "," +str(dtype)+ ","+str(location) + "," + str(state)+","+  str(0) + "," + str(0) + "," + str(tech_id) + ")"
        print(query)
        #db.executeCommand(query)
        if (dtype==5):
            add_pc(id,*args)
        elif (dtype==7):
            add_ic(id,*args)

                     
    	
        return
    def add_pc(id,*args) :
        query = "insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ("+str(id)+"," + str(args[0]) + "," + str(args[1])+"," + str(args[2]) + ")"

        #print(query)
        db.executeNonQuery(query)

        return


    def add_pc_os(pc_id, os_id) :
        query = "insert into HAS_OS(PC_ID , OS_ID ) values( " + str(pc_id) + "," + str(os_id) + ")"
        #print(query)
        db.executeNonQuery(query)
        return
        

    def add_pc_software(pc_id, software_id) :
        query = "insert into  HAS_SOFTWARE(PC_ID , SOFTWARE_ID ) values( " + str(pc_id) + "," + str(software_id) + ")"
        #print(query)
        return

    def add_ic(id,*args) :
        query = "insert into ICS(ID,CODE)values( "+str(id)+"," + str(args[0]) + ")"
        #print(query)
        db.executeNonQuery(query)
        return

    def update_devicestate(id, state) :
        query = "  update DEVICE set STAT =" + str(state) + "where ID =" + str(id) 
        #print(query)
        db.executeNonQuery(query)
        return

    def update_devicerate(id, rate) :
        query = " update DEVICE set OVERALL_REVIEW+=" + str(rate) + " ,NUM_REVIEWS+=1 where ID =" + str(id)
        #print(query)
        db.executeNonQuery(query)

        return


    def remove_device(id) :
        query = "delete from device where ID=" + str(id)
        #print(query)
        db.executeNonQuery(query)
        return

    def add_os(id, name, link) :
        query = "insert into  OS(ID,NAME,LINK ) values(" + str(id) + "," + " '"+str(name) +"'"+ "," +" '"+ str(link)+" '" + ")"
        #print(query)
        db.executeNonQuery(query)
        return

    def add_software(id, name, link) :
        query = "insert into SOFTWARE(ID,NAME,LINK ) values(" + str(id) + "," +"'"+ str(name)+"'" + "," +"'" +str(link)+"'" + ")"
        #print(query)
        db.executeNonQuery(query)
        return

    def add_ictype(Gate , link) :
        query = "insert into  IC_TYPE(CODE,link ) values(" +str(Gate) + "," + "'"+str(link)+"'" + ")"
        #print(query)
        db.executeNonQuery(query)
        return
