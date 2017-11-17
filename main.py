from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      #return render_template("result.html",result = result)
      omar = dict(result)
      return str(omar['Age'][0])


@app.route('/hello/<name>')
def hello(name):
	return 'Hello {}'.format(name)

if __name__ == '__main__':
   app.run(debug = True)