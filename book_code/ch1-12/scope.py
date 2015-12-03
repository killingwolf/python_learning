#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" 变量和名字空间
"""

if __name__ == '__main__':
    j, k = 1, 2

    def proc1():
        j, k = 3, 4
        print "j == %d and k == %d" % (j, k)
        k = 5

    def proc2():
        j = 6
        proc1()
        print "j == %d and k == %d" % (j, k)
        j = 8
    proc2()
    print "j == %d and k == %d" % (j, k)
