#!/usr/bin/env python
# coding=utf-8     
import concurrent.futures 
import pdb
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
    ports = [80,443]
    alive = 0  
    for port in ports: 
        try:
            async with asyncio.Semaphore(2000): 
                connection = asyncio.open_connection(ip,port) 
                reader,writer = await asyncio.wait_for(connection,timeout=1)
        except ConnectionRefusedError as e:     
            alive = 1   
        except Exception as e: 
            pass
#            print('an unexpected error: {}'.format(e))  
        else:
            writer.close()
            alive = 1  
        finally:
            if alive:
                break 
    if alive:
        return ip 

if __name__ == '__main__':  
    ip_base = '172.22.254.{}' 
    loop = asyncio.get_event_loop()  
    tasks = [asyncio.ensure_future(alive_scan(ip_base.format(i))) for i in range(1,2) ]
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        if task.result():
            print(task.result()+' UP')
#     results = []
#         ip = ip_base.format(i)
#         result = icmp_ping(ip)
#         if result:
#            results.append(result)  
#     print('共发现{}台存活主机'.format(len(results)))
