#!/usr/bin/python
#-*- coding:utf-8 -*- 


def main(numb=5):
    """输出格式
    """

    i = 0
    while i < 7:
        j = 1
        space = " " * 2 * (6 - i)
        print space,
        while j <=i:
            print "*",
            j += 1
        r = 1
        while r < i:
            print "*",
            r += 1
        print
        i += 1

if __name__ == "__main__":
    main()
