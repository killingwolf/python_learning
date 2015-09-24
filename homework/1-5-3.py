#!/usr/bin/python
#coding:utf-8


def main():
    """while+print输出指定样式
    
    """
    i = 6
    l = i
    j = 1
    while i > 0:
       h = j
       print " " * (l-j),
       while h > 0:
           print h,
           h = h - 1
       print
       i = i - 1
       j = j + 1

if __name__ == "__main__":
    main()
