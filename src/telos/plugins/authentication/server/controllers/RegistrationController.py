from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.Registration import Registration

from flask import request, jsonify
import hashlib

class RegistrationController:
    def __init__(self, container: Container):
        self.container = container
        self.registrationRepo = self.container.get(Registration)

    def signup(self):
        mendatory_fields = ['name', 'email', 'username', 'password']

        for mendatory_field in mendatory_fields:
            if request.form.get(mendatory_field) is None:
                return (jsonify(dict(
                    success = False,
                    error_message = "Mendatory Field %s Missing" % mendatory_field
                )), 404)

        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if not username.replace('_', '').isalnum():
            return (jsonify(dict(
                success = False,
                error_message = "Username can only have alphanumeric characters and underscores"
            )), 400)

        if len(username) < 4:
            return (jsonify(dict(
                success = False,
                error_message = "Username must be at least 4 characters in length"
            )), 400)

        if len(password) < 6:
            return (jsonify(dict(
                success = False,
                error_message = "Password must be at least 6 characters in length"
            )), 400)

        existing_user = self.registrationRepo.find_one({'username': username})

        if existing_user is not None:
            return (jsonify(dict(
                success = False,
                error_message = "Username is not available"
            )), 400)

        new_user = dict(
            name = name,
            email = email,
            username = username,
            password = str(hashlib.sha1(bytes(password, 'utf-8')).hexdigest())
        )

        res = self.registrationRepo.insert_one(new_user)

        return (jsonify(dict(
            success = True,
            message = "Sign Up Successful"
        )), 200)
