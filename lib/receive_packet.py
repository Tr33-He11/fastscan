#!/usr/bin/env python
# coding=utf-8
from scapy.all import *  

def prn(pkt):
    ip = pkt[IP].src
    port = pkt[TCP].sport 
    return ip,port

def receive_packet(iface):
    sniff(iface=iface,lfilter=lambda x:x.haslayer(TCP) and x[IP].dst=='172.18.62.36' and x[TCP].flags==18,prn=prn) 

if __name__ == '__main__':
#    iface = 'wlp15s0'
    iface = 'enp8s0'
    receive_packet(iface)
