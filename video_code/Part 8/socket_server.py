#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/13 17:31
# @Author  : killingwolf (killingwolf@qq.com)
"""
socket 编程
"""
import socket
import os

HOST = '127.0.0.1'                 # Symbolic name meaning all available
# interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    print 'waiting for connect'
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        d = os.popen(data).read()
        conn.sendall(d)
    conn.close()
