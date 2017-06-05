#!/usr/bin/env python
# coding=utf-8  
from pymongo import MongoClient  
import pdb 

def save_port(data,port):
    with open('{}.txt'.format(port),'w') as f:
        for i in data:
            if port == 'http':
                if i['banner'].find('HTTP') != -1:
                    f.write('{}:{}\n'.format(i['ip'],i['port']))
            else:
                port = int(port)
                if i['port'] == port:
                    f.write('{}:{}\n'.format(i['ip'],i['port'])) 


def save_result(results):
    with open('results.txt','w') as f:
        for result in results:
            f.write('Host: {}  Port: {}  Banner: {}\n'.format(result['ip'],result['port'],result['banner'])) 

def save2mongodb(results):
    conn = MongoClient('localhost',27017)
    db = conn.banner 
    db.col.insert(results)
    conn.close() 
