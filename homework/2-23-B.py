#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def tr(srcstr, dststr, string, sensitive=False):
    """ python tr
    """
    if sensitive:
        tmp_srcstr = srcstr
        tmp_string = string
    else:
        tmp_srcstr = srcstr.lower()
        tmp_string = string.lower()

    f = tmp_string.find(tmp_srcstr)
    tmp_list = []
    slength = len(tmp_srcstr)
    if f > -1:
        tmp_list.append(string[:f])
        tmp_list.append(dststr)
        tmp_list.append(string[f + slength:])
    else:
        return string

    return ''.join(tmp_list)


if __name__ == "__main__":
    srcstr = 'ABC'
    dststr = 'mon'
    string = 'abcdef'
    print tr(srcstr, dststr, string, False)
