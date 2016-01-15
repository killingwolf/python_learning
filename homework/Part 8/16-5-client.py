#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 16:52
# @Author  : killingwolf (killingwolf@qq.com)

import socket

def client(host='127.0.0.1', port=50007, commands=[]):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        for cmd in commands:
            s.sendall(cmd)
            data = s.recv(1024)
            print 'Received', repr(data)
        s.close()
    except Exception as e:
        print e
        s.close()


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    commands = ['date', 'ls', 'xxx oooo dddd', 'bbbb cccc']
    client(ip, port, commands)
