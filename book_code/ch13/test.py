#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-28 12:16:48
# @Author  : killingwolf (killingwolf@qq.com)


class MyFirstClass(object):

    """docstring for MyFirstClass"""

    # print "before __init__"

    def __init__(self, arg):
        # super(MyFirstClass, self).__init__()
        self.arg = arg
        print "__init__"

    # print "after __init__"

    def mymethod(self):
        print "Method in MyFirstClass"

    def __del__(self):
        print "myins is terminated"


class AddrBookEntry(object):

    """docstring for AddrBookEntry"""

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Create instance for :', self.name

    def update_phone(self, newph):
        self.phone = newph
        print 'Updated phone# for:', self.name


class EmplAddrBookEntry(AddrBookEntry):

    """docstring for EmplAddrBookEntry"""

    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.id = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Update Emain address for:', self.name


class TestStaticMethod:

    @staticmethod
    def foo():
        print 'calling static method foo'


class TestClassMethod:

    @classmethod
    def foo(cls):
        print "calling class method foo()"
        print 'foo is part of class:', cls.__name__


class Parent(object):

    def pm(self):
        print "parent pm"

    def parent_method(self):
        print 'calling parent method'


class Child(Parent):

    def pm(self):
        print super(Child, self)
        print 'chiled pm'

    def child_method(self):
        print 'calling child method'


class RoundFload(float):

    def __new__(cls, val):
        return super(RoundFload, cls).__new__(cls, round(val, 2))


class SortedKeyDict(dict):

    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


# class P1:
class P1(object):

    def foo(self):
        print "called P1-foo()"


# class P2:
class P2(object):

    def foo(self):
        print "called P2-foo()"

    def bar(self):
        print "called P2-bar()"


class C1(P1, P2):
    pass


class C2(P1, P2):

    def bar(self):
        print "called C2-bar()"


class GC(C1, C2):
    pass

if __name__ == '__main__':
    gc = GC()
    gc.foo()
    gc.bar()
    print issubclass(GC, C1)
