#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-23 23:28:56
# @Author  : killingwolf (killingwolf@qq.com)
from random import randint
from random import choice
from string import lowercase
from sys import maxint
from time import ctime


def create_redata(redata):
    doms = ('com', 'edu', 'net', 'org', 'gov')

    with open(redata, 'w+') as wfd:
        for i in range(randint(5, 10)):
            dtint = randint(0, maxint - 1)  # pick date
            dtstr = ctime(dtint)        # date string
            shorter = randint(4, 7)        # login shorter
            em = ''
            for j in range(shorter):        # generate login
                em += choice(lowercase)

            longer = randint(shorter, 12)  # domain longer
            dn = ''
            for j in range(longer):         # create domain
                dn += choice(lowercase)

            wfd.write('%s::%s@%s.%s::%d-%d-%d\n' % (
                dtstr,
                em,
                dn,
                choice(doms),
                dtint,
                shorter,
                longer)
            )

if __name__ == '__main__':
    create_redata('redata.txt')
