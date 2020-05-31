from src.telos.services.Container import Container
from src.telos.repositories.MongoRepository import MongoRepository

class Login(MongoRepository):

    '''
    data model:
        {
            'user_id': user mongo id
            'token': token id
            'remote_addr': remote ip adress
            'expired': expiration status
            'created_at' = creation time
            'expired_at' = expiration time
        }
    '''
    def db(self):
        return 'authentication'

    def collection(self):
        return 'login'