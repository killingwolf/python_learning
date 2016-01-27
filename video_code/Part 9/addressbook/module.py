#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/21 14:39
# @Author  : killingwolf (killingwolf@qq.com)
import web
import datetime

DBN = 'mysql'
DB = 'addressbook'
TB = 'address'
USER = 'root'
PASSWORD = '123456'


db = web.database(dbn=DBN, db=DB, user=USER, passwd=PASSWORD)


def get_items():
    return db.select(TB, order='id DESC')


def get_item(id):
    try:
        return db.select(TB, where='id=$id', vars=locals())[0]
    except IndexError:
        return None


def add_item(name, address, tel):
    db.insert(TB, name=name, address=address, tel=tel)


def del_item(id):
    db.delete(TB, where="id=$id", vars=locals())


def update_item(id, name, address, tel):
    db.update(TB, where="id=$id", vars=locals(), name=name,
              address=address, tel=tel)