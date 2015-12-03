#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 19:00:59
# @Author  : killingwolf (killingwolf@qq.com)

import time


def fibonacci(n):
    """ fibonacci with Recursion """
    if n <= 2:
        rt = 1
    else:
        rt = fibonacci(n - 1) + fibonacci(n - 2)

    return rt


def fabonacci_v2(n):
    """ fibonacci without Recursion """
    k = j = 1
    if n <= 2:
        rt = 1
    else:
        for i in xrange(n):
            if i == n - 1:
                rt = j
            j, k = k, k + j

    return rt


if __name__ == '__main__':
    # print fabonacci_v2(10)
    print fibonacci(5)
