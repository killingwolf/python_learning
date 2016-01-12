#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 0:56
# @Author  : killingwolf (killingwolf@qq.com)

import time
import threading


def worker(num):
    print 'worker %d' % num
    print time.ctime()
    time.sleep(5)

threads = []

# create thread
for i in xrange(5):
    thread1 = threading.Thread(target=worker, args=(i, ))
    threads.append(thread1)

# start thread
for i in threads:
    i.start()
