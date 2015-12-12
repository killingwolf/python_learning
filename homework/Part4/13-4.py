#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-10 18:48:15
# @Author  : killingwolf (killingwolf@qq.com)

import time
import shelve
# from base64 import encodestring as ecdstr
# from base64 import encodestring as dcdstr


class UserData(object):

    def __init__(self, user_data_file='userdata.txt'):
        self.timestamp = time.time()
        self.data = shelve.open(user_data_file)

    def user_check(self, user):
        'check if the user is exist'
        rt = True if user in self.data else False
        return rt

    def login(self, user, password):
        if self.user_check(user):
            if password == self.data[user][0]:
                if self.timestamp - self.data[user][1] <= 14400:
                    lastlogin = time.ctime(self.data[user][1])
                    print "Last login at:{0}".format(lastlogin)
                self.data[user] = [password, self.timestamp, 1]
            else:
                print 'Permission deny or duser not exist'

        else:
            print "{0} is't exist".format(user)

    def logout(self, user):
        if self.user_check(user):
            password = self.data[user][0]
            timestamp = self.data[user][1]
            islogin = self.data[user][2]
            if islogin:
                self.data[user] = [password, timestamp, 0]

    def update(self, user, upuser, uppassword):
        isexist = self.user_check(upuser)
        if isexist and self.data[user][2]:
            if user == upuser:
                self.data[user] = [
                    uppassword,
                    time.time(),
                    self.data[user][2]
                ]
            elif user == 'admin':
                self.data[upuser] = [
                    uppassword,
                    self.data[user][1],
                    self.data[user][2]
                ]
            else:
                print "Permission deny or user not exist"
        else:
            print "Please Login"

    def register(self, user, password):
        islogin = 0
        isexist = self.user_check(user)
        if isexist:
            print "{0} already exist".format(user)
        else:
            self.data[user] = [password, self.timestamp, islogin]
            print "{0} register ok".format(user)

    def user_list(self, user):
        isexist = self.user_check(user)
        if user == 'admin' and isexist and self.data[user][2]:
            for k in self.data:
                print k, self.data[k][0]
        else:
            print "Permission deny or user not exist"

    def user_delete(self, user, duser):
        isexist = self.user_check(user)
        if isexist and self.data[user][2]:
            if self.user_check(duser):
                if user == duser:
                    del self.data[duser]
                elif user == 'admin':
                    del self.data[duser]
                else:
                    print "Permission deny or duser not exist"
        else:
            print "Please Login"

    def __del__(self):
        self.data.close()


if __name__ == '__main__':
    userdata = UserData()
    userdata.register('admin', '123456')
    userdata.register('user1', 'user1')
    userdata.register('abc', 'abc')
    print "#" * 40
    userdata.login('admin', '123456')
    # userdata.logout('admin')
    print 'all users:'
    userdata.user_list('admin')
    print "*" * 40
    userdata.update('admin', 'user1', 'xxxxxx')
    print 'all users after update:'
    userdata.user_list('admin')
    print "*" * 40
    userdata.user_delete('admin', 'user1')
    userdata.user_delete('admin', 'abc')
    print 'all users after deltete:'
    userdata.user_list('admin')
    # userdata.update('admin')
