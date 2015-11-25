#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def tr(srcstr, dststr, string):
    """ python tr
    """
    if srcstr in string:
        string = string.replace(srcstr, dststr)
    return string

if __name__ == "__main__":
    srcstr = 'abcdef'
    dststr = 'mon'
    string = 'abcdefghi'
    print tr(srcstr, dststr, string)
