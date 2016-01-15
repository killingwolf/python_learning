#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 15:16
# @Author  : killingwolf (killingwolf@qq.com)
import socket

if __name__ == '__main__':
    # creat a TCP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    print tcp_socket.getsockopt()
