from src.telos.services.Container import Container
from src.telos.plugins.authentication.server.repositories.Registration import Registration

from flask import request, jsonify

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
        email = request.form.get('name')
        username = request.form.get('name')
        password = request.form.get('name')

        return 'ok'
