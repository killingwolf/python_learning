#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 15:53:12
# @Author  : killingwolf (killingwolf@qq.com)


def import_as(mname):
    try:
        rt = __import__(mname)
    except BaseException, e:
        rt = e

    return rt

if __name__ == '__main__':
    nname = import_as('os')
    print nname.listdir('.')
