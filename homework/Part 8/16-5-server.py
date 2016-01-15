#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 16:52
# @Author  : killingwolf (killingwolf@qq.com)
import socket
import os
import sys


def server(host='127.0.0.1', port=50007, commands=[]):
    addr = (host, port)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(addr)
        s.listen(5)
        while True:
            print 'waiting for connect'
            conn, addr = s.accept()
            print 'Connected by', addr
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                cmd = data.split()
                if len(cmd) == 2:
                    cmd, arg = cmd[0], cmd[1]
                elif len(cmd) == 1:
                    cmd = cmd[0]
                else:
                    cmd = None
                if cmd and cmd in commands:
                    d = os.popen(data).read()
                    conn.sendall(d)
                else:
                    conn.sendall('unspportted command')
            conn.close()
        s.close()
    except Exception as e:
        print e
        s.close()
        sys.exit()
if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    commands = ['date', 'ls']
    server(ip, port, commands)