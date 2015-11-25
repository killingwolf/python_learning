#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 20:49:57
# @Author  : killingwolf (killingwolf@qq.com)


def count_ip_func(f):
    with open(f, 'r') as rfd:
        for i in set([line.split()[0] for line in rfd]):
            print i


def count_ip_gen(f):
    with open(f, 'r') as rfd:
        ip = set()
        for i in (line.split()[0] for line in rfd):
            ip.add(i)
        for i in ip:
            print i


if __name__ == '__main__':
    f = 'ip.txt'
    # count_ip_func(f)
    count_ip_gen(f)
