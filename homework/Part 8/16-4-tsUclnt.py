#!/usr/bin/env python

from socket import *


def udp_clt(host='localhost', port=21567, bufsiz=1024):
    addr = (host, port)
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = raw_input('> ')
        if not data:
            break
        udpCliSock.sendto(data, addr)
        data, addr = udpCliSock.recvfrom(bufsiz)
        if not data:
            break
        print data
    udpCliSock.close()

if __name__ == '__main__':
    try:
        host = '127.0.0.1'
        port = 80
        udp_clt(host, port)
    except Exception as e:
        print e