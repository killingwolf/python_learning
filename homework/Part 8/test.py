#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/11 11:45
# @Author  : killingwolf (killingwolf@qq.com)

import threading

def worker():
    print threading.current_thread().getName()
    print 'worker'

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()

t1 = threading.Thread(target=worker, name='###########')
t2 = threading.Thread(target=worker)
t3 = threading.Thread(target=worker)

t1.start()
t2.start()
t3.start()
if __name__ == '__main__':
    pass
