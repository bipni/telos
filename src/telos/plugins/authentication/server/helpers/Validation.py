from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.Login import Login
from src.telos.plugins.authentication.server.repositories.User import User

from flask import jsonify
import time


class Validation:
    def __init__(self, container: Container):
        self.container = container
        self.loginRepo = self.container.get(Login)
        self.userRepo = self.container.get(User)

    def LoginValidation(self, login_token: str):
        login_details = self.loginRepo.find_one({'token': login_token})

        if login_details is None:
            return None, "Invalid Token"

        if login_details['expired']:
            return None, "Login is Expired"

        if login_details['expired_at'] < time.time():
            login_details['expired'] = True
            self.loginRepo.update_one({'token': login_token}, login_details)
            return None, "Login is Expired"
        else:
            login_details['expired_at'] = time.time() + 60*60

        user_id = login_details['user_id']

        return user_id, None

    def UsernameValidation(self, username: str):
        if not username.replace('_', '').isalnum():
            return "Username can only have alphanumeric characters and underscores"

        if len(username) < 4:
            return "Username must be at least 4 characters in length"

        existing_user = self.userRepo.find_one({'username': username})

        if existing_user is not None:
            return "Username is not available"

        return None

    def PasswordValidation(self, password: str):
        if len(password) < 6:
            return "Password must be at least 6 characters in length"

        return None
