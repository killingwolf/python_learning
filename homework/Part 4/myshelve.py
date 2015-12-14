#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-12 14:56:14
# @Author  : killingwolf (killingwolf@qq.com)
import shelve

# d = shelve.open('test.txt')
# d['abc'] = ['password','time']
if __name__ == '__main__':
    d = shelve.open('test.txt')
    # d['abc'] = ['password', 'time']
    # d.close
    print d.keys()
