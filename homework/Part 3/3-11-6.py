#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 23:31:12
# @Author  : killingwolf (killingwolf@qq.com)


def printf(fstring, *args):
    return [(fstring % arg) for arg in args]


if __name__ == '__main__':
    fsting = '%s'
    str1 = 'xxxx'
    str2 = 1234
    for i in printf(fsting, str1, str2):
        print i
