#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-23 16:29:55
# @Author  : killingwolf (killingwolf@qq.com)
import re
if __name__ == '__main__':
    # 15-1
    p151 = r'[bh][aiu]t,?'
    print re.search(p151, 'hut').group()
    # 15-2
    p152 = r'\w+ \w+'
    print re.search(p152, 'abc cba').group()
    # 15-3
    p153 = r'\w+, [a-zA-Z]'
    print re.search(p153, 'abc, cba').group()
    # 15-4
    p154 = r'^[a-zA-Z_]+\w*'
    print re.search(p154, '_').group()
    # 15-5
    p155 = r'^[1-9][0-9]{3} [a-zA-Z ]*'
    print re.search(p155, '1180 b').group()
    # 15-6
    p156 = r'^www\.[a-zA-Z0-9\-]+\.(com|edu|net)$'
    print re.search(p156, 'www.abc-c.net').group()
    print re.search(p156, 'www.abc.com').group()
    print re.search(p156, 'www.abc.edu').group()
    # 15-7
    p157 = r'^(\+|-)?((0|[1-9]\d*)|(0[0-7])|(0[xX][0-9a-fA-F])+)$'
    print re.search(p157, '-0X1').group()
    # 15-8
    p158 = r'^(\+|-)?((0|[1-9]\d*)|(0[0-7])|(0[xX][0-9a-fA-F])+)$'
    print re.search(p158, '1222').group()
    # 15-9
    p159 = r'^[+-]?(0|[1-9]+)\.\d+$'
    print re.search(p159, '-1.2').group()
    # 15-10
    # p1510 = r'([+-]?(0|[1-9]\d*)?)?[+-]?([1-9]|\d*)?i$'
    p1510 = r'([+-]?(\d*)?)?[+-]?([1-9]|\d*)?i$'
    print re.search(p1510, '-1-2i').group()
    # 15-11
    p1511 = r'^(\.?[\w-]+)+@([\w-]+\.[\w-]+)+$'
    print re.search(p1511, 'a.b-@b.com.cn').group()
    # 15-12
    p1512 = r'^https?://([\w-]+\.?[a-zA-Z/]+)+$'
    print re.search(p1512, 'http://c.com/bbb/ccc.html').group()
    # 15-14
    p1514 = r'1[0-2]'
    print re.search(p1514, '10').group()
    print re.search(p1514, '11').group()
    print re.search(p1514, '12').group()
    # 15-19
    str1 = 'Tue Jul 21 17:19:18 1987::wmaoavw@bxboftm.org::553857558-7-7'
    p1519 = r'''
            (\b(Wed|Tue|Mon|Sun|Sat|Fri|Thu)\b\s
            \b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b\s
            (\d{2})\s
            ((\d{2}:){2}\d{2})\s
            (\d{4}))
    '''
    print re.search(p1519, str1, re.X).group()
    # 15-20
    p1520 = r'[a-z]+@[a-z]+\.(com|edu|net|org|gov)'
    print re.search(p1520, str1).group()
    # 15-21
    p1521 = r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b'
    print re.search(p1521, str1).group()
    # 15-22
    p1522 = r'\d{4}'
    print re.search(p1522, str1).group()
    # 15-23
    p1523 = r'\b((\d{2}:){2}\d{2})\b'
    print re.search(p1523, str1).group()
    # 15-24
    p1524 = r'([a-z]+)@([a-z]+\.(com|edu|net|org|gov))'
    match = re.search(p1524, str1).groups()
    print match[0] + match[1]
    # 15-25
    p1525 = r'([a-z]+)@([a-z]+\.(com|edu|net|org|gov))'
    match = re.search(p1524, str1).groups()
    print match[0], match[1]
    # 15-26
    p1526 = r'[a-z]+@[a-z]+\.(com|edu|net|org|gov)'
    print re.sub(p1526, 'aaa@bbb.com', str1)
    # 15-27
    p1527 = r'''
            (\b(Wed|Tue|Mon|Sun|Sat|Fri|Thu)\b\s
            \b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b\s
            (\d{2})\s
            ((\d{2}:){2}\d{2})\s
            (\d{4}))
    '''
    match = re.search(p1527, str1, re.VERBOSE).groups()
    print "%s %s, %s" % (match[2], match[3], match[6])
    # 15-28
    p1528 = r'(\d{3}-){1,2}\d{4}'
    print re.search(p1528, '800-555-1212').group()
    print re.search(p1528, '555-1212').group()
    # 15-29
    p1529 = r'(^\(\d{3}\)?|^\d{3}-)?\d{3}-\d{4}'
    print re.search(p1529, '800-555-1212').group()
    print re.search(p1529, '555-1212').group()
    print re.search(p1529, '(800)555-1212').group()
