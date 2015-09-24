#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com

def main():
    """ combine list to dict
    """
    l1 = [1, 2, 3]
    l2 = ['a', 'b', 'c']
    dict1 = dict(zip(l1, l2))
    print dict1

if __name__ == "__main__":
        main()

