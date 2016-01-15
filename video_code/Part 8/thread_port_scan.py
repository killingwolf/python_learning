#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 19:49
# @Author  : killingwolf (killingwolf@qq.com)
"""
多线程端口扫描
"""
import sys
import Queue
import socket
import threading

class PortScan(threading.Thread):
    def __init__(self, ips):
        self.ips = ips
        super(self.__class__, self).__init__()

    def run(self):
        while True:
            ip = self.ips.get()
            self.scan_ip(ip)
            self.ips.task_done()

    def scan_ip(self, ip, minport=1, maxport=1024, timeout=0.1):
        socket.setdefaulttimeout(timeout)
        try:
            for port in xrange(minport, maxport+1):
                skt = socket.socket()
                rst = skt.connect_ex((ip, port))
                if rst == 0:
                    print('Port :%d on ip: %s is open' % (port, ip))
                skt.close()
        except Exception as e:
            print e
            sys.exit()

if __name__ == '__main__':
    ip_queue = Queue.Queue()
    ips = ['222.73.243.132',
           '210.51.35.107',
           '222.73.196.30'
           ]
    for ip in ips:
        ip_queue.put(ip)

    for i in xrange(6):
        t = PortScan(ip_queue)
        t.setDaemon(True)
        t.start()
    ip_queue.join()

