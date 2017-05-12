#!/usr/bin/env python
# coding=utf-8
def save_result(results):
    with open('port_scan_result','w') as f:
        for result in results:
            f.write('Host: {}  Port: {}   Banner: {}\n'.format(result[0],result[1],result[2]))

