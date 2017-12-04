from flask import Flask, render_template, request
from manager import Manager
from technician import Technician


app = Flask(__name__)


m = Manager()
t = Technician()



@app.route('/')
def hello():
   return 'hello world'


@app.route('/hello/<name>')
def hello_name(name):
	return 'hello {}'.format(name)



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


if __name__ == '__main__':
   app.run(debug = True)