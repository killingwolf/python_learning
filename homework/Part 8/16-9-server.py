#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 18:59
# @Author  : killingwolf (killingwolf@qq.com)
"""
多用户全双工聊天 服务端
"""
import socket
import select
import sys

class ChatRoom(object):
    def __init__(self, id):
        self.id = id

class User(object):
    def __init__(self, name, room):
        self.name = name

def server(host='127.0.0.1', port=50007, maxconnection=10):
    addr = (host, port)
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(addr)
        server_socket.listen(maxconnection)
        inputs = [server_socket]
        clients = []
        while True:
            print 'waiting for connect'
            ipt, opt, xpt = select.select(inputs, clients, [])
            print '...connected from:', addr
            for i in ipt:
                if i is server_socket:
                    client_socket, addr = server_socket.accept()
                    client_socket.setblocking(0)
                    inputs.append(client_socket)
                else:
                    data = i.recv(1024)
                    if data:
                        print 'Recived from client: %s' % msg
                        if i not in clients:
                            clients.append(i)
                    else:
                        clients.remove(i)
                        i.close()
            for clt in opt:
                msg = clt.recv(1024)
                if not msg:
                    break
                print 'Recived from client: %s' % msg
                msg = raw_input('>')
                if not msg:
                    break
                clt.sendall(msg)
        server_socket.close()
    except Exception as e:
        print e
        server_socket.close()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 11111
    server(ip, port)
