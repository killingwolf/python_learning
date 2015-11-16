#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
"This is a hello world module"

import os


if __name__ == '__main__':
    ff = r'C:/Users/zhanghengfeng/Desktop/test.txt'
    with open(ff, 'a+') as f:
        while True:
            aLine = raw_input("Enter a line:")
            if aLine != '.':
                f.write("%s" % (aLine, os.linesep))
            else:
                break
