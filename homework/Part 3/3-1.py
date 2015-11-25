#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def find_median(L):
    if L:
        L.sort()
        if len(L) % 2:
            value = L[len(L) / 2]
        else:
            value = (L[len(L) / 2 - 1] + L[len(L) / 2]) / 2
        return value
    else:
        raise ValueError

if __name__ == '__main__':
    L = [15.0, 5.3, 18.2]
    print find_median(L)
    L = [1.0, 2.0, 3.0, 4.0]
    print find_median(L)
    L = []
    print find_median(L)
