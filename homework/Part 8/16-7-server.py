#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 18:59
# @Author  : killingwolf (killingwolf@qq.com)
"""
半双工聊天服务端
"""
import socket


def server(host='127.0.0.1', port=50007):
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
                print 'Received from client', data
                if not data:
                    continue
                msg = raw_input('>')
                conn.sendall(msg)
            conn.close()
        s.close()
    except Exception as e:
        print e
        s.close()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    server(ip, port)
