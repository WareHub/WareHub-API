from flask import Flask, render_template, request
from manager import Manager
from user import User


app = Flask(__name__)

m = Manager()
u = User()

@app.route('/')
def hello():
   return 'hello world'



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




if __name__ == '__main__':
   app.run(debug = True)