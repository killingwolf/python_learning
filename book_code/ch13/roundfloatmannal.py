#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-04 11:49:07
# @Author  : killingwolf (killingwolf@qq.com)


class RoundFloatManual(object):

    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a fload!'
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)

    __repr__ = __str__

if __name__ == '__main__':
    print RoundFloatManual(1.245)
