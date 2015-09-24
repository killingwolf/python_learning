#!/usr/bin/python
#coding:utf-8


def main(numb=5):
    """输出格式
    
    """

    i = numb
    l = i
    j = 1
    while i > 0:
       h = j
       k = j
       m = 2
       print " " * (l-j),
       while h > 0:
           print h,
           h = h - 1
       while m <= k:
           print m,
           m = m + 1 
       print
       i = i - 1
       j = j + 1


if __name__ == "__main__":
    while True:
        numb = raw_input("please input a number "
                         "between 1 and 15:").strip()
        if numb.isdigit() and  1 <= int(numb) <= 15:
            main(int(numb))
            break
        else:
            print "input error!"
            continue
