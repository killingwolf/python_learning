#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 10:45:16
# @Author  : killingwolf (killingwolf@qq.com)

import re

from string import punctuation


def word_count(f, sensitive=True):
    """ word statistics with RE """
    with open(f, 'r') as f:
        # A RE to replace all punctuation except '-'.
        re1 = r'[^\w\-\s]'
        # A RE to replace any '-'
        re2 = r'^-+$'
        kwords = {}
        words = [word for line in f for word in re.sub(
            re1, ' ', line).split() if not re.match(re2, word)]
        for word in words:
            if not sensitive:
                word = word.lower()
            if word in kwords:
                kwords[word] += 1
            else:
                kwords[word] = 1

    return kwords


def word_count_v2(f, sensitive=True):
    """ word statistics with string.punctuation """
    with open(f, 'r') as f:
        kwords = {}
        words = (word.translate(None, punctuation) for line in f for word
                 in line.split() if word.translate(None, punctuation))
        for word in words:
            if not sensitive:
                word = word.lower()
            if word in kwords:
                kwords[word] += 1
            else:
                kwords[word] = 1

    return kwords


if __name__ == '__main__':
    f = 'gettysburg.txt'
    try:
        # kwords = word_count(f)
        kwords = word_count_v2(f)
        # unrpt = [i for i in kwords if kwords[i] == 1]
        # print "Non-repetitive words:%s \n count：%d" % (unrpt, len(unrpt))
        print "Non-repetitive words"
        n = 0
        for i in kwords:
            if kwords[i] == 1:
                print i
                n += 1
        print "Non-repetitive words count is: ", n
        print "word  count"
        for i in kwords:
            print i, kwords[i]
    except BaseException, e:
        print e
