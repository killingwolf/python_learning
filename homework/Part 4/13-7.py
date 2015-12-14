#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:02:37
# @Author  : killingwolf (killingwolf@qq.com)

import time


class Date(object):

    fmt_string = {
        'MDY': '%m/%d/%y',
        'MDYY': '%m/%d/%Y',
        'DMY': '%d/%m/%y',
        'DMYY': '%d/%m/%Y',
        'MODYY': '%m %d, %Y'
    }

    def __init__(self, date=None):
        self.date = date if date else time.time()

    update = __init__

    def display(self, fmt=None):
        if fmt:
            if fmt in self.fmt_string:
                rt = time.strftime(
                    self.fmt_string[fmt], time.localtime(self.date))
            else:
                rt = 'Unsupportted fmt type'
        else:
            rt = time.ctime(self.date)
        return rt

if __name__ == '__main__':
    d1 = Date()
    print d1.display()
    d1.update(10999995555)
    print d1.display()
    print d1.display('DMY')
    print d1.display('xxx')
