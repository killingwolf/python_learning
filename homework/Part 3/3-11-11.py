#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 11:58:40
# @Author  : killingwolf (killingwolf@qq.com)


def map_remove_whitespace(srcfile, dstfile):
    """Remove whitespace with map and lambda"""
    with open(srcfile, 'r') as rfd, open(dstfile, 'w') as wfd:
        wfd.writelines(map(lambda x: x.strip() + '\n', rfd))


def remove_whitespace(srcfile, dstfile):
    """Remove whitespace with list comprehensions"""
    with open(srcfile, 'r') as rfd, open(dstfile, 'w') as wfd:
        wfd.writelines([line.strip() + '\n' for line in rfd])

if __name__ == '__main__':
    srcfile = 'abc.txt'
    dstfile = 'abc.strip.txt'
    try:
        map_remove_whitespace(srcfile, dstfile)
        remove_whitespace(srcfile, dstfile)
    except BaseException, e:
        print e
