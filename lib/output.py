#!/usr/bin/env python
# coding=utf-8  
from pymongo import MongoClient 

def save_port(data,port):
    with open('{}.txt'.format(port),'w') as f:
        for i in data:
            if port == 'http':
                if i[2].find('HTTP') != -1:
                    f.write('{}:{}\n'.format(i[0],i[1]))
            else:
                port = int(port)
                if i[1] == port:
                    f.write('{}:{}\n'.format(i[0],i[1])) 


def save_result(results):
    with open('results.txt','w') as f:
        for result in results:
            f.write('Host: {}  Port: {}  Banner: {}\n'.format(result['ip'],result['port'],result['banner'])) 

def save2mongodb(results):
    conn = MongoClient('localhost',27017)
    db = conn.banner 
    db.col.insert(results)
    conn.close() 
