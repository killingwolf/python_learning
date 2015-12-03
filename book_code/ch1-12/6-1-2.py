#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com

"Remove last object each time"

if __name__ == '__main__':
    l = range(1, 10)
    for i in [None] + range(-1, -len(l), -1):
        print l[:i]
    print '###' * len(l)
    while l:
        a = l.pop()
        if l:
            print l
