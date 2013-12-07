import web
import model

# Render templates
render = web.template.render('templates', base='base')

# Url mappings
urls = (
    '/', 'Index',
    '/del', 'Delete'
)

class Index:
    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull,
            description="Name"),
        web.form.Textbox('email', web.form.notnull,
            description="Email"),
        web.form.Button('Add')
    )

    def GET(self):
        listActiveSubs = model.listActiveSubscribers()
        form = self.form()
        return render.index(list_active_subs,form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            listActiveSubs = model.listActiveSubscribers()
            return render.index(listActiveSubs,form)
        model.newSub(form.d.name, form.d.email)
        raise web.seeother('/')

class Delete:
    """ Delete an entry """
    def GET(self):
        data = web.input()
        return model.delSub(data.email)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
