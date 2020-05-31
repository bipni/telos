from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.User import User
from src.telos.plugins.authentication.server.repositories.Login import Login

from flask import request, jsonify
import hashlib
import uuid
import time

class LoginController:
    def __init__(self, container: Container):
        self.container = container
        self.userRepo = self.container.get(User)
        self.loginRepo = self.container.get(Login)

    def login(self):
        username = request.form.get('username')
        password = request.form.get('password')

        user = self.userRepo.find_one({'username': username})

        if user is None:
            return (jsonify(dict(
            success = False,
            error_message = "Incorrect Username"
        )), 401)

        if user['locked']:
            return (jsonify(dict(
                success = False,
                error_message = "Account is disabled"
            )), 401)

        hashed_password = str(hashlib.sha1(bytes(password, 'utf-8')).hexdigest())

        if not user['password'] == hashed_password:
            user['attempts'] = user['attempts'] - 1

            if user['attempts'] == 0:
                user['locked'] = True

            self.userRepo.update_one({'username': username}, user)

            return (jsonify(dict(
            success = False,
            error_message = "Incorrect Password"
        )), 401)

        login_details = self.loginRepo.find_one({
            'user_id': user['_id'],
            'expired': False
        })

        if login_details is None:
            login_token = self.get_login_token(user['_id'], request.remote_addr)
        else:
            if login_details['expired_at'] < time.time():
                login_details['expired'] = True
                self.loginRepo.update_one({'user_id': user['_id'], 'expired': False}, login_details)
                login_token = self.get_login_token(user['_id'], request.remote_addr)
            else:
                login_token = login_details['token']

        return (jsonify(dict(
            success = True,
            token = login_token,
            message = "Login Successful"
        )), 200)

    def get_login_token(self, user_id, remote_addr):
        token = uuid.uuid4().hex

        login_info = dict(
                user_id = user_id,
                token = token,
                remote_addr = remote_addr,
                expired = False,
                expired_at = time.time() + 60*60
            )

        self.loginRepo.insert_one(login_info)

        return token