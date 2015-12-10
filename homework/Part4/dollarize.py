#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-10 17:15:35
# @Author  : killingwolf (killingwolf@qq.com)


def dollarize(n):
    if isinstance(n, float):
        if n > 0:
            negtive = False
        else:
            negtive = True
        n = str(round(abs(n), 2)).split('.')
        if len(n[0]) % 3 == 0:
            n[0] = ','.join([n[0][3 * (i - 1):3 * i]
                             for i in xrange(1, len(n[0]) / 3 + 1)])
        else:
            h = len(n[0]) % 3
            hn = n[0][:h]
            n[0] = n[0][h:]
            n[0] = ','.join([hn] + [n[0][3 * (i - 1):3 * i]
                                    for i in xrange(1, len(n[0]) / 3 + 1)])
        if negtive:
            print '-' + '.'.join(n) + '$'
        else:
            print '$' + '.'.join(n)

    else:
        print "n must be float"


def dollarize_v2(value, sigal=False):
    if isinstance(value, float):
        if value > 0:
            negtive = False
        else:
            negtive = True

        value = str(round(abs(value), 2)).split('.')
        val = list(value[0])
        lenth, head = divmod(len(val), 3)

        if head and lenth:
            val.insert(head, ',')

        if head:
            for i in xrange(1, lenth):
                val.insert(4 * i + head, ',')
        else:
            for i in xrange(1, lenth):
                val.insert(3 * i + head, ',')

        value[0] = ''.join(val)

        if negtive:
            if sigal:
                print '<' + '.'.join(value) + '$>'
            else:
                print '-' + '.'.join(value) + '$'
        else:
            print '$' + '.'.join(value)

    else:
        raise (TypeError, "value must be float")

if __name__ == '__main__':
    # dollarize_v2(-10.555, sigal=True)
    # dollarize_v2(1000000.444)
    # dollarize_v2(1000000000.9999999)

    dollarize(-10.555)
    dollarize(100000.444)
    dollarize(1000000000.9999999)
