from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
   return'hello world'

@app.route('/result',methods = ['POST', 'GET'])
def result():
   return 'result'


@app.route('/hello/<name>')
def hello(name):
	return 'Hello {}'.format(name)

if __name__ == '__main__':
   app.run(debug = True)