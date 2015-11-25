#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com


def main():
    """ dict operation
    """
    dict1 = {
        'ak': 'av',
        'dk': 'dv',
        'ck': 'cv',
        '1k': '1v',
        'bk': 0
    }
    for key in sorted(dict1):
        print key
    for key in sorted(dict1):
        print key, dict1[key]
    for value in sorted(dict1.values()):
        for key in dict1.keys():
            if dict1[key] == value:
                print value, key


if __name__ == "__main__":
    main()
