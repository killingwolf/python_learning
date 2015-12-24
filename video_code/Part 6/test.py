#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-16 14:22:41
# @Author  : killingwolf (killingwolf@qq.com)
"""
xxxx
"""
import sys
import re


a = 20


class Xx(object):
    # a = 10
    # print 'In clas xx', locals()
    # print '#' * 20
    # print globals()
    # print '#' * 20
    pass


def xx():
    a = 10
    print 'In xx', locals()
    print '#' * 20
    print a


if __name__ == '__main__':
    str = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w', str)
    # If-statement after search() tests if it succeeded
    if match:
        print 'found', match.group()  # 'found word:cat'
    else:
        print 'did not find'
