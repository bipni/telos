from src.telos.services.Container import Container
from src.telos.repositories.MongoRepository import MongoRepository

class Registration(MongoRepository):
    def db(self):
        return 'authentication'

    def collection(self):
        return 'authentication'