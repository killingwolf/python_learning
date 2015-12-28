#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 10:46:44
# @Author  : killingwolf (killingwolf@qq.com)


def my_open(fname, mode):
    try:
        return open(fname, mode)
    except BaseException:
        return None

if __name__ == '__main__':
    # open an exist file
    print my_open('10-6.py', 'r')
    # open an not exist file
    print my_open('xxxx', 'r')
