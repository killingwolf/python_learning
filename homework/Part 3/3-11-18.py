#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-27 16:03:43
# @Author  : killingwolf (killingwolf@qq.com)

import threading
import time

lock = threading.Lock()


def a():
    # print lock.locked()
    if lock.acquire(0):
        print "a() is't running ,run it"
        # time.sleep(10)
        # lock.release()
    else:
        print "a() is running"
        lock.release()


def b():
    # print lock.locked()
    # print lock.acquire(0)
    if lock.acquire(0):
        print "b() is't running ,run it"
        # time.sleep(10)
        # lock.release()
    else:
        print "b() is running"
        lock.release()

if __name__ == '__main__':
    a()
    b()
    b()
    a()
