from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.User import User

def register_repositories(container: Container):
    user = User(container)

    container.singleton('user', user)