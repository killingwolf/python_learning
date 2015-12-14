#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:07:17
# @Author  : killingwolf (killingwolf@qq.com)


class Stack(object):

    stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise (IndexError, 'pop from empty list')

    def isempty(self):
        return False if len(self.stack) else True

    def peek(self):
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)

    __repr__ = __str__

if __name__ == '__main__':
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    print s1
    s1.pop()
    print s1
    print s1.peek()
    print s1
    print s1.isempty()
    s1.pop()
    print s1.isempty()
    # s1.pop()
