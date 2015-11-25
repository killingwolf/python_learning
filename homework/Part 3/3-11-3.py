#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 22:33:01
# @Author  : killingwolf (killingwolf@qq.com)


def max(a, b):
    return a if a > b else b


def min(a, b):
    return a if a < b else b


def my_max(a, *args):
    if isinstance(a, list):
        a.extend(args)
        return reduce(max, a)
    else:
        return "Please input a list"


def my_min(a, *args):
    if isinstance(a, list):
        a.extend(args)
        return reduce(min, a)
    else:
        return "Please input a list"

if __name__ == '__main__':
    print max(4, 8)
    print min(4, 8)
    print my_max([1], 4, 5, 6)
    print my_min([1], 4, 5, 6)
