#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 23:48:30
# @Author  : killingwolf (killingwolf@qq.com)


def map_zip(l1, l2):
    return map(lambda x, y: (x, y), l1, l2)


def zip_zip(l1, l2):
    return zip(l1, l2)

if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = ['abc', 'def', 'ghi']
    print map_zip(l1, l2)
    print zip_zip(l1, l2)
