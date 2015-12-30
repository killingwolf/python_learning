#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-30 15:34:02
# @Author  : killingwolf (killingwolf@qq.com)
import re
import urllib2
import cookielib
import chardet
from random import choice


class BaiDu(object):

    zh_code = ['GBK', 'gb2312', 'GB2312']

    def __init__(self, host, get_urls, refer_url, agents=[]):
        self.get_urls = get_urls
        self.agents = agents
        self.header = {
            'Host': host,
            'Referer': refer_url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/47.0.2526.106 Safari/537.36'
        }

    def get_html(self):

        if self.agents:
            agent = choice(self.agents)

        # add cookile support
        cookie = cookielib.CookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)

        # add agent support
        if agent:
            proxy_handler = urllib2.ProxyHandler({'http': agent})
            # proxy_handler = urllib2.ProxyHandler({'https': agent})
            opener = urllib2.build_opener(cookie_handler, proxy_handler)
        else:
            opener = urllib2.build_opener(cookie_handler)

        urllib2.install_opener(opener)
        try:
            datas = []
            for url in self.get_urls:
                req = urllib2.Request(url, headers=self.header)
                html = urllib2.urlopen(req, timeout=30).read()
                # add chinese support
                code = chardet.detect(html)['encoding']
                if code in self.zh_code:
                    html = html.decode('GBK').encode('utf-8')
                datas.append(html)
            return datas
        except Exception as e:
            raise Exception(e)

    def get_keyword(self):
        words = []
        datas = self.get_html()
        for data in datas:
            words += re.findall(r's:\[|,"(.*?)"', data)
        return words

if __name__ == '__main__':
    keywords = ['科技', '集团']
    get_urls = []
    for keyword in keywords:
        s = urllib2.quote(keyword)
        get_urls.append(
            'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=%s' % s)
    host = 'sp0.baidu.com'
    refer_url = 'https://www.baidu.com/'
    agents = ['http://113.31.80.194:8080', 'http://60.195.250.55:80']
    bd = BaiDu(host, get_urls, refer_url, agents)
    # bd.get_html()
    for word in bd.get_keyword():
        print word
