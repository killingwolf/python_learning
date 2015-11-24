#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
from random import randint


def craps():
    sum1 = sum([randint(1, 6) for i in range(2)])
    result = None
    if sum1 in [7, 11]:
        result = "玩家赢"
    elif sum1 in [2, 3, 12]:
        result = "庄家赢"
    elif sum1 in [4, 5, 6, 8, 9, 10]:
        sum2 = sum([randint(1, 6) for i in range(2)])
        if sum2 == sum1:
            result = "玩家赢"
        elif sum2 == 7:
            result = "庄家赢"
        else:
            craps()
    else:
        craps()
    if result:
        return result
    else:
        return craps()
if __name__ == '__main__':
    print craps()
