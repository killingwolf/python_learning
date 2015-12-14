#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:07:58
# @Author  : killingwolf (killingwolf@qq.com)


class SortedKeyDict(dict):

    def keys(self):
        return sorted(super(self.__class__, self).keys())

    # def keys(self):
    #     # 无穷递归调用
    #     return sorted(self.keys())

if __name__ == '__main__':
    sdict = {
        'a': 1,
        'c': 3,
        'd': 4,
        'b': 2,
    }
    print sdict.keys()
    sdict = SortedKeyDict(sdict)
    print sdict.keys()
