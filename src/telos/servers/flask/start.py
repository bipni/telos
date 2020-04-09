from src.telos.services.Container import Container

from flask import Flask

class FLASK:
    def __init__(self, container: Container):
        self.container = container
        self.config = container.get('config')
        self.app = Flask(__name__)
        self.host = self.config['flask']['host']
        self.port = int(self.config['flask']['port'])
    
    def start(self):
        print("Flask Server Started at Host: %s and Port: %s" % (self.host, self.port))
        self.app.run(self.host, self.port)

def run(container: Container):
    flask = FLASK(container)
    container.singleton('flask', flask)
    flask.start()