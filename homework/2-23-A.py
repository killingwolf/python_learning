#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def tr(srcstr, dststr, string, ):
    """ python tr
    """
    f = string.find(srcstr)
    tmp_list = []
    slength = len(srcstr)
    if f > -1:
        tmp_list.append(string[:f])
        tmp_list.append(dststr)
        tmp_list.append(string[f+slength:])
    return ''.join(tmp_list)


if __name__ == "__main__":
    srcstr = 'abc'
    dststr = 'mon'
    string = 'abcdef'
    print tr(srcstr, dststr, string)
