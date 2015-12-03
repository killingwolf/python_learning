#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a decorator test module
"""
from time import time


def logged(when):
    def log(f, *args, **kargs):
        print '''Called: function: %s
            args:%s
            kargs: %r
        ''' % (f, args, kargs)

    def pre_logged(f):
        print "****** pre_logged ******"

        def wrapper(*args, **kargs):
            print "11111 pre_logged 111111"
            log(f, *args, **kargs)
            print "22222 pre_logged 222222"
            return f(*args, **kargs)
        print "33333 pre_logged 33333"
        return wrapper

    def post_logged(f):
        print "###### post_logged #######"

        def wrapper(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                print "44444 post_logged 44444"
                log(f, *args, **kargs)
                print "55555 post_logged 55555"
                print "time delta: %s" % (time() - now)
        print "66666 post_logged 66666"
        return wrapper

    try:
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre_logged" or "post"'


@logged("pre")
@logged("post")
# @logged("post")
# @logged("pre")
def hello(name, *args, **kargs):
    print "hello,", name

hello("world!", 2015, a=10)
# hello
