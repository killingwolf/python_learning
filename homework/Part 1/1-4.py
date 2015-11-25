#!/usr/bin/python
# coding:utf-8


def main():
    """打印9*9乘法表

    """

    for i in xrange(1, 10):
        if i != 9:
            print str(i), "   ",
        else:
            print i
    print '---------------------------------------------------------'
    for i in xrange(1, 10):
        print i, "|",
        for j in xrange(1, 10):
            print i * j, "    ",
        print


if __name__ == "__main__":
    main()
