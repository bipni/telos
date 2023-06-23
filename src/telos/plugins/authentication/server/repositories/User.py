from src.telos.services.Container import Container
from src.telos.repositories.MongoRepository import MongoRepository


class User(MongoRepository):

    '''
    data model:
        {
            'name': name
            'email': email
            'username': username
            'password': password
            'locked': account lock status
            'attempts': max number of invalid attempts
            'created_at' = creation time
        }
    '''

    def db(self):
        return 'authentication'

    def collection(self):
        return 'user'
