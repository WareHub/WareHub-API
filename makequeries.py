from passlib.hash import sha256_crypt as scrypt

id = 10000000
name = "'student"
password = '0000'
phone = 201000000000
name2 = "'tech"
ta = '0'
points = 0

file = open('insertqueries.sql', 'w')

query = "insert into USERS values({}, '{}')".format(id, scrypt.encrypt(password))
file.write(query + '\n')
query = "insert into MANAGER values ({}, '{}', {})".format(id, "manager1", phone)
file.write(query + '\n')

query = "insert into USERS values({}, '{}')".format(id + 1, scrypt.encrypt(password))
file.write(query + '\n')
query = "insert into MANAGER values ({}, '{}', {})".format(id + 1, "manager2", phone)
file.write(query + '\n')

id = id + 2

for i in range(50):
	query = "insert into USERS values({}, '{}')".format(id + 2*i, scrypt.encrypt(password))
	file.write(query + '\n')
	query = 'insert into STUDENT values ({}, {}, {}, {}, {})'.format(id + 2*i, name + str(i) + "'", phone, ta, points)
	file.write(query + '\n')
	query = "insert into USERS values({}, '{}')".format(id + 2*i+1, scrypt.encrypt(password))
	file.write(query + '\n')
	query = 'insert into TECHNICIAN values ({}, {}, {}, {})'.format(id + 2*i+1, name2 + str(i) + "'", phone, points)
	file.write(query + '\n')
	