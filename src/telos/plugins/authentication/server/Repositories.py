from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.Registration import Registration

def register_repositories(container: Container):
    registration = Registration(container)

    container.singleton('registraion', registration)