#!/usr/bin/env python
# coding=utf-8 
import aiohttp 
import asyncio  
import async_timeout 
import pdb

async def scan_port(ip,port):
    try:
        async with asyncio.Semaphore(1000):
            connection = asyncio.open_connection(ip,port)
            reader,writer = await asyncio.wait_for(connection,timeout=1)
    except Exception as e:
        return 
   
    banner = ''
    try:
        if port != 443:
            with async_timeout.timeout(0.5):
                HEAD = 'GET / HTTP/1.1\nHOST: {}:{}\n\n'.format(ip,port)
                writer.write(HEAD.encode('utf-8'))
                await writer.drain() 
                banner = await reader.read(1024) 
                writer.close() 
                banner = banner.decode('utf-8')
                banner = banner.replace('\r\n',' ').strip() 
        else:
            writer.close()  
            url = 'https://{}'.format(ip)
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.ClientSession(connector=conn) as session:
                with async_timeout.timeout(1):
                    async with session.get(url) as response:
                        headers = response.headers
                        banner = 'HTTP/1.1' 
                        for i,j in headers.items():
                            banner = '{} {}: {} '.format(banner,i,j)
                            
    except Exception as e: 
        banner = ''
    
    return [ip,port,banner]

