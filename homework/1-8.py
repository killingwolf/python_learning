#!/usr/bin/python
# coding:utf-8


def main(numb=9):
    """输出格式

    """

    i = numb
    h = i / 2 + 1
    j = 1
    k = 1
    while i > 0:
        if i > h:
            print " " * (h - k),
            print "*" * j,
            print
            k = k + 1
            j = j + 2
        elif i == h:
            print " " * (h - k),
            print "*" * j,
            print
        else:
            k = k - 1
            j = j - 2
            print " " * (h - k),
            print "*" * j,
            print
        i = i - 1


if __name__ == "__main__":
    main()
