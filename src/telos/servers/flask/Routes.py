from src.telos.services.Container import Container
from src.telos.helpers.Response import response

class Routes:
    def __init__(self, container: Container):
        self.container = container
    
    def index(self):
        return response(200, "Index")

def register_routes(container: Container):
    server = container.get('flask')

    routes = Routes(container)

    server.register_routes('/', 'index', routes.index)