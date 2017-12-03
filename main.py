from flask import Flask, render_template, request
from manager import Manager


app = Flask(__name__)

m = Manager()

@app.route('/')
def hello():
   return 'hello world'



if __name__ == '__main__':
   app.run(debug = True)