from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.User import User
from src.telos.plugins.authentication.server.helpers.Validation import Validation

from flask import request, jsonify
import hashlib


class UserController:
    def __init__(self, container: Container):
        self.container = container
        self.userRepo = self.container.get(User)
        self.validation = Validation(self.container)

    def signup(self):
        mendatory_fields = ['name', 'email', 'username', 'password']

        for mendatory_field in mendatory_fields:
            if request.form.get(mendatory_field) is None:
                return (jsonify(dict(
                    success=False,
                    error_message="Mendatory Field %s Missing" % mendatory_field
                )), 404)

        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        err = self.validation.UsernameValidation(username)
        if err is not None:
            return (jsonify(dict(
                success=False,
                error_message=err
            )), 400)

        err = self.validation.PasswordValidation(password)
        if err is not None:
            return (jsonify(dict(
                success=False,
                error_message=err
            )), 400)

        new_user = dict(
            name=name,
            email=email,
            username=username,
            password=str(hashlib.sha1(bytes(password, 'utf-8')).hexdigest()),
            locked=False,
            attempts=5
        )

        res = self.userRepo.insert_one(new_user)

        return (jsonify(dict(
            success=True,
            message="Sign Up Successful"
        )), 200)

    def update_user(self):
        login_token = request.headers.get('login-token')
        user_id, err = self.validation.LoginValidation(login_token)

        if err is not None:
            return (jsonify(
                status=False,
                error_message=err
            ), 401)

        data = {}

        updated_data = dict(request.form)

        if 'name' in updated_data and not updated_data['name'] == '':
            data['name'] = updated_data['name']

        if 'email' in updated_data and not updated_data['email'] == '':
            data['email'] = updated_data['email']

        if 'username' in updated_data:
            err = self.validation.UsernameValidation(updated_data['username'])
            if err is not None:
                return (jsonify(dict(
                    success=False,
                    error_message=err
                )), 400)

            data['username'] = updated_data['username']

        if 'password' in updated_data:
            err = self.validation.PasswordValidation(updated_data['password'])
            if err is not None:
                return (jsonify(dict(
                    success=False,
                    error_message=err
                )), 400)

            data['password'] = str(hashlib.sha1(
                bytes(updated_data['password'], 'utf-8')).hexdigest())

        self.userRepo.update_one({'_id': user_id}, data)

        return (jsonify(
            status=True,
            message="User Updated Successfully"
        ), 200)
