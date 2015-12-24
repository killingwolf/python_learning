#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 01:01:30
# @Author  : killingwolf (killingwolf@qq.com)
import os


def exec_module(f1, f2):
    with open(f1, 'r') as fd1, open(f2, 'r') as fd2:
        l1 = [line for line in fd1]
        l2 = [line for line in fd2]
        for line in l1:
            if line in l2:
                # __import__(line)
                os.system('python {0}.py'.format(line.strip()))
                # execfile('python {0}.py'.format(line.strip()))

            else:
                print 'Not exist'

if __name__ == '__main__':
    exec_module('a', 'b')
