#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
"This is a hello world module"

import time


def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print "%s cost %s second" % (fn.__name__, time.clock() - start)
    return _wrapper


@time_me
def time_list(data):
    print len([word for line in data for word in line.split()])


@time_me
def time_gen(data):
    print len([word for line in data for word in line.split()])


if __name__ == '__main__':
    ff = r'C:/Users/zhanghengfeng/Desktop/messages'
    data = open(ff, 'r')
    time_list(data)
    data = open(ff, 'r')
    ff = r'C:/Users/zhanghengfeng/Desktop/messages'
    time_gen(data)
