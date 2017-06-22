#!/usr/bin/env python
# coding=utf-8
from pymongo import MongoClient  

class MongoDB():
    def __init__(self,host='localhost',port=27017,database='fastscan',col='host',username='',password=''):
        self.host = host 
        self.port = port 
        self.database = database 
        self.conn = MongoClient(self.host,self.port) 
        self.db = self.conn[self.database] 
        if col == 'host':
            self.coll = self.db.host 
        elif col == 'web':
            self.coll = self.db.web
        try:
            self.coll.authenticate(username,password) 
        except:
            pass 


if __name__ == '__main__':
    mongo = MongoDB() 
    data = mongo.coll.find()
    for d in data:
        print(d) 
