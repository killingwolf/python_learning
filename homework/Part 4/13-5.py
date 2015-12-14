#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 00:06:04
# @Author  : killingwolf (killingwolf@qq.com)


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    __repr__ = __str__


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(1, 2)
    print p1
    print p2
