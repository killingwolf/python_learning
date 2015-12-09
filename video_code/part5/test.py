#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-08 16:07:48
# @Author  : killingwolf (killingwolf@qq.com)

import time


class Foo(object):

    """ __new__ 和__init__的区别"""

    def __new__(cls, *args, **kwargs):
        print "__new__ called"
        tmp = super(cls.__class__, cls).__new__(cls, *args, **kwargs)
        print 'cls id is :{0}'.format(id(cls))
        print 'tmp id is :{0}'.format(id(tmp))

    def __init__(self):
        print "__init__ called"


class Foo2(object):
    "*attr Demo"
    num = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

# print issubclass(Foo2, object)
# p = Foo2(10, 20)
# print isinstance(p, object)

# print getattr(p, 'x')
# print hasattr(p, 'xx')
# setattr(p, 'xx', 100)
# print getattr(p, 'xx')
# delattr(p, 'xx')
# print hasattr(p, 'xx')


class Foo3(object):
    """封装和隐藏"""

    def __init__(self, x, y):
        self.__x = x
        self.y = y

    def print_x_y(self):
        print self.__x, self.y

    def __print_x_y(self):
        print self.__x, self.y


# p = Foo3(100, 300)
# print p.y
# print p.__x  # 获取隐藏属性失败
# print p._Foo3__x  # 获取隐藏属性成功
# p.print_x_y()
# p.__print_x_y()  # 获取隐藏方法失败
# p._Foo3__print_x_y()  # 获取隐藏属性成功

class Foo4(Foo3):
    pass

# print dir(Foo4)
# p = Foo4(100, 200)
# p.print_x_y()
# p.__print_x_y()  # 继承隐藏方法失败
# p._Foo3__print_x_y()


class RoundFloadManual(object):
    """模拟标准类型"""
    def __init__(self, var):
        assert isinstance(var, float), "value must be a float"
        self.value = round(var, 2)

    def __str__(self):
        return "The value {0}".format(self.value)

    __repr__ = __str__

# p = RoundFloadManual(10.33333)
# print p
# print p.value


class Time60(object):
    """操作符重载"""
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    # def __str__(self):
    #     return "{0}:{1}".format(self.hr, self.min)

    def __add__(self, other):
        return self.__class__(self.hr+other.hr, self.min+other.min)


# mon = Time60(10, 30)
# tue = Time60(5, 15)

# o = mon + tue
# print "{0}:{1}".format(o.hr, o.min)


class Foo5(object):
    """__*attr__ vs __*attribute__"""
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        if name == "age":
            return self.x
        else:
            raise (AttributeError, name)

    # def __getattribute__(self, attr):
    #     return attr

# p = Foo5(10)
# print p.x


class MyIterator(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n


# p = MyIterator(10)
# for i in p:
#     print i


class Date(object):
    """静态方法和类方法"""
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now1():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


class EuroDate(Date):
    def __str__(self):
        return "%d-%d-%d" % (self.year, self.month, self.day)


# d = Date(2, 3, 4)
# d = EuroDate(2, 3, 4)
# # print d.now().year
# # print d.now().month
# # print d.now().day
# print d.now()
# print d.now1()


if __name__ == '__main__':
    # a = Foo.__new__(Foo, 10)
    # print "a id is: {0}".format(id(a))
    # print "Foo id is: {0}".format(id(Foo))
    pass
