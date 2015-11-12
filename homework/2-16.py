#!/usr/bin/python
# coding:utf-8


def main(number):
    """ 数字转化为英文单词
    """
    l1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine']
    number = str(number)
    l2 = []
    for i in number:
        i = int(i)
        l2.append(l1[i])

    return '-'.join(l2)

if __name__ == "__main__":
    print main(88775)
