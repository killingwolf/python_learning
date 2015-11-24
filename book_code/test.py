#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a test module
"""
x = 10


def foo():
    y = 5
    bar = lambda: x + y
    print bar()
    y = 10
    print bar()


class MyClass(object):

    """docstring for MyClass"""
    a = [1]

    def b(self):
        self.a[0] += 1
        print self.a[0]


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
    # bb = MyClass()
    # bb.b()
    # bb.b()
    # bb.b()
    # del bb
    # print factorial(5)
    g1 = gen(1)
    g2 = gen(4)
    g3 = gen(1000)
    # g1.close()
    print g1.next()
    g1.send(10)
    print g1.next()
    g1.send(10)
    print g1.next()
    # print g1.next(), g2.next(), g3.next()
    # print g1.next(), g2.next(), g3.next()
    # print g1.next(), g2.next(), g3.next()
