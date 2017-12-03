from dbmanager import DBManager
from user import User
import json


class Manager(User):

	def __init__(self):
		User.__init__(self)



	#this function adds managers, students, technetians to the database
	#only managers can call this functions
	def insertUser(self, type, id, name, password, phone, isTA = 0, points = 0):
		hashpass = scrypt.encrypt(password)

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

	#this function deletes a tech using id
	def deleteTech(self, id):
		query = 'delete from TECHNICIAN where ID = {}'.format(id)
		self.db.executeNonQuery(query)

	#this funcion deletes a student using his id
	def deleteStudent(self, id):
		query = 'delete from STUDENT where ID = {}'.format(id)
		self.db.executeNonQuery(query)