#!/usr/bin/env python3
import config
import cherrypy
from cherrypy.lib import static
import os
import display

class Page(object):
    @cherrypy.expose
    def index(self):
        return config.get_main()

    @cherrypy.expose
    def scene(self, s, m=None):
        if m:
            return config.get_mood(s, m)
        else:
            return config.get_scene(s)

    @cherrypy.expose
    def displaybg(self, d):
        return static.serve_file(os.path.abspath(os.getcwd())+"/"+display.get())

    @cherrypy.expose
    def display(self):
        return display.get_js()

    @cherrypy.expose
    def image(self):
        display.set("assets/forest.png")
        return "ok"

    @cherrypy.expose
    def image2(self):
        display.set("assets/graves.png")
        return "ok"

    @cherrypy.expose
    def generate(self, length=8):
        return "hi from {}".format(length)

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './assets'
        }
    }
    config.load_config('./config.yml')
    config.debug()
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 8082
    cherrypy.server.shutdown_timeout = 1
    cherrypy.quickstart(Page(), '/', conf)
