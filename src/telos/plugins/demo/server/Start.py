from src.telos.services.Container import Container
from src.telos.plugins.demo.server.Routes import register_routes as routes
from src.telos.plugins.demo.server.Events import register_events as events


def register_routes(container: Container):
    routes(container)


def register_events(container: Container):
    events(container)
