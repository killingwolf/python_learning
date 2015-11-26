#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 17:24:23
# @Author  : killingwolf (killingwolf@qq.com)
""" Functional Programming with reduce() and Recursion.
"""

import time
import sys
sys.setrecursionlimit(1000000000)


def timeit(func, *args, **kargs):
    t1 = time.time()
    func(*args, **kargs)
    t2 = time.time()

    return "Running Time : %f seconds" % (t2 - t1)


def mult(x, y):
    if (isinstance(x, int) or isinstance(x, long)) and \
            (isinstance(y, int)or isinstance(y, long)):
        rt = x * y
    else:
        rt = "You must input int numbers"
    return rt


def factorials_v1(x):
    if isinstance(x, int):
        if x > 1:
            rt = reduce(mult, range(1, x + 1))
        else:
            rt = 1
    else:
        rt = "You must input an int number"

    return rt


def factorials_v2(x):
    if isinstance(x, int):
        if x > 1:
            rt = reduce(lambda x, y: x * y, range(1, x + 1))
        else:
            rt = 1
    else:
        rt = "You must input an int number"

    return rt


def factorials_v3(x):
    if isinstance(x, int) or isinstance(x, long):
        if x > 1:
            rt = x * factorials_v3(x - 1)
        else:
            rt = 1
    else:
        rt = "You must input an int number"

    return rt


if __name__ == '__main__':
    # print mult(11, 11)
    number = 5000
    # print factorials_v1(number)
    # print factorials_v2(number)
    # print factorials_v3(number)
    print timeit(factorials_v1, number)
    print timeit(factorials_v2, number)
    print timeit(factorials_v3, number)
