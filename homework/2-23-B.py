#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def tr(srcstr, dststr, string, sensitive=False):
    """ python tr
    """
    if not sensitive:
        srcstr = srcstr.lower()
        string = string.lower()

    if srcstr in string:
        string = string.replace(srcstr, dststr)
    return string


if __name__ == "__main__":
    srcstr = 'ABC'
    dststr = 'mon'
    string = 'abcdef'
    print tr(srcstr, dststr, string, True)
