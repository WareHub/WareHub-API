output=open('device2.sql','w')
id1=1000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id1) + str(i)+ ",'" +'microphone'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000003' + ")"
	output.write(query+'\n')
	
id2=2000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id2) + str(i)+ ",'" +'datashow'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000003' + ")"
	output.write(query+'\n')
	
id3=3000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id3) + str(i)+ ",'" +'kits'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000005' + ")"
	output.write(query+'\n')
	
id4=4000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id4) + str(i)+ ",'" +'uno'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000005' + ")"
	output.write(query+'\n')
	
id5=5000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id5) + str(i)+ ",'" +'dell'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000007' + ")"
	output.write(query+'\n')
	
id6=6000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id6) + str(i)+ ",'" +'breadboard'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000007' + ")"
	output.write(query+'\n')
	
id7=7000010
for i in range(20):
	query="insert into DEVICE(ID,DTYPE,LOCATION,STAT,OVERALL_REVIEW,NUM_REVIEWS,TECH_ID) Values(" + str(id7) + str(i)+ ",'" +'fairchild'+str(i)+ "',"+str(i) + "," + '0'+","+ '0'+ "," + '0' + "," +'10000003' + ")"
	output.write(query+'\n')
	
					