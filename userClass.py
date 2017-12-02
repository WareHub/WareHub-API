import json
from dbmanager import DBManager

class users:
    def __init__(self):
        self.db=DBManager()
     
    def update_info(self,ID,table,**kwargs):
        #ID of updater, name of table and kwargs is ([phone:123,password:123])
        seted=""
        for key in kwargs:
            seted+="{}={}".format(key,kwargs[key])
        query="UPDATE {} Set {} Where ID={}".format(table,seted,ID)
        db.executeCommand(query)
    
    def retrive_devices(self,type):
        #type of devicea assumed that type is number
        if (type==5): #for PCs 
            return self.retrive_pc(type)
        if (type==7): #for ICs
            return self.retrive_ic(type)
        check="where ID>{} and ID<{}".format(type*10000000,(type+1)*10000000)
        query="select * from DEVICE D {} order by D.overall_review/D.Num_reviews".format(check)
        table=db.executeCommand(query)
        table=table.fetchall()
        return json.dumps(table)


    
    def retrive_ic(self,type):
        #retrive for ICs only , type is number less than 100 to get IC code
        check="where D.ID>{} and D.ID<{}".format(type*10000000,(type+1)*10000000)
        query="select * from DEVICE D join ICS I join IC_TYPE T on T.code=I.code on I.ID=D.ID {} order by D.overall_review/D.Num_reviews".format(check)
        table=db.executeCommand(query)
        table=table.fetchall()
        return json.dumps(table)

        
    
    def retrive_pc(self,type):
        #retrive for PCs only , type is number less than 100 to get PC code
        check="where ID>{} and ID<{}".format(type*1000000,(type+1)*1000000)
        query="select * from DEVICE D join PCS P on P.ID = D.ID {} order by D.overall_review/D.Num_reviews, D.ID".format(check)
        table=db.executeCommand(query)
        table=table.fetchall()
        return json.dumps(table)
