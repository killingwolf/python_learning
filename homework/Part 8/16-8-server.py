#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 18:59
# @Author  : killingwolf (killingwolf@qq.com)
"""
全双工聊天服务端
"""
import socket
import select
import sys


def server(host='127.0.0.1', port=50007):
    addr = (host, port)
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(addr)
        server_socket.listen(5)
        inputs = [server_socket, sys.stdin]
        while True:
            print 'waiting for connect'
            client_socket, addr = server_socket.accept()
            print '...connected from:', addr
            inputs.append(client_socket)
            while True:
                ipt, opt, xpt = select.select(inputs, [], [])
                for i in ipt:
                    if i is server_socket:
                        msg = i.recv(1024)
                        if not msg:
                            break
                        print 'Recived from client: %s' % msg
                    else:
                        msg = raw_input('>')
                        if not msg:
                            break
                        client_socket.sendall(msg)
        server_socket.close()
    except Exception as e:
        print e
        server_socket.close()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    server(ip, port)
