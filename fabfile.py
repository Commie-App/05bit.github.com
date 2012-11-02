from fabric.api import *
import os

BUILD_DIR = '.build'
PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
        
def build():
    if os.path.exists(BUILD_DIR):
        local('rm -r %s' % BUILD_DIR)
    local('mynt gen -f src %s' % BUILD_DIR)
    local('rsync -r %s/ %s/' % (BUILD_DIR, PROJECT_DIR))

def deploy():
    pass

def runserver():
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    import BaseHTTPServer
    server_address = ('localhost', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print "Running server on http://%s:%s ..." % server_address
    httpd.serve_forever()
