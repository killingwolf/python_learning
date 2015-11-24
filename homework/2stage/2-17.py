#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(string):
    """ Mr.ED to mR.ed
    """
    for i in string:
        if i.isupper():
            string = string.replace(i, i.lower())
        elif i.islower():
            string = string.replace(i, i.upper())
        else:
            pass
    return string


if __name__ == "__main__":
    print main('Mr.ED')
