from src.telos.services.Container import Container

import http.server
import socketserver

class HTTP:
    def __init__(self, container: Container):
        self.container = container
        self.config = container.get('config')
        self.host = self.config['http']['host']
        self.port = int(self.config['http']['port'])
    
    def start(self):
        print("HTTP Server Started at Host: %s and Port: %s" % (self.host, self.port))
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", self.port), Handler)
        httpd.serve_forever()

def run(container: Container):
    http = HTTP(container)
    container.singleton('http', http)
    http.start()