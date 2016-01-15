#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/13 17:31
# @Author  : killingwolf (killingwolf@qq.com)
"""
socket 编程
"""
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('dir')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
