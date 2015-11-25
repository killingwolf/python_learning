#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 21:30:01
# @Author  : killingwolf (killingwolf@qq.com)


def countToFour1():
    for eachNum in range(5):
        print eachNum,


def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum,


def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum,

if __name__ == '__main__':
    print "Input countToFour1 countToFour2 countTofour3"
    for i in 2, 4, 5:
        print i,
        try:
            print countToFour1(i),
        except BaseException, e:
            print 'ERROR',
        print '(',
        countToFour2(i),
        print ')',
        print '(',
        countToFour3(i)
        print ')',
        print
