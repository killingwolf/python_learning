#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: killingwolf
# Email: killingwolf@qq.com
""" This is a simple GUI module
"""

from functools import partial
import Tkinter

if __name__ == '__main__':
    root = Tkinter.Tk()
    MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
    b1 = MyButton(text='周一')
    b2 = MyButton(text='周二')
    b3 = MyButton(text='周三')
    b4 = MyButton(text='周四')
    b5 = MyButton(text='周五')
    b6 = MyButton(text='周六')
    b7 = MyButton(text='周日')
    qb = MyButton(text='QUIT', bg='red', command=root.quit)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    b6.pack()
    b7.pack()
    qb.pack(fill=Tkinter.X, expand=True)
    root.title('工作目录')
    root.mainloop()
