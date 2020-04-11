from src.telos.services.Container import Container
from src.telos.helpers.Response import response

import simplejson

def base_path(path: str):
    return '/contacts' + path

def contact():
    return response(200, "Contacts")

def register_routes(container: Container):
    server = container.get('flask')
    
    print("Registering Contacts Routes")
    server.register_routes(base_path(''), 'Contacts', contact)