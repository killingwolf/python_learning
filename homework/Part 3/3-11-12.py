#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 11:58:40
# @Author  : killingwolf (killingwolf@qq.com)

import time


def dec_time(f):
    def wrapper(*args, **kargs):
        t1 = time.time()
        f(*args, **kargs)
        t2 = time.time()
        print "Running Time : %f seconds" % (t2 - t1)
    return wrapper


def timeit(func, *args, **kargs):
    t1 = time.time()
    func(*args, **kargs)
    t2 = time.time()

    return "Running Time : %f seconds" % (t2 - t1)


@dec_time
def test(*args, **kargs):
    """ Show function running time with decorator """
    print "This is in test functinon"
    time.sleep(5)


def test2(*args, **kargs):
    """ Show function running time with passing functions """
    print "This is in test2 functinon"
    time.sleep(5)

if __name__ == '__main__':
    test()
    print timeit(test2)
