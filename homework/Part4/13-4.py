#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-10 18:48:15
# @Author  : killingwolf (killingwolf@qq.com)

import time


class UserData(object):

    timestamp = time.localtime()

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.timestamp = timestamp

    def login(self):
        pass

    def logout(self):
        pass

    def update(self):
        pass

    def register(self):
        pass

    def __del__(self):
        pass

if __name__ == '__main__':
    user1 = UserData('admin', 'password')
