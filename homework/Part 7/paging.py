#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-29 18:42:43
# @Author  : killingwolf (killingwolf@qq.com)

import re
import urllib2
import chardet
import cookielib


def get_paging_url(number):
    """ Get number pages from http://bbs.chinaunix.net/
    """

    refer_url = 'http://bbs.chinaunix.net/forum-55-1.html'
    zh_code = ['GBK', 'gb2312', 'GB2312']
    write_file = 'paging.txt'
    # get cookie
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    opener.open(refer_url)

    header = {
        'Host': 'bbs.chinaunix.net',
        # 'Origin': 'http://bbs.chinaunix.net',
        'Referer': refer_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    }
    with open(write_file, 'w') as wfd:
        for i in xrange(2, number + 2):
            get_url = 'http://bbs.chinaunix.net/forum-55-%s.html' % i
            req = urllib2.Request(get_url, headers=header)
            html = urllib2.urlopen(req).read()
            code = chardet.detect(html)['encoding']
            if code in zh_code:
                html = html.decode('GBK').encode('utf-8')
            html = re.findall(
                r'<a href="(.*?)" (style=".*onclick="atarget|onclick="atarget)\(this\)"', html)

            for i in html:
                # print i
                wfd.write(i[0] + '\n')


if __name__ == '__main__':
    try:
        get_paging_url(1)
    except Exception as e:
        print e
