from dbmanager import DBManager
import user


class Manager(user.User):
#this function adds managers, students, technetians to the database
#only managers can call this functions
	def insertUser(type, id, name, password, phone, isTA = 0, points = 0):
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

		db.executeNonQuery(query2)
		db.executeNonQuery(query1)




#this funciton retreives students from database
	def getAllStudets():
		query = 'select * from STUDENT'
		data = db.executeQuery(query)
		return json.dumps(data)

#this funciton retrieves one student by his/her id
	def getStudent(id):
		query = 'select * from STUDENT where ID = {}'.format(id)
		data = db.executeQuery(query)
		return json.dumps(data)

#this function retrieves all techniciens
	def getAllTech():
		query = 'select * from TECHNICIAN'
		data = db.executeQuery(query)
		return json.dumps(data)


#this function retrieves one tech using id
	def getTech(id):
		query = 'select * from TECHNICIAN where ID = {}'.format(id)
		data = db.executeQuery(query)
		return json.dumps(data)