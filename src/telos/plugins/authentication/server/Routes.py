from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.controllers.UserController import UserController

from flask import jsonify

class Routes:
    def __init__(self, container):
        self.container = container

    def base_path(self, path: str):
        return '/auth' + path

    def authentication(self):
        return (jsonify(dict(
            status = True,
            message = "Authentication"
        )), 200)

def register_routes(container: Container):
    server = container.get('flask')
    routes = Routes(container)
    user = UserController(container)

    print("Registering Authentication Routes")

    server.register_routes(routes.base_path(''), 'Authentication', routes.authentication)

    server.register_routes(routes.base_path('/signup'), 'SignUp', user.signup, methods=['POST'])
    server.register_routes(routes.base_path('/login'), 'Login', user.login, methods=['POST'])