#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a decorator test module
"""

from time import ctime, sleep


def tsfunc(func):
    def warppedFunc():
        print '[%s] %s() called' % (
            ctime(), func.__name__
        )
        return func()
    return warppedFunc


@tsfunc
def foo():
    print "%s() called" % __name__


foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
