from src.telos.services.Container import Container
from src.telos.helpers.Response import response
from .Controller import Controller

import simplejson

class Routes:
    def __init__(self, container):
        self.container = container

    def base_path(self, path: str):
        return '/passwords' + path

    def password(self):
        c = Controller(self.container)
        c.insert_one({"name": "bipni"})
        return "done", 200

def register_routes(container: Container):
    server = container.get('flask')
    r = Routes(container)
    
    print("Registering Passwords Routes")
    server.register_routes(r.base_path(''), 'Password', r.password)