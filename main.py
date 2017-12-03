from flask import Flask, render_template, request
app = Flask(__name__)
from manager import Manager
from user import User

@app.route('/')
def hello():
   return 'hello world'

@app.route('/hello/<name>')
def hello_name(name):
	return 'hello {}'.format(name)


@app.route('/getstudents')
def students():
	M=Manager()
	return M.getAllStudets()


@app.route('/retriveDevices/<int:type>')
def student(type):
    return getStudent(type)


@app.route('/getstudent/<int:sid>')
def student(sid):
    return getStudent(sid)


@app.route('/insertuser',methods = ['POST', 'GET'])
def insert():
   if request.method == 'POST':
      result = request.form
      #return render_template("result.html",result = result)
      result = dict(result)
      insertUser(int(result[''][0]), result[''][1], result[''][2], result[''][3], result[''][4])

      return str(result[''])


if __name__ == '__main__':
   app.run(debug = True)
