#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 14:52:09
# @Author  : killingwolf (killingwolf@qq.com)


class HotelRoomCalc(object):

    'Hotel rome rate calculator'

    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments:
        sales tax = 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calc_total(self, days=1):
        'Calculate tool; default to daily rate'
        daily = round(
            (self.roomRate * (1 + self.roomTax + self.salesTax)), 2)

        return float(days) * daily

if __name__ == '__main__':
    ht = HotelRoomCalc(299)
    print ht.calc_total(2)
