#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-04 12:14:51
# @Author  : killingwolf (killingwolf@qq.com)

from random import choice


class RandSeq(object):

    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)

    # def __str__(self):
    #     return str(choice(self.data))

if __name__ == '__main__':
    rs = RandSeq('123')
    print iter(rs)
    print rs.next()
    print rs.next()
    print rs.next()
    print rs.next()
    print rs.next()
