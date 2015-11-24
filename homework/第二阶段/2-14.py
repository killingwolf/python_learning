#!/usr/bin/python
#coding:utf-8

import os

if __name__ == "__main__":
    nl = []
    sl = []
    while True:
        try:
            ipt = raw_input("Please input a number or string ,\nuse ctrl+d or "
                            "ctrl+c to complete input：")
            if ipt.isalpha():
                sl.append(ipt)
            elif ipt.isalnum():
                nl.append(ipt)
            else:
                pass
        except:
            os.system('clear')
            break
    sl.sort()
    nl.sort()
    print "Your inputted strings are: "
    for s in sl:
        print s
    print "Your inputted numbers are: "
    for n in nl[::-1]:
        print n
