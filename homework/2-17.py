#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(string):
    """ Mr.ED to mR.ed
    """

    tmp_list = []
    for i in string:
        if i.isalpha():
            if i.isupper():
                tmp_list.append(i.lower())
            else:
                tmp_list.append(i.upper())
        else:
            tmp_list.append(i)
    print ''.join(tmp_list)


if __name__ == "__main__":
    main('Mr.ED')
