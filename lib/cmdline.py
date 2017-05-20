#!/usr/bin/env python
# coding=utf-8 
import argparse   
import pdb 

def cmd_parse():
    parser = argparse.ArgumentParser(description='User information') 

    parser.add_argument('-s','--speed',dest='speed',action='store',choices=['low','medium','high'],help='scan speed',default=['medium'])
    parser.add_argument('-o','--output',dest='output',action='store',help='the port  or the service  you want to output',default=[]) 
    parser.add_argument('-p','--port',dest='port',action='store',help='the port wait for scan default are top 1000 ports',default=[])    
    parser.add_argument('-i','--iface',dest='iface',action='store',help='the network interface',default=[])
    parser.add_argument('ip')

    args = parser.parse_args() 

    if not any(args.__dict__.values()):
        parser.print_help() 
        raise SystemExit 

    return args 



if __name__=='__main__':
    args = cmd_parse()  
    pdb.set_trace() 
    print(args)
