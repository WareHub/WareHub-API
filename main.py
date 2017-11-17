from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
   return 'hello world'

@app.route('/hello/<name>')
def hello_name(name):
	return 'hello {}'.format(name)


if __name__ == '__main__':
   app.run(debug = True)