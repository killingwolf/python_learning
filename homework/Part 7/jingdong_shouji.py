#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-30 11:08:32
# @Author  : killingwolf (killingwolf@qq.com)

import re
import urllib2
import chardet
import cookielib


def get_shouji_url(refer_url, get_urls, url_file, header, pt):
    """Get data form get_urls and write them to url_file.

    Get data from get_urls, then use regular expression to filter them.
    At the end write all filted data to url_file.

    Args:
        refer_url: A refer url in http header.
        get_urls: A list of urls to be getted.
        url_file: A file where the get url to be saved.
        header: An dict http header.
        pt: A regular expression.

    Return:
        None

    Raise:
        Exception

    """
    zh_code = ['GBK', 'gb2312', 'GB2312']
    # add cookie suport
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    with open(url_file, 'w') as wfd:
        for get_url in get_urls:
            req = urllib2.Request(get_url, headers=header)
            try:
                html = urllib2.urlopen(req).read()
                code = chardet.detect(html)['encoding']
                if code in zh_code:
                    html = html.decode('GBK').encode('utf-8')
                html = re.findall(pt, html)
                for i in html:
                    wfd.write(i + '\n')
            except Exception as e:
                raise Exception(e)


def get_shouji_price(refer_url, get_urls, price_file, header, pt):
    """Get data form get_urls and write them to price_file.

    Get data from get_urls, then use regular expression to filter them.
    At the end write all filted data to url_file.

    Args:
        refer_url: A refer url in http header.
        get_urls: A dict of consist of iterm_ids and get_urls.
        url_file: A file where the get price to be saved.
        header: An dict http header.
        pt: A regular expression.

    Return:
        None

    Raise:
        Exception
    """

    zh_code = ['GBK', 'gb2312', 'GB2312']
    # add cookie suport
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    opener.open(refer_url)

    with open(price_file, 'w') as wfd:
        for get_url in get_urls:
            header['Referer'] = re.sub(r'\d+', get_url, refer_url)
            req = urllib2.Request(get_urls[get_url], headers=header)
            html = urllib2.urlopen(req).read()
            code = chardet.detect(html)['encoding']
            if code in zh_code:
                html = html.decode('GBK').encode('utf-8')
            html = re.findall(pt, html)
            for i in html:
                wfd.write(i + '\n')

if __name__ == '__main__':
    get_urls = []
    url_file = 'jd_url.txt'
    price_file = 'jd_price.txt'
    pages = 5
    for i in xrange(pages):
        get_urls.append(
            'http://list.jd.com/list.html?cat=9987%2C653%2C655&ev=exprice_M2100L4199%40&page=' + str(i + 1) + '&JL=6_0_0')

    refer_url = 'http://list.jd.com/list.html?cat=9987%2C653%2C655&ev=exprice_M2100L4199%40&page=1&JL=6_0_0'
    header = {
        'Host': 'list.jd.com',
        'Referer': refer_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    }
    pt = r'href="(http://item.jd.com/\d+?.html)"'
    get_shouji_url(refer_url, get_urls, url_file, header, pt)

    refer_url = 'http://item.jd.com/1514800.html'
    get_urls = {}
    with open(url_file, 'r') as rfd:
        for line in rfd:
            numb = re.search(r'(\d+)', line).group()
            get_urls.update({
                numb:
                    'http://p.3.cn/prices/mgets?callback=jQuery9027716&type=1&area=1_72_4137_0&pdtk=&pduid=786318978&pdpin=&pdbp=0&skuIds=J_' +
                numb + '%2C'
            })
    header = {
        'Host': 'p.3.cn',
        'Referer': refer_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    }
    pt = r'"p":"(\d+\.\d+?)'
    get_shouji_price(refer_url, get_urls, price_file, header, pt)
