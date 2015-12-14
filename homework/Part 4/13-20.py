#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:08:06
# @Author  : killingwolf (killingwolf@qq.com)


class Time60(object):

    HOUR = 24
    MIN = 60

    def __init__(self, *args):
        if len(args) == 2:
            if isinstance(args[0],  int) and isinstance(args[1], int):
                self.hour = args[0]
                self.min = args[1]
            else:
                raise (IOError, "args error")
        elif len(args) == 1:
            if isinstance(args[0], tuple):
                self.hour = args[0][0]
                self.min = args[0][1]
            elif isinstance(args[0], dict):
                self.hour = args[0]['hr']
                self.min = args[0]['min']
            elif isinstance(args[0], str):
                self.hour = int(args[0].split(':')[0])
                self.min = int(args[0].split(':')[1])
            else:
                raise (IOError, "args error")
        elif len(args) == 0:
            self.hour = 0
            self.min = 0
        else:
            raise (IOError, "Too many args")

    def __str__(self):
        return "%02d:%02d" % (self.hour, self.min)

    def __add__(self, other):
        self.hour += other.hour
        self.min += other.min
        mh = self.min / self.MIN
        m = self.min % self.MIN
        if mh or m:
            self.hour += mh
            self.min = m

        self.hour %= self.HOUR
        return self

    def __repr__(self):
        return repr("%02d:%02d" % (self.hour, self.min))

    __iadd__ = __add__


if __name__ == '__main__':
    t0 = Time60()
    # t0 = Time60((1, 2))
    # t0 = Time60({'hr': 1, 'min': 2})
    # t0 = Time60("1:2")
    t1 = Time60(11, 59)
    t2 = Time60(9, 2)
    print t1
    print t2
    t1 += t2
    # print t1
    print t1 + t2
