from fabric.api import *
import os

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
        
def build():
    local('mynt -f src build')
    local('rsync -r build/ ./')

def deploy():
    pass

def runserver():
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    import BaseHTTPServer
    server_address = ('localhost', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print "Running server on http://%s:%s ..." % server_address
    httpd.serve_forever()
