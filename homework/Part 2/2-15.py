#!/usr/bin/python
# coding:utf-8


def my_strip(string):
    """去除字符串首尾空格
    """

    # The space numbers in the head of the string.
    h = 0
    # The space numbers in the head of the string.
    t = 0
    for i in string:
        if i != ' ':
            break
        else:
            h += 1
    for i in string[::-1]:
        if i != ' ':
            break
        else:
            t -= 1
    if t == 0:
        return string[h:]
    else:
        return string[h:t]

if __name__ == "__main__":
    s = "bb cc aa "
    print my_strip(s)
