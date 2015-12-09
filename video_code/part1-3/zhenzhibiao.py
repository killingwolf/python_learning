#!/usr/bin/python
#coding:utf-8

if __name__ == "__main__":
    bool_list = [True, False]
    s1 = ("p        q     (not p) or q     (p and q) or q     (p or q) and p    "
          "(p or q) and (p and q)")
    print s1
    print "-" * len(s1)
    for p in bool_list:
        for q in bool_list:
            b1 = not p or q
            b2 = p and q or q
            b3 = p or q and p
            b4 = (p or q) and (p and q)
            print "%s\t%s\t %s\t\t  %s\t\t   %s    \t\t%s" % (p,q,b1,b2,b3,b4)
