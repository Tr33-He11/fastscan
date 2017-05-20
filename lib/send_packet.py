#!/usr/bin/env python
# coding=utf-8
import asyncio
from scapy.all import * 

async def send_packet(ip,port):
    packet = IP(dst=ip)/TCP(dport=port,flags=2)
    await send(packet,verbose=False) 
    return '{}:{} 发送成功'.format(ip,port)

if __name__=='__main__':
    ip = '10.42.0.254'
    port = 80
    send_packet(ip,port)
