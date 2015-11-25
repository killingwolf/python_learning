#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def main():
    """ dict key value revese
    """

    dict1 = {
        'key1': "value1",
        'key2': "value2"
    }

    print dict1

    l1 = dict1.keys()
    l2 = dict1.values()

    dict2 = dict(zip(l2, l1))

    print dict2


if __name__ == "__main__":
    main()
