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
#    pdb.set_trace() 
    page_size = 5
    q = request.form.get('q','')
    q = q.strip().split(';') 
    page = int(request.args.get('page','1'))
    Previous = '/?page={}'.format(page-1)
    Next = '/?page={}'.format(page+1)
    query = query_logic(q)
    data = mongo.coll.find(query).limit(page_size).skip((page-1) * page_size)

    return render_template('index.html',data=data,Previous=Previous,Next=Next)


@app.route('/search.html',methods=['POST','GET'])
def search():
    return render_template('search.html',data=[])



if __name__ == '__main__':
    app.run(debug=True)
