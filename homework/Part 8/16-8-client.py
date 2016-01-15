#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 18:59
# @Author  : killingwolf (killingwolf@qq.com)
"""
全双工聊天客户端
"""
import socket
import select
import sys


def client(host='127.0.0.1', port=50007):
    addr = (host, port)
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        inputs = [client_socket, sys.stdin]
        while True:
            ipt, opt, xpt = select.select(inputs, [], [])
            for i in ipt:
                if i is client_socket:
                    msg = i.recv(1024)
                    if not msg:
                        break
                    print 'Recived from Server: %s' % msg
                else:
                    msg = raw_input('>')
                    client_socket.sendall(msg)
        client_socket.close()
    except Exception as e:
        print e
        client_socket.close()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    client(ip, port)
