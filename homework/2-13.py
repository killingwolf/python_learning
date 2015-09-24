#!/usr/bin/python
#coding:utf-8

import sys
import keyword
try:
    s = raw_input("Please in put a strings:").strip()
except:
    print "Your input has error!"
    sys.exit()

if __name__ == "__main__":
    lenth = len(s)
    if lenth == 1:
        print "Your string lenth is :%d " % lenth
    elif keyword.iskeyword(s):
        print "You input a Python keyword!"
    else:
        print "The lenth of your strings is :%d " % lenth
