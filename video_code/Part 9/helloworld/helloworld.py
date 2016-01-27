
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/16 17:01
# @Author  : killingwolf (killingwolf@qq.com)

import web
import datetime

urls = (
    '/', 'index',
    '/test?', 'test',
    '/db', 'Db',
    '/add', 'add',
    '/test2/(.*)', 'test2',
)

render = web.template.render('templates/')
db = web.database(dbn='mysql', db='webpyblog', user='root',passwd='123456' )

class index:
    def GET(self):
        name = 'killingwolf'
        return render.index(None)
        # return render.index(name)


class test(object):
    def GET(self):
        i = web.input(name=None)
        return render.index(i.name)


class test2(object):
    def GET(self, name=None):
        return render.index(name)

class Db(object):
    def GET(self):
        todos = db.select('entries')
        return render.dbs(todos)

class add(object):
    def POST(self):
        i = web.input()
        db.insert('entries', title=i.title, content=i.content,
                  posted_on=datetime.datetime.utcnow())
        raise web.seeother('/db')

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
