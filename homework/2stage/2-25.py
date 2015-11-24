#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
import random

# How lenth the list will be generated.
length = random.randrange(2, 101)
# How many object will be selected from the generated list.
number = random.randint(1, 100)


def generate_list(length):
    """Generate a list"""
    tmp_list = []
    while length > 0:
        tmp_list.append(random.randint(1, 2**31 - 1))
        length -= 1
    return tmp_list


def get_value_from_list(number, list):
    """Get value from list"""
    tmp_list = []
    while number > 0:
        tmp_list.append(random.choice(list))
        number -= 1
    tmp_list.sort()
    return tmp_list


if __name__ == '__main__':
    glist = generate_list(length)
    slist = get_value_from_list(number, glist)
    print slist
