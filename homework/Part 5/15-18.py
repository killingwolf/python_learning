#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-24 11:19:35
# @Author  : killingwolf (killingwolf@qq.com)

import re
from time import ctime


def data_corruption_check(datafile):
    """Check data corruption in give datafile

    Read each line in data file, and check the first integer of
    the integer field matches the timestamp given at the front
    of each output line.

    Args:
        datafile: A file tobe checked.

    Return:
        True:
            All line in data file is ok.
        False:
            Some line has corruption data.

    """
    with open(datafile, 'r') as rfd:
        pt = r'''
            (\b(Wed|Tue|Mon|Sun|Sat|Fri|Thu)\b\s
            \b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b\s
            (\d{2})\s
            ((\d{2}:){2}\d{2})\s
            (\d{4}))::
            ([a-z]+@[a-z]+\.(com|edu|net|org|gov))::
            ((\d+)-\d-\d)
        '''
        for line in rfd:
            match = re.search(pt, line, re.X)
            if match:
                if match.groups()[0] != ctime(float(match.groups()[10])):
                    return False
            else:
                return False
        return True

if __name__ == '__main__':
    data = 'redata.txt'
    try:
        print data_corruption_check(data)
    except Exception as e:
        print e
