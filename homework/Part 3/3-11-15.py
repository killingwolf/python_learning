#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 19:15:50
# @Author  : killingwolf (killingwolf@qq.com)


def print_string():
    try:
        str1 = raw_input('Please in put a string:\n').strip('\n')
        lens = len(str1)
        if not lens:
            return False
        if lens == 1:
            print str1
            return True
        for i, j in enumerate(str1):
            if not i and lens != 1:
                print j, str1[i + 1]
            elif i == len(str1) - 1 and i:
                print str1[i - 1]
            else:
                print str1[i - 1], j, str1[i + 1]
        return True
    except BaseException, e:
        print e

if __name__ == '__main__':
    print_string()
