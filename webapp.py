#!/usr/bin/env python3
import cherrypy
import os
import display

class Page(object):
    @cherrypy.expose
    def index(self):
        return "hi!"

    @cherrypy.expose
    def image(self):
        display.set("pie.jpg")
        return "ok"

    @cherrypy.expose
    def image2(self):
        display.set("waffle.jpg")
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
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    display.init(cherrypy.engine.exit)
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 8082
    cherrypy.server.shutdown_timeout = 1
    cherrypy.quickstart(Page(), '/', conf)
