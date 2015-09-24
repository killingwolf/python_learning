#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com

def main():
    """ dict join
    """

    dict1 = {
        'key1' : "value1",
        'key2' : "value2"
    }
    dict2 = {
        'key2' : "value2",
        'key3' : "value3"
    }
    tmp_dict = {}
    
    for (k, v) in dict1.iteritems():
        tmp_dict.update({k : v})
    for (k, v) in dict2.iteritems():
        tmp_dict.update({k : v})

    print tmp_dict
    

if __name__ == "__main__":
        main()
