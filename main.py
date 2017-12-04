from flask import Flask, render_template, request
from manager import Manager
from technician import Technician
from user import User
import datetime



app = Flask(__name__)



m = Manager()
t = Technician()
u = User()



@app.route('/')
def hello():
   return 'hello world'



###############################################roba################################################################

'''
@app.route('/add_device',methods=['POST','GET'])
    def addevice():#return the addevice function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
			if( result[''][1]==5)
				add_device(int(result[''][0]), result[''][1], result[''][2], result[''][3], result[''][4],result[''][5],result[''][6],result[''][7],result[''][8])
			
            else
				add_device(int(result[''][0]), result[''][1], result[''][2], result[''][3], result[''][4],result[''][5])

		return str(result[''])
		
	@app.route('/add_pc',methods=['POST','GET'])
    def addpc():#return the addpc function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
			
			add_pc(int(result[''][0]), result[''][1], result[''][2], result[''][3], result[''][4])

		return str(result[''])
		
		
		
	@app.route('/add_pc_os',methods=['POST','GET'])
    def addpc_os():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			add_pc_os(int(result[''][0]), result[''][1])

		return str(result[''])
			
		
	@app.route('/add_pc_software',methods=['POST','GET'])
    def addpc_software():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			add_pc_software(int(result[''][0]), result[''][1])

		return str(result[''])
			
	@app.route('/add_ic',methods=['POST','GET'])
    def addic():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			add_ic(int(result[''][0]), result[''][1])

		return str(result[''])
			
				
    @app.route('/update_devicestate',methods=['POST','GET'])
    def updatedevicestate():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			update_devicestate(int(result[''][0]), result[''][1])

		return str(result[''])
			
	@app.route('/update_devicerate',methods=['POST','GET'])
    def updatedevicerate():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			update_devicestate(int(result[''][0]), result[''][1])

		return str(result[''])
	
	@app.route('/add_os',methods=['POST','GET'])
    def addos():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			add_os(int(result[''][0]), result[''][1],result[''][2])

		return str(result[''])
	@app.route('/add_software',methods=['POST','GET'])
    def addsoftware():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			add_software(int(result[''][0]), result[''][1],result[''][2])

		return str(result[''])	
	@app.route('/add_ictype',methods=['POST','GET'])
    def addictype():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			add_software(int(result[''][0]), result[''][1])
			
    @app.route('/remove_ic',methods=['POST','GET'])
    def removeic():#return the addpc_os function url
		if request.method == 'POST':
			result = request.form
			#return render_template("result.html",result = result)
			result = dict(result)
		
			remove_ic(int(result[''][0]))

		return str(result[''])	 
'''

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
  if requet.method  == 'POST':
    result = dict(request.form)
    return u.login(result[''][0], result[''][1])

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
