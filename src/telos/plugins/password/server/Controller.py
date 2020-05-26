from src.telos.repositories.MongoRepository import MongoRepository
from src.telos.services.Container import Container

class Controller(MongoRepository):
    def client(self):
        return 'localhost:27017'

    def db(self):
        return 'telos'

    def collection(self):
        return 'test'