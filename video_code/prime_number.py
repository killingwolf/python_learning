#!/usr/bin/python
#coding:utf-8

count = 88887
i = 2
k = 2
print 2,
pset=set()
while count > 0:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
        if j == i:
            print i,
            if k % 8 == 0:
                print
            count -= 1
            k += 1
    i += 1
