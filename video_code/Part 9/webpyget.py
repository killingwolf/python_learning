
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/16 17:01
# @Author  : killingwolf (killingwolf@qq.com)

import web

urls = (
    '/', 'index',
    '/test', 'test',
    '/page?', 'page',
    '/topic/(\d+)', 'topic',
    '/hello/(.*)', 'hello'
)


class index:

    def GET(self):
        return 'Hello, world!'


class test(object):

    def GET(self):
        return '''web.py test'''


class page(object):

    def GET(self):
        i = web.input()
        return 'from page ' + str(i)


class topic(object):

    def GET(self, name):
        return 'from topic ' + name


class hello(object):

    def GET(self, name):
        return 'from hello ' + name


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
