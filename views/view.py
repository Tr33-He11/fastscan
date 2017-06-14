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
    ip_count = len(mongo.coll.distinct('ip'))
    result_count = mongo.coll.count()  
    return render_template('index.html',ip_count=ip_count,result_count=result_count) 


@app.route('/result.html',methods=['POST','GET'])
def result(): 
    q = request.args.get('q','')
    q = q.strip().split(';')
    query = query_logic(q)
    data = mongo.coll.find(query).sort([('ip',1),('port',1)])

    return render_template('result.html',data=data,q=q)


@app.route('/search.html',methods=['POST','GET'])
def search():
    return render_template('search.html')

@app.route('/test.html')
def test():
    data = mongo.coll.find().sort([('ip',1),('port',1)])
    return render_template('test.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)
