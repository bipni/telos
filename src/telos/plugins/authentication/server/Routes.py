from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.controllers.UserController import UserController
from src.telos.plugins.authentication.server.controllers.LoginController import LoginController

from flask import jsonify


class Routes:
    def __init__(self, container):
        self.container = container

    def base_path(self, path: str):
        return '/auth' + path

    def authentication(self):
        return (jsonify(dict(
            status=True,
            message="Authentication"
        )), 200)


def register_routes(container: Container):
    server = container.get('flask')
    routes = Routes(container)
    user = UserController(container)
    login = LoginController(container)

    print("Registering Authentication Routes")

    server.register_routes(routes.base_path(
        ''), 'Authentication', routes.authentication)

    server.register_routes(routes.base_path('/signup'),
                           'SignUp', user.signup, methods=['POST'])
    server.register_routes(routes.base_path('/update'),
                           'Update', user.update_user, methods=['POST'])
    server.register_routes(routes.base_path('/login'),
                           'Login', login.login, methods=['POST'])
    server.register_routes(routes.base_path('/logout'),
                           'Logout', login.logout, methods=['GET'])
