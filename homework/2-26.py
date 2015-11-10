#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
import random

# length of set A.
lengtha = random.randrange(1, 11)
# length of set B.
lengthb = random.randrange(1, 11)


def generate_set(length):
    """Generate a set"""
    tmp_set = set()
    while length > 0:
        tmp_set.add(random.randrange(1, 10))
        length -= 1
    return tmp_set


if __name__ == '__main__':
    seta = generate_set(lengtha)
    setb = generate_set(lengthb)
    print "A|B is : \n\t%s" % (seta | setb)
    print "A&B is : \n\t%s" % (seta & setb)
