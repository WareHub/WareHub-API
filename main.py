from flask import Flask, render_template, request
from manager import Manager
from technician import Technician
from user import User
from student import Student
import datetime
import json



app = Flask(__name__)



m = Manager()
t = Technician()
u = User()
s = Student()



@app.route('/')
def hello():
   return 'hello world'


@app.route('/add_device',methods=['POST','GET'])
def addevice():#return the addevice function url
	if request.method == 'POST':
		result = request.form
		result = dict(result)
		if( int(result['id'][0])>50000000 and int(result['id'][0]) <60000000):
			t.add_device(int(result['id'][0]), result['dtype'][0], int(result['location'][0]), result['state'][0], result['OVERALL_REVIEW'][0],result['NUM_REVIEWS'][0],result['tech_id'][0],result['CPU'][0],result['GPU'][0],result['RAM'][0])
		elif(int(result['id'][0])>70000000 and int(result['id'][0])<80000000):
			t.add_device(int(result['id'][0]), result['dtype'][0], int(result['location'][0]), result['state'][0], result['OVERALL_REVIEW'][0],result['NUM_REVIEWS'][0],result['tech_id'][0],result['code'][0])
		else:
			t.add_device(int(result['id'][0]),result['dtype'][0], int(result['location'][0]), int(result['state'][0]), int(result['OVERALL_REVIEW'][0]),int(result['NUM_REVIEWS'][0]),int(result['tech_id'][0]))
		return json.dumps(result)

		
		
@app.route('/add_pc_os',methods=['POST','GET'])
def addpc_os():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
		t.add_pc_os(int(result['pc_id'][0]), result['os_id'][0])
	return json.dumps(result)

		

@app.route('/add_pc_software',methods=['POST','GET'])
def addpc_software():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
		t.add_pc_software(int(result['pc_id'][0]), result['software_id'][0])
	return json.dumps(result)

@app.route('/getsoftware')
def getSoftware():#return the addpc_os function url
	return t.getSoftware()

@app.route('/getOS')
def getOS():#return the addpc_os function url
	return t.getOS()
				
@app.route('/update_devicestate',methods=['POST','GET'])
def updatedevicestate():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
		t.update_devicestate(int(result['id'][0]), result['state'][0])
	return json.dumps(result)



@app.route('/update_devicerate',methods=['POST','GET'])
def updatedevicerate():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
		t.update_devicerate(int(result['id'][0]), result['r'][0])
	return json.dumps(result)
	
	
@app.route('/retrive_table/<table>')
def retriveTable (table):
	return u.retrive_table(table)
	

@app.route('/add_os',methods=['POST','GET'])
def addos():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		result = dict(result)
		t.add_os(result['name'][0],result['link'][0])
	return json.dumps(result)


@app.route('/add_software',methods=['POST','GET'])
def addsoftware():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
		t.add_software(result['name'][0], result['link'][0])
	return json.dumps(result)



@app.route('/add_ictype',methods=['POST','GET'])
def addictype():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
		t.add_ictype(int(result['code'][0]), result['gate'][0])
	return json.dumps(result)	
			
@app.route('/remove_Device',methods=['POST','GET'])
def removeDevice():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		result = dict(result)
		t.remove_device(int(result['id'][0]))
	return json.dumps(result)



@app.route('/retrive_devices/<int:did>')
def retdevices(did):
  return u.retrive_devices(did)


@app.route('/retriveOnePC/<int:pcid>')
def retrive1pc(pcid):
	return u.retriveOnePC(pcid)


###############################################omar###########################################

@app.route('/getstudents')
def getstudents():
   return m.getAllStudets()

@app.route('/gettechs')
def getTechs():
  return m.getAllTech() 

@app.route('/getstudent/<int:sid>')
def getStudentByID(sid):
  return m.getStudent(sid)

@app.route('/gettech/<int:tid>')
def getTechByID(tid):
  return m.getTech(tid)

@app.route('/insertuser', methods = ['POST'])
def insertUserAPI():
  if request.method == 'POST':
    result = dict(request.form)
    m.insertUser(int(result[''][0]), result[''][1], result[''][2], result[''][3], result[''][4], result[''][5])
    return json.dumps(result)


@app.route('/deleteuser/<int:sid>', methods = ['DELETE'])
def delUser(sid):
  m.deleteUser(sid)


@app.route('/insertreview', methods = ['POST'])
def insertrev():
	if request.method == 'POST':
		result = dict(request.form)
		s.insertReview(result[''][0], result[''][1], result[''][2], result[''][3], result[''][4])


@app.route('/getreviews')
def getReviewsAPI():
  return u.getReviews()


@app.route('/getdevicereviews/<int:dID>')
def getDeviceReviews(dID):
  return u.getReviewsDevice(dID)


@app.route('/login', methods = ['POST'])
def loginAPI():
  if request.method  == 'POST':
    result = dict(request.form)
    return u.login(result[''][0], result[''][1])


@app.route('/updateinfo', methods = ['POST'])
def updateInfoAPI():
  if request.method == 'POST':
    result = dict(request.form)
    u.updateInfo(int(result[''][0]), result[''][1], result[''][2],  result[''][3])

@app.route('/getmanager/<int:mID>')
def getManager(mID):
	return m.getManager(mID)


@app.route('/setinuse', methods = ['POST'])
def setUsage():
	if request.method == 'POST':
		result = dict(request.form)
		t.setInUse(result[''][0], result[''][1], result[''][2])


##########################################hanin##############################################################################

@app.route('/insertdemand', methods = ['POST'])
def insertDemand():
    if request.method == 'POST':
        result = request.form
        result = dict(result)
        s.insertDemand(result[''][0], result[''][1], result[''][2], result[''][3])
        



@app.route('/retrievedemand_st/<int:sid>')
def retrieveDemandS(sid):
        return s.retrieveDemand_St(sid)
    


@app.route('/retrievedemand_tech/<int:tid>')
def retrieveDemandT(tid):
        return t.retrieveDemand_Tech(tid)


@app.route('/deletedemand_st', methods = ['POST'])
def deleteDemand():
    if request.method == 'POST':
        result = request.form
        result = dict(result)
        s.removeDemand(result[''][0], result[''][1], result[''][2])


###############################################stats################################################################
@app.route('/getrushhour')
def getrush_hour():
	return m.rushhour()


@app.route('/getcrowded_day')
def getcrowded_day():
	return m.crowdedday()
	
@app.route('/getmostused_ic')	
def mostused__ic():
	return m.mostused_ic()
		
		
		
	
@app.route('/getmostused_pc')	
def mostused__pc():
		
		return m.mostused_pc()


@app.route('/getmostused_software')	
def mostused__software():
		
		return  m.mostused_software()

@app.route('/getmostused_os')			
def mostused__os():
		return m.mostused_os()
@app.route('/getmostdemanded_pcs')			
def mostdemanded__pcs():
		return m.mostdemanded_pcs()
@app.route('/getmostdemanded_ic')			
def mostdemanded__ic():
		return m.mostdemanded_ic()
 	
	
@app.route('/getmostvisited_ic')			
def mostvisited():
		return m.mostvisited()
 		
@app.route('/getcomplains')
def complains():
		return m.getcomplain()	
	
	
	
	
	
	
###########################################################################################################################################	

if __name__ == '__main__':
   app.run(debug = True)
