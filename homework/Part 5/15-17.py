#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-23 23:50:19
# @Author  : killingwolf (killingwolf@qq.com)
import re


def week_count(datafile):
    pt = r'\b(Wed|Tue|Mon|Sun|Sat|Fri|Thu)\b'
    count = {}
    with open(datafile, 'r') as rfd:
        for i in rfd:
            match = re.findall(pt, i)
            if match:
                for i in match:
                    if i in count:
                        count[i] += 1
                    else:
                        count[i] = 1
    return count

if __name__ == '__main__':
    data = 'redata.txt'
    # data = 'rxedata.txt'
    try:
        count = week_count(data)
        for k in count:
            print k, count[k]
    except Exception as e:
        print e
