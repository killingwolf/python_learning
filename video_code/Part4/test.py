#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-07 22:25:29
# @Author  : killingwolf (killingwolf@qq.com)


class Foo(object):
    num = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_xy(self):
        # return self.x + self.y + self.num
        # return self.x + self.y + Foo.num
        return self.x + self.y + self.__class__.num

    def print_num(self):
        print Foo.num
        print self.num


class Person(object):

    """Person class """

    def __init__(self, name, age, height):
        dict1 = {
            'work': 'Pythoner',
            '收入': '15K'
        }
        self.name = name
        self.age = age
        self.height = height
        self.zhiye = dict1

    def what_you_name(self):
        print "My name is %s " % self.name

    def how_old(self):
        print "I am %d years old" % self.age

    def how_height(self):
        print "{1}有{0}米高".format(self.height, self.name)

    def print_salary(self):
        for k in self.zhiye:
            print k, self.zhiye[k]


class TestClass(object):
    jshu = 100
    my_list = []

    def test_jishu(self, number):
        self.jishu = number

    def print_jishu(self):
        print 'jishu,我是实例变量', self.jishu


class FindIp(object):

    """get uniq sougo ips"""

    def __init__(self, path):
        self.txtfile = path

    def get_sougo_ip(self):
        try:
            with open(self.txtfile, 'r') as rfd:
                return set([line.split()[0]
                            for line in rfd if 'sougo' in line])
        except BaseException, e:
            return e


class SaveMoney(object):

    """描述月光族如何省钱"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def save_money(self):
        print '每月存款工资的一半，{0}元'.format(self.salary / 2.0)

    def consume(self):
        # print "消费剩下的一半中支出"
        return self.salary / 2.0

    def consume_total(self):
        consume1 = 1000
        consume2 = 1200
        if consume1 + consume2 > self.consume():
            print "消费超标!"
        else:
            print "You can buy other thins"


class Method(object):

    """绑定方法，类方法，静态方法"""

    def test(self):
        print self
        print 'Instance Method'

    @staticmethod
    def statimtd(x):
        print "staticmethod", x

    @classmethod
    def classmtd(cls, o):
        print cls
        print "classmethod", o


class P1(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test(self):
        print "In P1"
        print self.x, self.y


class C1(P1):

    def __init__(self, x, y, z):
        super(self.__class__, self).__init__(x, y)

    def test(self):
        print "In C1"
        print self.x, self.y
        super(self.__class__, self).test()


if __name__ == '__main__':
    # c1 = C1(10, 20)
    c1 = C1(4, 5, 6)
    c1.test()
