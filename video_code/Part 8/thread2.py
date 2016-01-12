#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 16:02
# @Author  : killingwolf (killingwolf@qq.com)

import threading
import time

def worker():
    print threading.currentThread().getName() + ' starting'
    time.sleep(5)
    print threading.currentThread().getName() + ' Exiting'


def my_service():
    print threading.currentThread().getName() + ' starting'
    time.sleep(10)
    print threading.currentThread().getName() + ' Exiting'

t1 = threading.Thread(name='sleep 2', target=worker)
t2 = threading.Thread(name='sleep 10', target=my_service)
t3 = threading.Thread(target=worker)

t1.start()
t3.start()
t2.start()

