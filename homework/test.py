#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a hello world module
    dfadfadfa
"""

a = 10


def main():
    global a
    print "global a is :%s" % a
    a = 200
    print "local a is :%s" % a
    b = 300
    print "local b is :%s" % b


if __name__ == '__main__':
    a = 10
    b = 20
    main()
    print "####%s####" % a
    print "####%s####" % b
