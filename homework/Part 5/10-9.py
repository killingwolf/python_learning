#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 12:21:23
# @Author  : killingwolf (killingwolf@qq.com)

from math import sqrt


def safe_sqrt(number):
    try:
        return sqrt(number)
    except ValueError:
        return '±%di' % sqrt(abs(number))
    except BaseException, e:
        return e

if __name__ == '__main__':
    print safe_sqrt(4)
    print safe_sqrt(-4)
    print safe_sqrt('x')
