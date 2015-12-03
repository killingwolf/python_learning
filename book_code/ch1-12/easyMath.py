#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
"This is a easyMath module"

from operator import add, sub
from random import choice, randint


def doprob():
    "ddddd"
    opdict = {'+': add, '-': sub}
    op = choice("+-")
    number = [randint(1, 10) for i in range(2)]
    number.sort(reverse=True)
    result = opdict[op](*number)
    # return result
    prt = "Please input %s %s %s = " % (
        number[1], op, number[0]
    )
    while True:
        if int(raw_input(prt)) == result:
            print "You got it "
            break
        else:
            break

if __name__ == '__main__':
    print doprob()
