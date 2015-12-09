#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-04 11:51:47
# @Author  : killingwolf (killingwolf@qq.com)


class Time60(object):

    def __init__(self, hr, min):
        self.hour = hr
        self.min = min

    def __str__(self):
        return "%d:%d" % (self.hour, self.min)

    def __add__(self, other):
        return self.__class__(self.hour + other.hour, self.min + other.min)

    __repr__ = __str__

    def __iadd__(self, other):
        self.hour += other.hour
        self.min += other.min
        return self
if __name__ == '__main__':
    t1 = Time60(11, 20)
    t2 = Time60(13, 40)
    t1 += t2
    print t1
