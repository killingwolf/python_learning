#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 16:35:19
# @Author  : killingwolf (killingwolf@qq.com)
import urllib2
import chardet

html = urllib2.urlopen('http://www.sohu.com', timeout=30).read()
code = chardet.detect(html)['encoding']
zh_code = ['GBK', 'gb2312', 'GB2312']
if code in zh_code:
    print html.decode('GBK').encode('utf-8')
else:
    print html

if __name__ == '__main__':
    pass
