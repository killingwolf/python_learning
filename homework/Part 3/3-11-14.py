#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 19:00:59
# @Author  : killingwolf (killingwolf@qq.com)


def fibonacci(n):
    if n <= 2:
        rt = 1
    else:
        rt = fibonacci(n - 1) + fibonacci(n - 2)

    return rt

if __name__ == '__main__':
    print fibonacci(10)
