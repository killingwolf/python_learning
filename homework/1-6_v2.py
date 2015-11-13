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
        l = j
        while l > 0:
            print l,
            l -= 1
        k = 2
        while k <= j:
            print k,
            k += 1
        print
        j = j + 1


if __name__ == "__main__":
    main(5)
    # while True:
    #     numb = raw_input("please input a number "
    #                      "between 1 and 15:").strip()
    #     if numb.isdigit() and 1 <= int(numb) <= 15:
    #         main(int(numb))
    #         break
    #     else:
    #         print "input error!"
    #         continue
