#!/usr/bin/python
#coding:utf-8

def perfect_number(number):
    """perfect number check
    """
    i = 1
    j = 0
    while i < number:
        if number % i == 0:
            j += i
        i += 1
    if j == number:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(raw_input("Please input a Number:\n"))
    print perfect_number.__doc__
    print __name__
    if perfect_number(number):
        print "perfect number"
    else:
        print "Not perfect number"
