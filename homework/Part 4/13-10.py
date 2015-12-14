#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:07:39
# @Author  : killingwolf (killingwolf@qq.com)


class StackQueue(object):
    sq = []

    def shift(self):
        if self.sq:
            rt = self.sq[0]
            del self.sq[0]
        else:
            raise (IndexError, 'del from empty list')
        return rt

    def unshift(self, element):
        self.sq = [element] + self.sq

    def push(self, element):
        self.sq.append(element)

    def pop(self):
        if self.sq:
            rt = self.sq.pop()
        else:
            raise (IndexError, 'pop from empty list')
        return rt

    def __str__(self):
        return str(self.sq)

    __repr__ = __str__


if __name__ == '__main__':
    sq1 = StackQueue()
    sq1.unshift(1)
    sq1.unshift(2)
    print sq1
    print sq1.shift()
    print sq1.shift()
    # print sq1.shift()
    sq1.push(1)
    sq1.push(2)
    print sq1
    print sq1.pop()
    print sq1.pop()
