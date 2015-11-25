#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 15:32:46
# @Author  : killingwolf (killingwolf@qq.com)

import os


def text_format_v1(sf, df):
    """ Text format v1 before watching the video """
    with open(sf, 'r') as fd, open(df, 'w') as wfd:
        lnumb = 1
        text = []
        for line in fd:
            lid = '***编号****'
            lmc = '公司名称：'
            lhy = '公司行业：'
            lxz = '公司性质：'
            lgm = '公司规模：'
            ljj = '公司简介：'
            # line = line.strip(os.linesep)
            if line.strip(os.linesep):
                if lid in line:
                    text.append(line)
                    lnumb += 1
                elif lhy in line:
                    line = line.split()
                    if len(line) == 5:
                        hy = "%s\t%s\t%s\n" % (
                            lhy, line[1], line[2].replace(lxz, ''))
                    else:
                        hy = "%s\t%s\n" % (lhy, line[2].replace(lgm, ''))

                    xz = "%s\t%s\n" % (lxz, line[-2].replace(lgm, ''))
                    gm = "%s\t%s\n" % (lgm, line[-1])
                    text.extend([hy, xz, gm])
                    lnumb += 1
                elif lnumb == 2:
                    text.append("%s %s" % (lmc, line))
                elif lnumb == 3:
                    text.append("%s %s" % (ljj, line))
                    lnumb = 1
                else:
                    continue
        wfd.writelines(text)


def text_format_v2(sf, df):
    """Text format v2 after watching the video"""
    with open(sf, 'r') as rfd, open(df, 'w') as wfd:
        for line in rfd:
            if '***编号****' in line:
                wfd.write(line)
                rfd.next()
                # line = rfd.next()
                wfd.write('公司名称：' + rfd.next())
            elif '公司行业：' in line:
                slen = len('公司行业：')
                # f1 = line.find('公司行业：')
                f2 = line.find('公司性质：')
                f3 = line.find('公司规模：')
                wfd.write('公司行业：' + line[slen:f2] + '\n')
                wfd.write(line[f2:f3] + '\n')
                wfd.write(line[f3:])
            else:
                wfd.write('公司简介：')
                while '***编号****' not in line:
                    line1 = line.strip(os.linesep).strip()
                    if line:
                        wfd.write(line1)
                    line = rfd.next()
                wfd.write('\n')
                wfd.write(line)
                rfd.next()
                wfd.write('公司名称：' + rfd.next())

if __name__ == '__main__':
    src_file = 'test.txt'
    dst_file = 'formatted.txt'
    try:
        # text_format_v1(src_file, dst_file)
        text_format_v2(src_file, dst_file)
    except BaseException, e:
        print e
