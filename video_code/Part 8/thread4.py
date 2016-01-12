#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 16:34
# @Author  : killingwolf (killingwolf@qq.com)
"""
守护线程
"""

import threading
import time

def daemon():
    print threading.currentThread().getName()+ ' starting'
    time.sleep(2)
    print threading.currentThread().getName()+ ' Exiting'


def none_daemon():
    print threading.currentThread().getName()+ ' starting'
    print threading.currentThread().getName()+ ' Exiting'

if __name__ == '__main__':
    t1 =  threading.Thread(name='non-daemon', target=none_daemon)
    t2 = threading.Thread(name='daemon', target=daemon)
    # t2.setDaemon(True)
    t2.start()
    t2.join()
    t1.start()
