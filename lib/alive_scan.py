#!/usr/bin/env python
# coding=utf-8  
from scapy.all import * 

def arp_ping(ip,iface='enp8s0'):
    iface = iface 
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip,op=1)
    ans,unans = srp(pkt,iface=iface,timeout=0.2,verbose=False)

    if len(ans) > 0:
        print(ip+' Up')
        return ip

