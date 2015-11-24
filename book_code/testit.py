#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a test module
"""
from operator import add
from operator import mul
from functools import partial


def testit(func, *nkeyargs, **keyargs):
    try:
        retval = func(*nkeyargs, **keyargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')
    for eachFunc in funcs:
        print '-' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) =' % \
                    (eachFunc.__name__, repr(eachVal)), retval[1]
            else:
                print '%s(%s) = FAILED' % \
                    (eachFunc.__name__, repr(eachVal)), retval[1]


def testtest(a, *nkv, **kv):
    print a
    print nkv
    print kv


def arg_location():
    m = 3

    def bar():
        n = 4
        print m + n

        def foo():
            i = 10
            print m + n + i
        foo()
    bar()


def counter(start_at=0):
    count = start_at
    # count = [start_at]
    print "in counter %d" % count
    # print "in counter %d" % count[0]

    def incr():
        # print count
        # print count + 1
        count += 1
        # count[0] += 1
        print "in incr %d" % count
        # print "in incr %d" % count[0]
        return count
        # return count[0]
    return incr


def make_adder(a):
    def adder(b):
        return a + b
    return adder


def test1(test2):
    print 1111
    test2(999)
    print 'test1'


def test2(a):
    print 2222
    print a
    test3()
    print 'test2'


def test3():
    print 33333

if __name__ == '__main__':
    # count = counter(5)
    # print count()
    # print count()
    # print count()
    # p = make_adder(23)
    # print p(100)
    test1(test2)
