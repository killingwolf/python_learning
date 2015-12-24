#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-23 18:45:19
# @Author  : killingwolf (killingwolf@qq.com)

import re


def format_type(cls):
    return re.search(r'.*\'(.*)\'.*', str(type(cls))).group(1)

if __name__ == '__main__':
    print format_type(int)
