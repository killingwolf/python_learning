#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-04 13:55:23
# @Author  : killingwolf (killingwolf@qq.com)


class AnyIter(object):

    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

if __name__ == '__main__':
    ai = AnyIter(range(10), 1)
    i = iter(ai)
    print i.next(15)
