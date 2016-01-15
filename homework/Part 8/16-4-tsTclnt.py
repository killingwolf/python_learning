#!/usr/bin/env python

from socket import *


def tcp_clt(host='localhost', port=21567, bufsiz=1024):
    addr = (host, port)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(addr)
    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(bufsiz)
        if not data:
            break
        print data
    tcpCliSock.close()

if __name__ == '__main__':
    try:
        host = '127.0.0.1'
        port = 80
        tcp_clt(host, port)
    except Exception as e:
        print e