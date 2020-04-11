from src.telos.services.Container import Container
from src.telos.plugins.contacts.server.Routes import register_routes as routes

def register_routes(container: Container):
    routes(container)