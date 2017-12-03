from flask import Flask, render_template, request
app = Flask(__name__)
from add_retrieve import *
import datetime

@app.route('/')
def hello():
   return 'hello world'

@app.route('/hello/<name>')
def hello_name(name):
	return 'hello {}'.format(name)


@app.route('/getstudents')
def students():
	return getAllStudets()


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
