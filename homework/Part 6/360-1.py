#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-25 23:27:11
# @Author  : killingwolf (killingwolf@qq.com)
import urllib2
import re
# from time import sleep
from random import choice
import chardet


def get_keyword_from_360(word, useagent=False):
    kword = urllib2.quote(word)
    agent = ['http://113.31.80.194:8080', 'http://60.195.250.55:80']
    url = 'http://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&ecodeout=utf-8&format=json&fields=word&word=' + \
        kword
    headers = {
        'GET': url,
        'Host': 'sug.so.360.cn',
        'Referer': 'http://www.haosou.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    }
    if useagent:
        proxy_handler = urllib2.ProxyHandler({'http': choice(agent)})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
    req = urllib2.Request(url, headers=headers)
    rt = urllib2.urlopen(req, timeout=60).read()
    return rt

if __name__ == '__main__':
    words = ['科技', 'nihao']
    for word in words:
        str1 = get_keyword_from_360(word)

        zh_code = ['GBK', 'gb2312', 'GB2312']
        if chardet.detect(str1)['encoding'] in zh_code:
            print '#' * 79
            str1 = str1.decode('GBK').encode('utf-8')
            ss = re.findall(r'"word":"(.*?)"', str1)
            # print
            for i in ss:
                print i
        # sleep(5)
