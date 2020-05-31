from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.Login import Login
from src.telos.plugins.authentication.server.repositories.User import User

from flask import jsonify

class Validation:
    def __init__(self, container):
        self.container = container
        self.loginRepo = self.container.get(Login)
        self.userRepo = self.container.get(User)

    def LoginValidation(self, login_token):
        login_details = self.loginRepo.find_one({'token': login_token})

        if login_details is None:
            return None, "Invalid Token"

        if login_details['expired']:
            return None, "Login is Expired"

        user_id = login_details['user_id']

        return user_id, None

    def UsernameValidation(self, username):
        if not username.replace('_', '').isalnum():
            return "Username can only have alphanumeric characters and underscores"

        if len(username) < 4:
            return "Username must be at least 4 characters in length"

        existing_user = self.userRepo.find_one({'username': username})

        if existing_user is not None:
            return "Username is not available"

        return None

    def PasswordValidation(self, password):
        if len(password) < 6:
            return "Password must be at least 6 characters in length"

        return None