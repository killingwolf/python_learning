#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 12:19:23
# @Author  : killingwolf (killingwolf@qq.com)


def safe_input():
    try:
        return raw_input("Please input something:")
    except (EOFError, KeyboardInterrupt):
        return None


if __name__ == '__main__':
    print safe_input()
