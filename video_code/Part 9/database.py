#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/18 10:47
# @Author  : killingwolf (killingwolf@qq.com)

import sys
import MySQLdb

host = '127.0.0.1'
user = 'root'
password = '123456'
port = 3306
database = 'webpy'

con = MySQLdb.connect(host, user, password, database, port, charset='utf8')

with con:
    cur = con.cursor()
    # SELECT
    select = "SELECT * FROM STUDY"
    cur.execute(select)
    for line in cur.fetchall():
        for word in line:
            print word,
        print
    print '#' * 79
    # DELETE
    delete = "DELETE FROM STUDY WHERE TEL='9999'"
    cur.execute(delete)
    # INSERT
    insert = "INSERT INTO study(name, address, tel) values('ben', 'USA','9999')"
    cur.execute(insert)
    # UPDATE
    update = "UPDATE study set tel='19999999999' where tel='9999'"
    cur.execute(update)

