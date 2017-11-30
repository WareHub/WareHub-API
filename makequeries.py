

id = 10000000
name = "'student"
password = "'11111111'"
phone = 201000000000
name2 = "'tech"
ta = '0'
points = 0

file = open('file.txt', 'w')

for i in range(50):
	query = 'insert into USERS values({}, {})'.format(id + 2*i, password)
	file.write(query + '\n')
	query = 'insert into STUDENT values ({}, {}, {}, {}, {})'.format(id + 2*i, name + str(i) + "'", phone, ta, points)
	file.write(query + '\n')
	query = 'insert into USERS values({}, {})'.format(id + 2*i+1, password)
	file.write(query + '\n')
	query = 'insert into TECHNICIAN values ({}, {}, {}, {})'.format(id + 2*i+1, name2 + str(i) + "'", phone, points)
	file.write(query + '\n')
	