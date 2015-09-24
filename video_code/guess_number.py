#!/usr/bin/python
#coding:utf-8
"""
Guess number
"""

import random

def guess_number(number):
    """ Guess number
    """
    while True:
        numb = raw_input("Please guess :")
        print numb
        if numb.isdigit():
            numb = int(numb)
            if number == numb:
                print "Yes,you get it"
                break
            elif number < numb:
                print "Too biger"
            else:
                print "Too small!"
        else:
            print "input error!"
            continue


if __name__ == "__main__":
    number = random.randint(0,100)
    print number
    try:
        guess_number(number)
    except:
        print
