#!/usr/bin/python
#coding:utf-8


def main():
    """while+print输出指定样式
    
    """
    i = 1
    while i < 7:
       j = 1
       while j <= i:
           print j,
           j = j + 1
       i =  i + 1 
       print
         

if __name__ == "__main__":
    main()
