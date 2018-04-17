# -*- coding:utf-8 -*-
from flask import Flask,session

from iHome import *

app = Flask(__name__)







@app.route('/', methods=['GET', 'POST'])
def hello_world():
    session['name'] = 'jack'
    return 'Hello World!'

if __name__ == '__main__':
    manager.run()
