#!/usr/bin/python
# coding:utf-8


def main(numb=5):
    """计算连续整数和

    """

    for i in xrange(1, numb + 1):
        sum = 0
        s = ''
        for j in xrange(1, i + 1):
            sum = sum + j
            if i != j:
                s = s + str(j) + '+'
            else:
                s = s + str(j)
        print s, "=", sum


if __name__ == "__main__":
    while True:
        numb = raw_input("please input a numb:").strip()
        if numb.isdigit():
            main(int(numb))
            break
        elif numb is '':
            main()
            break
        else:
            print "input error!"
            continue
