from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.User import User
from src.telos.plugins.authentication.server.repositories.Login import Login

def register_repositories(container: Container):
    user = User(container)
    login = Login(container)

    container.singleton('user', user)
    container.singleton('login', login)