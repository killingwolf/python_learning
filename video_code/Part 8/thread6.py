#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 19:49
# @Author  : killingwolf (killingwolf@qq.com)
"""
多线程同步
    锁
    队列
"""
import Queue
import threading


class Foo(threading.Thread):
    pass

def queue_test():
    q1 = Queue.Queue()
    for i in xrange(1, 10):
        q1.put(i)
    while True:
        print q1.get()

if __name__ == '__main__':
    queue_test()

