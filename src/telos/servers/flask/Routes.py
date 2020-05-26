from src.telos.services.Container import Container

from flask import jsonify

class Routes:
    def __init__(self, container: Container):
        self.container = container
    
    def index(self):
        return (jsonify(dict(
            status = 200,
            message = "Telos"
        )), 200)

def register_routes(container: Container):
    server = container.get('flask')

    routes = Routes(container)

    server.register_routes('/', 'index', routes.index)