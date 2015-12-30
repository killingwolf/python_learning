#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-29 17:24:14
# @Author  : killingwolf (killingwolf@qq.com)
import urllib
import urllib2
import cookielib

login_url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes&return_type=1'
post_url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LGiG2'

# 用户名为中文时，要用urllib.quote() 或者urllib.quote_plus()
# 还要注意汉字的编码问题
username = 'killingwolf'
password = '12345678'

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

header = {
    'Host': 'bbs.chinaunix.net',
    'Origin': 'http://bbs.chinaunix.net',
    'Referer': 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
}

post_data = {
    'formhash': 'a54fd87d',
    'referer': 'http://bbs.chinaunix.net/forum.php',
    'username': username,
    'password': password,
    'loginsubmit': 'true',
    'return_type': ''
}

post_data = urllib.urlencode(post_data)

req = urllib2.Request(post_url, post_data, header)
text = urllib2.urlopen(req).read()

with open('xxx.html', 'w') as wfd:
    wfd.write(text)


# print post_data
if __name__ == '__main__':
    pass
