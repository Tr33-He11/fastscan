#!/usr/bin/env python
# coding=utf-8  
from pymongo import MongoClient     
from datetime import datetime 
import sys
import socket 
import re
import pdb   

def ip2hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname 
    except: 
        return ''

def web_info(result):  
    conn = MongoClient('localhost',27017) 
    db = conn.fastscan
    pattern = r'([^<]+)(<!DOCTYPE[\d\D]+|<HTML[\d\D]+)?'
    tmp = re.search(pattern,result["banner"],re.I | re.M) 
    header = tmp.group(1)
    html = tmp.group(2)
    if not html:
        html = '' 
        title = ''
    else:
        title = re.search(r'<title>(.+)</title>',html,re.I | re.M)  
        if not title:
            title = '' 
        else:
            title = title.group(1).strip()

    server = re.search(r'server:([\s]*)([^:]+\s)([^\s]+:)?',header,re.I | re.M) 
    if not server:
        server = '' 
    else:
        server = server.group(2).strip()
    
    ip = result['ip'] 
    port = result['port']  
    domain = ip2hostname(ip)
    date = str(datetime.now()).split('.')[0] 
    db.web.update({'ip':ip,'port':port},{'$set':{'domain':domain,'date':date,'header':header,'title':title,'server':server}},upsert=True,multi=True)  
    conn.close()


def save_port(data,port):
    with open('{}.txt'.format(port),'a+') as f:
        for i in data:
            if port == 'http':
                if i['banner'].find('HTTP') != -1:
                    f.write('{}:{}\n'.format(i['ip'],i['port']))
            else:
                port = int(port)
                if i['port'] == port:
                    f.write('{}:{}\n'.format(i['ip'],i['port'])) 


def save_result(results):
    with open('results.txt','a+') as f:
        for result in results:
            f.write('Host: {}  Port: {}  Banner: {}\n'.format(result['ip'],result['port'],result['banner'])) 

def save2mongodb(results):
    conn = MongoClient('localhost',27017)
    db = conn.fastscan
    db.host.update({'ip':results['ip'],'port':results['port']},{'$set':{'banner':results['banner'],'date':results['date']}},upsert=True,multi=True)
    conn.close() 
