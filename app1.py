# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:26:50 2021

@author: Balaji Rubha
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

