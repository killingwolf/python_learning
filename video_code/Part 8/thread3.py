#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/12 16:23
# @Author  : killingwolf (killingwolf@qq.com)

import time
import urllib2
from threading import Thread


class GetUrlTread(Thread):

    def __init__(self, url):
        self.url = url
        super(self.__class__, self).__init__()

    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()


def get_response():
    urls = ['http://www.baidu.com',
            'http://www.ebay.com',
            'http://www.google.com'
            ]
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlTread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print 'Elaped time %s' % (time.time() - start)

if __name__ == '__main__':
    get_response()
