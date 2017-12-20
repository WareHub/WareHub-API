output=open('restdevice.sql','w')
id1=50000000
for i in range(5):
	query="insert into PCS(ID,GPU ,CPU ,RAM ) VALUES ("+str(id1 + i)+"," + "'amd'" + "," + "'intel'"+"," + '5' + ")"
	output.write(query+'\n')
	

id7=70000000
for i in range(5):
	query="insert into ICS(ID,CODE)values( "+str(id7 +i)+",'" + '7408' + "')"
	output.write(query+'\n')
	
id1=50000000					
for i in range(5):
	query="insert into HAS_OS(PC_ID , OS_ID ) values( " + str(id1+i) + "," + str(i) + ")"
	output.write(query+'\n')
id1=50000000					
for i in range(5):
	query="insert into  HAS_SOFTWARE(PC_ID , SOFTWARE_ID ) values( " + str(id1+i) + "," + str(i) + ")"
	output.write(query+'\n')
for i in range(5):
	query="insert into SOFTWARE(ID,NAME,LINK ) values(" + str(i+1) + "," +"'"+ 'visualstudio'+str(i)+"'" + "," +"'" +'visualstudio.com'+"'" + ")"
	output.write(query+'\n')

for i in range(5):
	query="insert into  OS(ID,NAME,LINK ) values(" + str(i+1) + "," + " '"+'windows'+str(i+5) +"'"+ "," +" '"+ 'windows.com'+" '" + ")"
	output.write(query+'\n')	
	
for i in range(5):
	query="insert into  IC_TYPE(CODE,link ) values(" +"'7408'" + "," + "'"+'texasinstrument.com'+"'" + ")"	
	output.write(query+'\n')	
		

	