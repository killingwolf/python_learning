#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 00:10:33
# @Author  : killingwolf (killingwolf@qq.com)


class Line(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __repr__(self):
        return str(((self.x1, self.y1), (self.x2, self.y2)))

    __str__ = __repr__

    def length(self):
        return ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**0.5

    def slope(self):
        rt = (self.x1 - self.x2) / float((self.y1 - self.y2))
        return rt if rt else None
if __name__ == '__main__':
    l1 = Line(1, 1, 2, 2)
    print l1
    print l1.slope()
    print l1.length()
    l2 = Line(1, 1, 2, 2)
    print l2
    print l2.slope()
    print l2.length()
