#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 15:41:00
# @Author  : killingwolf (killingwolf@qq.com)


if __name__ == '__main__':
    # import os
    os = __import__('os')
    print os.listdir('.')
    # from os import listdir
    listdir = __import__('os', 'listdir').listdir
    print listdir('.')
