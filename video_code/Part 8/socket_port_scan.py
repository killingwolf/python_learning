#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/13 22:02
# @Author  : killingwolf (killingwolf@qq.com)
"""
使用socket进行端口扫描
"""
import socket
import time


def port_scan(ip, minport=1, maxport=1024):
    socket.setdefaulttimeout(0.2)
    remote_ip = ip
    start = time.time()
    try:
        for port in xrange(minport, maxport+1):
            skt = socket.socket()
            rst = skt.connect_ex((remote_ip, port))
            if rst == 0:
                print('Port :%d on ip: %s is open' % (port, ip))
            skt.close()
    except Exception as e:
        print e
    end = time.time()
    print 'All Port scanned in %f' % (end-start)

if __name__ == '__main__':
    server = 'www.baidu.com'
    ip = socket.gethostbyname(server)
    port_scan(ip)




