from flask import Flask, render_template, request
from manager import Manager
from technician import Technician
from user import User
import datetime

import json



app = Flask(__name__)



m = Manager()
t = Technician()
u = User()



@app.route('/')
def hello():
   return 'hello world'



###############################################roba################################################################


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
		print (result)
		t.update_devicerate(int(result['id'][0]), result['r'][0])

	return json.dumps(result)
	
	
@app.route('/retrive_table/<table>')
def retriveTable (table):
	return u.retrive_table(table)
	
@app.route('/add_os',methods=['POST','GET'])
def addos():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
	
		t.add_os(int(result['id'][0]), result['name'][0],result['link'][0])

	return json.dumps(result)

@app.route('/add_software',methods=['POST','GET'])
def addsoftware():#return the addpc_os function url
	if request.method == 'POST':
		result = request.form
		#return render_template("result.html",result = result)
		result = dict(result)
	
		t.add_software(int(result['id'][0]), result['name'][0],result['link'][0])

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
		#return render_template("result.html",result = result)
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
    m.insertUser(int(result[''][0]), result[''][1], result[''][2], result[''][3], result[''][4])


@app.route('/deletestudent/<int:sid>')
def delStudent(sid):
  m.deleteStudent(sid)


@app.route('/deletetech/<int:tid>')
def delTech(tid):
  m.deleteTech(tid)


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
    return u.login(result['username'][0], result['password'][1])

@app.route('/updateinfo', methods = ['POST'])
def updateInfoAPI():
  if request.method == 'POST':
    result = dict(request.form)
    u.updateInfo(result[''][0], result[''][1], result[''][2])


##########################################hanin##############################################################################


@app.route('/insertdemand', methods = ['POST', 'GET'])
def insertDemand():
    if request.method == 'POST':
        result = request.form
        result = dict(result)
        insertDemand(int(result[''][0]), int(result[''][1]), datetime(result[''][2]), datetime(result[''][3]))
    return



@app.route('/retrievedemand_st', methods = ['POST', 'GET'])
def retrieveDemandS():
    if request.method == 'POST':
        result = request.form
        result = dict(result)
        return retrieveDemand_St(int(result[''][0]))
    


@app.route('/retrievedemand_tech', methods = ['POST', 'GET'])
def retrieveDemandT():
    if request.method == 'POST':
        result = request.form
        result = dict(result)
        return retrieveDemand_Tech(int(result[''][0]))


@app.route('/deletedemand_st', methods = ['POST', 'GET'])
def deleteDemand():
    if request.method == 'POST':
        result = request.form
        result = dict(result)
        deleteDemand_St(int(result[''][0]), int(result[''][1]), datetime(result[''][2]))
    return


####################################################################################################################




if __name__ == '__main__':
   app.run(debug = True)
