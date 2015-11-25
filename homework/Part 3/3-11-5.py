#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 23:23:46
# @Author  : killingwolf (killingwolf@qq.com)


def business_tax(turnover, rate=0.1):
    try:
        return turnover * rate
    except BaseException, e:
        return e

if __name__ == '__main__':
    print business_tax(100)
