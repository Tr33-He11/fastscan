#!/usr/bin/env python
# coding=utf-8  
from scapy.all import * 

def arp_ping(ip,iface):
    iface = iface 
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip,op=1)
    ans,unans = srp(pkt,iface=iface,timeout=1,verbose=False)

    if len(ans) > 0:
        return ip  

def icmp_ping(ip):
    ans,unans = sr(IP(dst=ip)/ICMP(),timeout=2,verbose=False)

    if len(ans) > 0:
        return ip

