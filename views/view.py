#!/usr/bin/env python
# coding=utf-8
from flask import Flask,request,render_template,redirect,url_for,jsonify
from lib.mongo import MongoDB 
from lib.query_logic import query_logic   
from urllib import parse 
import re  
import json
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
#    q = request.args.get('q','')
#    q = q.strip().split(';')
#    query = query_logic(q)
#    data = mongo.coll.find(query).sort([('ip',1),('port',1)])

    return render_template('result.html') 


@app.route('/search.html',methods=['POST','GET'])
def search():
    return render_template('search.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/data.json',methods=['POST','GET'])
def json():       
    referer = request.headers['Referer']    
    if referer.find('result') != -1:
        parse_result = parse.urlparse(referer) 
        param_dict = parse.parse_qs(parse_result.query)  
        try:
            q = param_dict['q'][0]  
            q = q.strip().split(';') 
        except:
            q = ['']
    else: 
        q = ['']  

    query = query_logic(q)
    draw = request.form.get('draw')
    start =  request.form.get('start')
    length = request.form.get('length')    
    draw = int(draw)
    start = int(start)
    length = int(length)  

    print('draw:{}  start:{}  length:{}  '.format(draw,start,length))

    recordsTotal = mongo.coll.count()  
    recordsFiltered = mongo.coll.find(query).count() 
    data = mongo.coll.find(query,projection={'_id':False}).sort([('ip',1),('port',1)]).skip(start).limit(length)    
    dd = []
    for d in data:  
        tmp = [] 
        tmp.append(d['ip']) 
        tmp.append(d['port']) 
        tmp.append(d['date']) 
        tmp.append(d['banner'][:100])
        dd.append(tmp)


    result = {
        'draw':draw,
        'recordsTotal':recordsTotal,
        'recordsFiltered':recordsFiltered,
        'data':dd
    } 

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
