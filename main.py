# import modules
import os
import web
import random
import urllib.request
import json

# url = 'http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25'
#
#
# def getRandomMadlibs(url):
#     madLibUrl = urllib.request.urlopen(url)
#     print('Madlib', str(madLibUrl.getcode()))
#     madLib = json.load(madLibUrl)
#     print(madLib)

# set urls

urls = (
    '/',
    'index',
    '/api',
    'api',
    '/api/(.*)',
    'getMadlibs'
)

# setup app and render

webApp = web.application(urls, globals())
render = web.template.render('templates/', base="layout")


# / Route
class Index(object):
    def GET(self):
        return render.index(output="", title="")

    def POST(self):
        form = web.input()
        output = ""
        title = form["title"]
        for i in range(0, len(form) / 2):
            v = "v" + str(i) if "v" + str(i) in form else ""
            b = "b" + str(i)
            if v in form:
                output += form(v)
            if b in form:
                output += form(b)
        return render.index(output, title=title)


# /api route
class Api(object):
    def GET(self):
        return render.api()


# /api/random route


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webApp.run()
