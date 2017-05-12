#!/usr/bin/env python
# coding=utf-8
def get_ip_list(ip_range):
    ip2num = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
    num2ip = lambda x: '.'.join([str(x // (256 ** i) % 256) for i in range(3, -1, -1)])  
    if '/' in ip_range:
        try:
            with open(ip_range) as f:
                for ip in f:
                    yield ip.strip()
        except Exception as e:
            print('ip file error')

    elif '-' in ip_range:
        ip_split = ip_range.split('-')
        ip_start = ip2num(ip_split[0])
        ip_end = ip2num(ip_split[1]) 
        ip_count = ip_end - ip_start 

        if ip_count >= 0 and ip_count <= 65535:
            for i in range(ip_start,ip_end+1):
                yield num2ip(i)
        else:
            print('IP format error')  

