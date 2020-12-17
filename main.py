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
class index(object):
    def GET(self):
        return render.index(output="", title="")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webApp.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
