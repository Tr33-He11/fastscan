#!/usr/bin/env python
# coding=utf-8
from flask import Flask,request,render_template,redirect,url_for
from lib.mongo import MongoDB 
from lib.query_logic import query_logic 
import re 
import pdb

app = Flask(__name__) 
mongo = MongoDB() 

@app.route('/index.html')
@app.route('/',methods=['POST','GET']) 
def index():
    if request.method == 'POST':
        if request.form['q']:
            q = request.form['q'] 
            q = q.strip().split(';')
            query = query_logic(q)
            data = mongo.coll.find(query)
        else:
            data = []
    else:
        data = []

    return render_template('index.html',data=data)


@app.route('/search.html',methods=['POST','GET'])
def search():
    return render_template('search.html',data=[])



if __name__ == '__main__':
    app.run(debug=True)
