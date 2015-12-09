#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-04 15:43:56
# @Author  : killingwolf (killingwolf@qq.com)


class NumStr(object):

    'A class used to string and number operation'

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d::%s]' % (self.__num, self.__string)

    def __add__(self, other):
        return "[%d::%s]" % ((self.__num + other.__num),
                             (self.__string + other.__string))

    def __mul__(self, num):
        return self.__class__(self.__num * num, self.__string * num)

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval__(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval__(cmp(self.__num, other.__num)) + \
            self.__norm_cval__(
                cmp(self.__string, other.__string)
            )


if __name__ == '__main__':
    ns1 = NumStr(1, 'a')
    ns2 = NumStr(2, 'b')
    print ns1
