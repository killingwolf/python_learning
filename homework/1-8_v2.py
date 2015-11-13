#!/usr/bin/python
# coding:utf-8


def main(numb=5):
    """输出格式
    """

    i = numb
    j = 1
    while j <= i:
        space = " " * 2 * (i - j)
        print space,
        k = 0
        while j * 2 - 1 > k:
            print "*",
            k += 1
        print
        j += 1
    l = i - 1
    while l > 0:
        space = " " * 2 * (i - l)
        print space,
        k = 0
        while l * 2 - 1 > k:
            print "*",
            k += 1
        print
        l -= 1


if __name__ == "__main__":
    main()
