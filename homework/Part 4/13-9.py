#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:07:28
# @Author  : killingwolf (killingwolf@qq.com)


class Queue(object):

    queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.queue:
            rt = self.queue[0]
            del self.queue[0]
            return rt

        else:
            raise (IndexError, 'del from empty list')

    def __str__(self):
        return str(self.queue)

    __repr__ = __str__

if __name__ == '__main__':
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    print q1
    print q1.dequeue()
    print q1
    print q1.dequeue()
    print q1
    # print q1.dequeue()
