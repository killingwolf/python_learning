#!/usr/bin/python
# coding:utf-8


def main(numb=10):
    """输出格式
    """
    for i in xrange(1, numb):
        s = ''
        for j in xrange(1, i + 1):
            s = s + str(j)
        sum = int(s) * 8 + i
        print "%d * 8 + %d = %d" % (int(s), i, sum)

if __name__ == "__main__":
    main()
