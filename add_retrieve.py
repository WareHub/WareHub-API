from dbmanager import DBManager
import json
from passlib.hash import sha256_crypt as scrypt


#this function adds managers, students, technetians to the database
#only managers can call this functions
def insertUser(type, id, name, password, phone, isTA = 0, points = 0):

	manager = DBManager()
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

	manager.executeNonQuery(query2)
	manager.executeNonQuery(query1)



#this function adds a review to the database
def insertReview(sid, deviceid, opinion, rate):
	manager = DBManager()
	date = manager.executeQuery('select GETDATE()')
	query = "insert into REVIEW (STUDENT_ID, DEVICE_ID, R_TIME, OPINION, RATE) values ({}, {}, {}, '{}', {})".format(sid, deviceid, date, opinion, rate)
	manager.executeNonQuery(query)


#this function retreives the reviews of devices and returns it in json string
def getReviews():
	manager = DBManager()
	query = 'select * from REVIEW'
	data = manager.executeQuery(query)
	return json.dumps(data)


#this function retreives the reviews of a specefic device
def getReviewsDevice(id):
	manager = DBManager()
	query = 'select * from REVIEW where DEVICE_ID = {}'.format(id)
	data = manager.executeQuery(query)
	return json.dumps(data)


#this funciton retreives students from database
def getAllStudets():
	manager = DBManager()
	query = 'select * from STUDENT'
	data = manager.executeQuery(query)
	return json.dumps(data)

#this funciton retrieves one student by his/her id
def getStudent(id):
	manager = DBManager()
	query = 'select * from STUDENT where ID = {}'.format(id)
	data = manager.executeQuery(query)
	return json.dumps(data)

#this function retrieves all techniciens
def getAllTech():
	manager = DBManager()
	query = 'select * from TECHNICIAN'
	data = manager.executeQuery(query)
	return json.dumps(data)


#this function retrieves one tech using id
def getTech(id):
	manager = DBManager()
	query = 'select * from TECHNICIAN where ID = {}'.format(id)
	data = manager.executeQuery(query)
	return json.dumps(data)


#this function checks if password is ture of false
def login(id, password):
	manager = DBManager()
	query = 'select PASS from USERS where ID = {}'.format(id)
	data = manager.executeQuery(query)
	hashpass = data.fetchall()[0][0]
	if scrypt.verify(password, hashpass):
		return json.dumps(True)
	else:
		return json.dumps(False)


#this function updates user's info
def updateInfo(type, id, password, phone):

	manager = DBManager()
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

	manager.executeNonQuery(query2)
	manager.executeNonQuery(query1)



#this function updates points of students or techs
def updatePoints(type, id, points):
	manager = DBManager()
	if type == 0:
		query = 'update STUDENT '
	else:
		query = 'update TECHNICIAN '
	query += 'set POINTS = {} where ID = {}'.format(points, id)
	manager.executeNonQuery(query)