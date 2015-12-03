#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a test module
"""
x = 10


class MyClass(object):

    """docstring for MyClass"""
    a = [1]

    def b(self):
        self.a[0] += 1
        print self.a[0]


class C(object):

    "A test class"

    def __init__(self):
        print "init"

    def __del__(self):
        print 'deleted'


def foo():
    y = 5
    bar = lambda: x + y
    print bar()
    y = 10
    print bar()


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


def gen(n):
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    c1 = C()
    c3 = c2 = c1
    del c1
    del c2
    del c3
