#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/14 18:48
# @Author  : killingwolf (killingwolf@qq.com)

import socket

if __name__ == '__main__':
    service = 'daytime'
    protocol = 'udp'
    print socket.getservbyname(service, protocol)
