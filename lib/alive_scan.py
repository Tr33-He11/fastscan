#!/usr/bin/env python
# coding=utf-8   
import asyncio  
import aiohttp 
import async_timeout 
from scapy.all import *   
import logging 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) 

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
    ans = sr1(IP(dst=ip,ttl=255)/ICMP(),timeout=2,verbose=False) 
    if ans and ans[ICMP].type == 0:  
        return ip 

async def alive_scan(ip):
    ports = [80,3389,22,3306,443,21]
    alive = 0
    for port in ports: 
        if alive:
            break 
        try:
            async with asyncio.Semaphore(3000):
                connection = asyncio.open_connection(ip,port)
                reader,writer = await asyncio.wait_for(connection,timeout=1)
        except Exception as e:    
            continue 
        else:
            alive = 1 
    if alive:
        return ip
