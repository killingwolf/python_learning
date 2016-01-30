#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/18 20:56
# @Author  : killingwolf (killingwolf@qq.com)
import web
import datetime

db = web.database(dbn='mysql', db='webpyblog', user='root',passwd='123456')


def get_posts():
    return db.select('entries', order='id DESC')


def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None


def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())


def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())


def update_post(id, title, text):
    db.update('entries', where="id=$id", vars=locals(),
              title=title, content=text)

def page_post(page):
    perpage = 3
    offset = (int(page) - 1 ) * perpage
    posts = db.select("entries", order='id DESC', offset=offset, limit=perpage)
    postcount = db.query("SELECT COUNT(*) AS count FROM entries")[0]
    return posts, postcount
