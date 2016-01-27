#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/1/21 14:38
# @Author  : killingwolf (killingwolf@qq.com)

import web
import module

# URL mappings
urls = (
    '/', 'Index',
    '/view', 'View',
    '/add', 'Add',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
    '/search', 'Search',
)

# Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)
# render = web.template.render('templates', globals={})

class Index:

    def GET(self):
        """ Show page """
        return render.index()


class Add(object):

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull,
                         size=30,
                         description="姓名："),
        web.form.Textarea('address', web.form.notnull,
                         rows=2, cols=32,
                         description="地址："),
        web.form.Textbox('tel', web.form.notnull,
                         size=30,
                         description="电话："),
        web.form.Button('Add'),
    )

    def GET(self):
        form = self.form()
        return render.add(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.add(form)
        module.add_item(form.d.name, form.d.address, form.d.tel)
        raise web.seeother('/view')

class Delete(object):
    def POST(self, id):
        module.del_item(int(id))
        raise web.seeother('/view')

class Search(object):
    form = web.form.Form(
        web.form.Dropdown(None, [
            ('name', '姓名'),
            ('address', '地址'),
            ('tel', '电话' )]),
        web.form.Textbox('name', web.form.notnull,
                         size=30,
                         description="姓名："),
        web.form.Textarea('address', web.form.notnull,
                         rows=2, cols=32,
                         description="地址："),
        web.form.Textbox('tel', web.form.notnull,
                         size=30,
                         description="电话："),
        web.form.Button('Search'),
    )
    def GET(self):
        """ Search item """
        return render.search(self.form)

class Edit(object):

    def GET(self, id):
        post = module.get_item(int(id))
        if not post:
            raise web.seeother('/')
        form = Add.form()
        form.fill(post)
        return render.edit(post, form)

    def POST(self, id):
        form = Add.form()
        post = module.get_item(int(id))
        if not form.validates():
            return render.edit(post, form)
        module.update_item(id, form.d.name, form.d.address, form.d.tel)
        raise web.seeother('/view')

class View(object):
    def GET(self):
        """ Show page """
        items = module.get_items()
        return render.list(items)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
