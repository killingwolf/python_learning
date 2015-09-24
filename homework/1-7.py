#!/usr/bin/python
#coding:utf-8


def main(numb=5):
    """输出格式
    
    """

    i = numb
    h = i
    j = 1
    k = 1
    while i > 0:
       m = 1
       while m <= (h-k): 
           print " ",
           m = m + 1
       l = 1
       while l <= j:
           print "*",
           l = l + 1
       print
       i = i - 1
       k = k + 1
       j = j + 2


if __name__ == "__main__":
    while True:
        numb = raw_input("please input a number "
                         "between 1 and 15:").strip()
        if numb.isdigit(): 
            main(int(numb))
            break
        else:
            print "input error!"
            continue
