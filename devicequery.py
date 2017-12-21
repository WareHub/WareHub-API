output=open('device2.sql','w')
id1=10000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id1+i)+ ",'" +'microphone'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000003' + ")"
	output.write(query+'\n')
	
id2=20000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id2+i)+ ",'" +'datashow'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000003' + ")"
	output.write(query+'\n')
	
id3=30000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id3+i)+ ",'" +'kits'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000005' + ")"
	output.write(query+'\n')
	
id4=40000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id4+i)+ ",'" +'uno'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000005' + ")"
	output.write(query+'\n')
	
id5=50000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id5+i)+ ",'" +'dell'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000007' + ")"
	output.write(query+'\n')
	
id6=60000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id6+i)+ ",'" +'breadboard'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000007' + ")"
	output.write(query+'\n')
	
id7=70000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id7+i)+ ",'" +'fairchild'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000003' + ")"
	output.write(query+'\n')
	
					