#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def rot13(srcstr):
    """ rot13 encryption algorithm
    """
    upper_table = {}
    lower_table = {}
    upper_range = range(ord('A'), ord('Z') + 1)
    lower_range = range(ord('a'), ord('z') + 1)
    lenth = 0
    for i in upper_range:
        if lenth < 13:
            upper_table[chr(i)] = chr(i+13)
        else:
            upper_table[chr(i)] = chr(i-13)
        lenth += 1
    lenth = 0
    for i in lower_range:
        if lenth < 13:
            lower_table[chr(i)] = chr(i+13)
        else:
            lower_table[chr(i)] = chr(i-13)
        lenth += 1
    tmp_list = []
    for i in srcstr:
        if i.isalpha():
            if i in upper_table:
                tmp_list.append(upper_table[i])
            else:
                tmp_list.append(lower_table[i])
        else:
            tmp_list.append(i)
    return ''.join(tmp_list)


if __name__ == "__main__":
    # print '[%s]' % rot13('This is a short sentence.')
    print '[%s]' % rot13('Guvf vf n fubeg fragrapr.')
