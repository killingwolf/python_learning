#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 23:06:41
# @Author  : killingwolf (killingwolf@qq.com)


def minutes_to_hour(minutes):
    if isinstance(minutes, int):
        return "%dH:%dM" % (minutes / 60, minutes % 60)
    else:
        return "Please Input an int"

if __name__ == '__main__':
    print minutes_to_hour(400)
