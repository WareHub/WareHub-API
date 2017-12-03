from flask import Flask, render_template, request
from manager import Manager


app = Flask(__name__)

m = Manager()

@app.route('/')
def hello():
   return 'hello world'

#just for trial
@app.route('/getstudents')
def hello():
   return m.getAllStudets()


if __name__ == '__main__':
   app.run(debug = True)
