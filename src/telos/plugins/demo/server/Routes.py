from src.telos.services.Container import Container
from src.telos.plugins.demo.server.repositories.Controller import Controller

from flask import jsonify

class Routes:
    def __init__(self, container):
        self.container = container

    def base_path(self, path: str):
        return '/demo' + path

    def demo(self):
        c = Controller(self.container)
        c.insert_one({"name": "bipni"})
        return "done", 200

def register_routes(container: Container):
    server = container.get('flask')
    r = Routes(container)
    
    print("Registering Demo Routes")
    server.register_routes(r.base_path(''), 'Demo', r.demo)