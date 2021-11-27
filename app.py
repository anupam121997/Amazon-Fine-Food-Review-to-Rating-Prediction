# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:01:38 2021

@author: kumar
"""

from flask import Flask, render_template,request
import dummy
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('test.html')

@app.route('/',methods=['POST','GET'])
def getValues():
    query=request.form.get('query')
    model=request.form.get('models')
    a,b=dummy.return_params(query, model)
    return render_template("test.html",a=a,b=b)
	


if __name__ == "__main__":
    app.run(debug=False)