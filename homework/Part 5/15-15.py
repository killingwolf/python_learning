#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-23 19:43:46
# @Author  : killingwolf (killingwolf@qq.com)
import re


class CreditCard(object):

    """A class to validate the creditcard id

    Attributes:
        number: creditcard id
    """

    def __init__(self, number):
        self.number = number

    def isvalid(self):
        length = len(str(self.number))
        rt = False
        if length == 17:
            pt = r'^\d{4}-\d{6}-\d{5}$'
            sc = re.search(pt, str(self.number))
            if sc:
                rt = True
        elif length == 19:
            pt = r'^(\d{4}-){3}\d{4}$'
            sc = re.search(pt, str(self.number))
            if sc:
                rt = True
        else:
            rt = False
        return rt

if __name__ == '__main__':
    number = CreditCard("1111-111111-11111")
    print number.isvalid()
    number = CreditCard("1a11-1111-1111-1111")
    print number.isvalid()
    number = CreditCard("11111111")
    print number.isvalid()
