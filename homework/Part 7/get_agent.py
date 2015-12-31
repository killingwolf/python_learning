#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-30 18:45:09
# @Author  : killingwolf (killingwolf@qq.com)
import gzip
import StringIO
import chardet
import re

from baidu_keyword import BaiDu as Agent

if __name__ == '__main__':
    get_urls = ['http://www.youdaili.net/Daili/guowai/4029.html']
    host = 'www.youdaili.net'
    refer_url = 'http://www.youdaili.net/Daili/'
    ags = Agent(host, get_urls, refer_url)
    pt = r'(\d.*?:\d+)@HTTP'
    html = ags.get_html()
    for data in html:
        data = StringIO.StringIO(data)
        gz = gzip.GzipFile(fileobj=data)
        data = gz.read()
        zh_code = ['GBK', 'gb2312', 'GB2312']
        code = chardet.detect(data)['encoding']
        if code in zh_code:
            data = data.decode('GBK').encode('utf-8')
        gz.close()
        print re.findall(pt, data)
