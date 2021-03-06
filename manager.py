from dbmanager import DBManager
from user import User
from passlib.hash import sha256_crypt as scrypt
import json


class Manager(User):

	def __init__(self):
		User.__init__(self)



	#this function adds managers, students, technetians to the database
	#only managers can call this functions
	def insertUser(self, type, name, password, phone, isTA = 0, points = 0):
		hashpass = scrypt.encrypt(password)
		try:
			id = (self.db.executeQuery('select max(ID) from USERS')[0][0]) + 1
		except TypeError:
			id = 1

		query2 = "insert into USERS (ID, PASS) values ({}, '{}')".format(id, hashpass)	
		#manager
		if type == 0:
			query1 = "insert into MANAGER (ID, NAME, PHONE) values ({}, '{}', {})".format(id, name, phone)
		
		#student
		elif type == 1:
			query1 = "insert into STUDENT (ID, NAME, PHONE, TA, POINTS) values ({}, '{}', {}, {}, {})".format(id, name, phone, isTA, points)

		#technician
		else:
			query1 = "insert into TECHNICIAN (ID, NAME, PHONE, POINTS) values ({}, '{}', {}, {})".format(id, name, phone, points)

		self.db.executeNonQuery(query2)
		self.db.executeNonQuery(query1)




	#this funciton retreives students from database
	def getAllStudets(self):
		query = 'select * from STUDENT'
		data = self.db.executeQuery(query)
		return json.dumps(data)

	#this funciton retrieves one student by his/her id
	def getStudent(self, id):
		query = 'select * from STUDENT where ID = {}'.format(id)
		data = self.db.executeQuery(query)
		return json.dumps(data)

	#this function retrieves all techniciens
	def getAllTech(self):
		query = 'select * from TECHNICIAN'
		data = self.db.executeQuery(query)
		return json.dumps(data)


	#this function retrieves one tech using id
	def getTech(self, id):
		query = 'select * from TECHNICIAN where ID = {}'.format(id)
		data = self.db.executeQuery(query)
		return json.dumps(data)

	#this function retrieves one manager using id
	def getManager(self, id):
		query = 'select * from MANAGER where ID = {}'.format(id)
		data = self.db.executeQuery(query)
		return json.dumps(data)

	#this function deletes a tech using id
	def deleteUser(self, id):
		query = 'delete from USERS where ID = {}'.format(id)
		self.db.executeNonQuery(query)
    #this function to get the rushhour of demands 
	
	def rushhour(self):
		query = 'select   AS time)as demand_time, count(*) as demand_count from  DEMAND Group by cast(CONVERT(TIME(0), [START_TIME]) AS time) Order By demand_count desc'
		data = self.db.executeQuery(query)
		for i in range(len(data)):
			data[i] = list(data[i])
			data[i][0] = str(data[i][0])[:8]
		return json.dumps(data)

	 #this function to get the rushday  of demands 	
	def	crowdedday(self):
		query='select cast(START_TIME as date) as time, count(*) as demand_count from DEMAND Group by cast(START_TIME as date) Order By demand_count desc'
		data=self.db.executeQuery(query)
		for i in range(len(data)):
			data[i] = list(data[i])
			data[i][0] = str(data[i][0])
		return json.dumps(data)
		
	def getcomplain(self):
		query='SELECT ID, COUNT(*) AS COMPLAIN_COUNT FROM DEVICE, REVIEW WHERE DEVICE_ID = ID AND RATE < 3GROUP BY ID, DTYPE, STAT, OVERALL_REVIEW, NUM_REVIEWS, TECH_ID, ID, DTYPE, LOCATION ORDER BY COMPLAIN_COUNT DESC'
		data=self.db.executeQuery(query)
		return json.dumps(data)
		
	def mostused_ic(self):
		query='SELECT I.CODE, COUNT(*) AS USES FROM ICS, DEMAND AS D WHERE ICS.ID = D.DEVICE_ID AND INUSE = 2 GROUP BY CODE ORDER BY USES DESC'
		data=self.db.executeQuery(query)
		return json.dumps(data)
		

	def mostused_pc(self):
		query='SELECT PC.ID, COUNT(*) AS USES FROM PCS AS PC, DEMAND AS D WHERE PC.ID = D.DEVICE_ID AND INUSE = 2 GROUP BY PC.ID ORDER BY USES DESC'		

		data=self.db.executeQuery(query)
		return json.dumps(data)


	def mostused_software(self):
		query='SELECT NAME, COUNT(*) AS USES FROM HAS_SOFTWARE, DEMAND, SOFTWARE WHERE PC_ID = DEVICE_ID AND ID = SOFTWARE_ID GROUP BY NAME ORDER BY USES DESC'
		data=self.db.executeQuery(query)
		return json.dumps(data)

		
	def mostused_os(self):
		query='SELECT NAME, COUNT(*) AS USES FROM HAS_OS, DEMAND, OS WHERE PC_ID = DEVICE_ID AND OS_ID = ID  GROUP BY NAME ORDER BY USES DESC'
		data=self.db.executeQuery(query)
		return json.dumps(data)
	def mostdemanded_pcs(self):
		query='SELECT PC.ID, COUNT(*) AS USES FROM PCS AS PC, DEMAND AS D WHERE PC.ID = D.DEVICE_ID  GROUP BY PC.ID ORDER BY USES DESC'
		data=self.db.executeQuery(query)
		return json.dumps(data)
		
	def mostdemanded_ic(self):
		query='SELECT code, COUNT(*) AS USES  FROM ICS, DEMAND AS D WHERE ICS.ID = D.DEVICE_ID GROUP BY CODE ORDER BY USES'
		data=self.db.executeQuery(query)
		return json.dumps(data)
 
	def mostvisited(self):
		query='SELECT LOCATION, COUNT(*) AS VISITS_COUNT FROM DEVICE, DEMAND WHERE DEVICE_ID = ID AND INUSE = 2 GROUP BY LOCATION ORDER BY VISITS_COUNT DESC'
		data=self.db.executeQuery(query)
		return json.dumps(data)
