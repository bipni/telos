from src.telos.services.Container import Container
from src.telos.helpers.Response import response

import simplejson

def base_path(path: str):
    return '/passwords' + path

def password():
    return response(200, "Passwords")

def register_routes(container: Container):
    server = container.get('flask')
    
    print("Registering Passwords Routes")
    server.register_routes(base_path(''), 'Password', password)