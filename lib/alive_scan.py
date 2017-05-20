#!/usr/bin/env python
# coding=utf-8   
import asyncio 
from scapy.all import *  
import pdb

def arp_ping(ip,iface):
    try:
        iface = iface 
        pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip,op=1)
        ans,unans = srp(pkt,iface=iface,timeout=1,verbose=False)

        if len(ans) > 0:
            return ip 

    except Exception as e:
        print('arp_ping error:{} args:{} {}'.format(ip,iface,e))

def icmp_ping(ip):
    ans,unans = sr(IP(dst=ip)/ICMP(),timeout=2,verbose=False)

    if len(ans) > 0:
        return ip
