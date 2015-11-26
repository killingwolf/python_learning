#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 11:50:19
# @Author  : killingwolf (killingwolf@qq.com)


def average(list):
    # func = lambda x, y: (x + y) / 2.0
    return reduce(lambda x, y: (x + y) / 2.0, list)

if __name__ == '__main__':
    List = [1, 2, 3]
    print average(List)
