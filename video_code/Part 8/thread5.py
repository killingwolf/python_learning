#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 17:07
# @Author  : killingwolf (killingwolf@qq.com)

import time
import threading


class Foo(threading.Thread):

    def run(self):
        # start = time.time()
        fname = threading.currentThread().getName()
        with open(fname, 'w') as wfd:
            wfd.write(fname)
        time.sleep(2)
        # end = time.time()
        # print threading.currentThread().getName(), 'running time ', \
        #     end - start


def foo():
    print threading.currentThread().getName()

if __name__ == '__main__':
    start = time.time()
    for i in xrange(5):
        t = Foo()
        t.start()
        t.join()
    end = time.time()
    print end - start
