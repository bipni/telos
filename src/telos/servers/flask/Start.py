from src.telos.services.Container import Container
from src.telos.servers.flask.Routes import register_routes
from src.telos.servers.flask.Plugins import register_plugins

from typing import Callable
from flask import Flask
from flask_cors import CORS
from waitress import serve

class FLASK:
    def __init__(self, container: Container):
        self.container = container
        self.config = container.get('config')
        self.app = Flask(__name__)
        self.host = self.config['flask']['host']
        self.port = int(self.config['flask']['port'])
        CORS(self.app)
    
    def register_routes(self, endpoint: str, name: str, handler: Callable, methods: list = ['POST', 'GET']):
        self.app.add_url_rule(endpoint, name, handler, methods = methods)
    
    def start(self):
        print("Flask Server ", end='')
        serve(self.app, host=self.host, port=self.port)

def run(container: Container):
    flask = FLASK(container)
    container.singleton('flask', flask)

    register_routes(container)
    register_plugins(container)

    flask.start()