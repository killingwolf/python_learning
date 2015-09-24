#!/usr/bin/python
#coding:utf-8


def main():
    """统计能被17整出的三位数
    
    """
    numb = []
    for i in xrange(100,1000):
        if i % 17 == 0:
            numb.append(i)
    print "能被17整除的三位数个数是：%d\n它们是：%s" % (len(numb),numb)


if __name__ == "__main__":
    main()
