#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" random 9 number from 1 to 99 , reture even number
"""

from random import randint


def even_num_v1():
    "even number v1"
    rand_list = []
    even_list = []
    for i in range(9):
        rand_list.append(randint(1, 99))

    for i in rand_list:
        if not i % 2:
            even_list.append(i)

    return even_list


def even_num_v2():
    "even number v2"
    rand_list = [randint(1, 99) for i in range(9)]
    even_func = lambda x: x % 2
    return filter(even_func, rand_list)


def even_num_v3():
    "even number v3"
    return [n for n in [randint(1, 99)
                        for i in range(9)] if n % 2]


if __name__ == '__main__':
    # print even_num_v1()
    # print even_num_v2()
    print even_num_v3()
