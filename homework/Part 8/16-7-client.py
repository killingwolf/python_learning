#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 18:59
# @Author  : killingwolf (killingwolf@qq.com)
"""
半双工聊天客户端
"""
import socket


def client(host='127.0.0.1', port=50007):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        while True:
            msg = raw_input('>')
            s.sendall(msg)
            data = s.recv(1024)
            print 'Received from server', repr(data)
        s.close()
    except Exception as e:
        print e
        s.close()


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    client(ip, port)

