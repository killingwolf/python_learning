#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a hello world module
    dfadfadfa
"""


class test(Exception):
    print "xx oo xx"


def main():
    raise test, ((1, 2, 3),)

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print e
    else:
        pass
    finally:
        pass
