#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 14:32:08
# @Author  : killingwolf (killingwolf@qq.com)


class ShortInputException(Exception):

    """A customer excetpion"""

    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


if __name__ == '__main__':
    try:
        raise ShortInputException(10, 2)
    except ShortInputException as e:
        print e.length, e.atleast
