from dbmanager import DBManager
import json
from passlib.hash import sha256_crypt as scrypt

class User:
	def __init__(self):
	    self.db=DBManager()

	def retrive_devices(self,type):
	    #type of devicea assumed that type is number if type =0 retruive all devices
	    type=int(type)
	    if (type==5): #for PCs
	        return self.retrive_pc(type)
	    if (type==7): #for ICs
	        return self.retrive_ic(type)
	    check="where D.ID>{} and D.ID<{}".format(type*10000000,(type+1)*10000000)
	    query="select * from DEVICE D {} order by D.overall_review".format(check)
	    if (type==0):
	        query="select * from DEVICE"
	    data =  self.db.executeQuery(query)
	    return json.dumps(data)

	def retrive_table(self,table):
	    #type of devicea assumed that type is number if type =0 retruive all devices
	    query="select * from {}".format(table)
	    data =  self.db.executeQuery(query)
	    return json.dumps(data)

	def retriveOnePC(self,id):
	    #one device with all attributes and reviews
	    query="select * from DEVICE D join PCS P on P.ID=D.ID where D.ID={}".format(id)
	    pc =  self.db.executeQuery(query)
	    query="select O.NAME,O.LINK from HAS_OS HS join OS O on O.ID=HS.OS_ID where HS.PC_ID={}".format(id)
	    oss =  self.db.executeQuery(query)
	    query="select O.NAME,O.LINK from HAS_SOFTWARE HS join SOFTWARE O on O.ID=HS.SOFTWARE_ID	where HS.PC_ID={}".format(id)
	    softwares =  self.db.executeQuery(query)
	    pc.append(oss)
	    pc.append(softwares)
	    return json.dumps(pc)
		
		
	def retrive_ic(self,type):
	    #retrive for ICs only , type is number less than 100 to get IC code
	    check="where D.ID>{} and D.ID<{}".format(type*10000000,(type+1)*10000000)
	    query="select * from DEVICE D join ICS I join IC_TYPE T on T.code=I.code on I.ID=D.ID {} order by D.overall_review".format(check)
	    data =  self.db.executeQuery(query)
	    return json.dumps(data)

	    

	def retrive_pc(self,type):
	    #retrive for PCs only , type is number less than 100 to get PC code
	    check="where D.ID>{} and D.ID<{}".format(type*10000000,(type+1)*10000000)
	    query="select * from DEVICE D join PCS P on P.ID = D.ID {} order by D.overall_review".format(check)
	    data =  self.db.executeQuery(query)
	    return json.dumps(data)


	#this function adds a review to the database
	def insertReview(self, sid, deviceid, opinion, rate):
		date = self.db.executeQuery('select GETDATE()')
		query = "insert into REVIEW (STUDENT_ID, DEVICE_ID, R_TIME, OPINION, RATE) values ({}, {}, {}, '{}', {})".format(sid, deviceid, date, opinion, rate)
		self.db.executeNonQuery(query)


	#this function retreives the reviews of devices and returns it in json string
	def getReviews(self):
		query = 'select * from REVIEW'
		data = self.db.executeQuery(query)
		return json.dumps(data)
	


	#this function retreives the reviews of a specefic device
	def getReviewsDevice(self, id):
		query = 'select * from REVIEW where DEVICE_ID = {}'.format(id)
		data = self.db.executeQuery(query)
		return json.dumps(data)

	#this function checks if password is ture of false
	def login(self, id, password):
		query = 'select PASS from USERS where ID = {}'.format(id)
		data = self.db.executeQuery(query)
		if len(data > 0):
			hashpass = data[0][0]
			return json.dumps(scrypt.verify(password, hashpass))
		else:
			return json.dumps(False)



	#this function updates user's info
	def updateInfo(self, type, id, password, phone):
		hashpass = scrypt.encrypt(password)

		query2 = "update USERS set PASS = '{}' where ID = {}".format(hashpass, id)	
		setquery = "set PHONE = {} where ID = {}".format(phone, id)
		#manager
		if type == 0:
			query1 = "update MANAGER " + setquery
			
		#student
		elif type == 1:
			query1 = "update STUDENT " + setquery

		#technician
		else:
			query1 = "update TECHNICIAN " + setquery

		self.db.executeNonQuery(query2)
		self.db.executeNonQuery(query1)


	#this function updates points of students or techs
	def updatePoints(self, type, id, points):
		if type == 0:
			query = 'update STUDENT '
		else:
			query = 'update TECHNICIAN '
		query += 'set POINTS = {} where ID = {}'.format(points, id)
		self.db.executeNonQuery(query)

