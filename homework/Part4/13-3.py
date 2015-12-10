#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-10 10:38:59
# @Author  : killingwolf (killingwolf@qq.com)


class MoneyFmt(object):

    def __init__(self, value=0.0, sigal=False):
        if isinstance(value, float):
            self.value = value
            self.sigal = sigal
        else:
            raise (TypeError, 'value must be float')

    def update(self, value=None, sigal=False):
        self.__init__(value, sigal)
        # if isinstance(value, float):
        #     self.value = value
        #     self.sigal = sigal
        # else:
        #     raise (TypeError, 'value must be float')

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        value = self.value
        sigal = self.sigal
        if isinstance(value, float):
            if value > 0:
                negtive = False
            else:
                negtive = True

            value = str(round(abs(value), 2)).split('.')
            val = list(value[0])
            lenth, head = divmod(len(val), 3)

            # 整形部分长度大于3才插入‘，’
            if head and lenth:
                val.insert(head, ',')

            if head:
                for i in xrange(1, lenth):
                    val.insert(4 * i + head, ',')
            else:
                for i in xrange(1, lenth):
                    val.insert(3 * i, ',')

            value[0] = ''.join(val)

            if negtive:
                if sigal:
                    rt = '<' + '.'.join(value) + '$>'
                else:
                    rt = '-$' + '.'.join(value)
            else:
                rt = '$' + '.'.join(value)
        else:
            raise (TypeError, "value must be float")

        return rt

    def __nonzero__(self):
        return False if self.value == 0 else True


if __name__ == '__main__':
    p = MoneyFmt(10.099)
    print p
    p.update(100.355)
    print p
    p.update(-100.995)
    print p
    p.update(-1000.995, sigal=True)
    print p
    p.update(-10000.995)
    print p
    p.update(-100000.995)
    print p
    p.update(-1000000.995)
    print p
