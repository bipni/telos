from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.Routes import register_routes as routes
from src.telos.plugins.authentication.server.Events import register_events as events
from src.telos.plugins.authentication.server.Repositories import register_repositories as repositories

def register_routes(container: Container):
    routes(container)

def register_events(container: Container):
    events(container)

def register_repositories(container: Container):
    repositories(container)