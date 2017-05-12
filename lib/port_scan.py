#!/usr/bin/env python
# coding=utf-8
import asyncio  
import async_timeout

async def scan_port(ip,port):
    try:
        async with asyncio.Semaphore(1000):
            connection = asyncio.open_connection(ip,port)
            reader,writer = await asyncio.wait_for(connection,timeout=0.5)
    except Exception as e:
        return 
   
    banner = ''
    try:
        with async_timeout.timeout(0.2):
            HEAD = 'HEAD / HTTP/1.1\nHOST: {}:{}\n\n'.format(ip,port)
            writer.write(HEAD.encode('utf-8'))
            await writer.drain() 
            banner = await reader.read(1024) 
            writer.close() 
            banner = banner.decode('utf-8')
            banner = banner.replace('\r\n',' ').strip()
    except Exception as e:
        banner = ''
    
    return [ip,port,banner]

