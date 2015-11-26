#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-26 11:19:18
# @Author  : killingwolf (killingwolf@qq.com)


def is_leap_year(year):
    if (not year % 4 and year % 100) or not year % 400:
        return year


def filter_leap_year(years):
    # ffunc = lambda year: (not year % 4 and year % 100) or not year % 400
    return filter(is_leap_year, years)

if __name__ == '__main__':
    years = [100, 300, 2000]
    print filter_leap_year(years)
    print [year for year in years
           if (not year % 4 and year % 100) or not year % 400]
