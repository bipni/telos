from src.telos.services.Container import Container
from src.telos.services.Mongo import Mongo

import time

class MongoRepository:
    def __init__(self, container: Container):
        self._container = container
        self._mongo = self._container.get(Mongo)
        self._client = self._mongo.get_client(self.client())
        self._db = self._client[self.db()]
        self._col = self._db[self.collection()]

    def client(self):
        return 'localhost:27017'

    def db(self):
        return 'telos'

    def collection(self):
        return 'default'

    def insert_one(self, data: dict):
        data['created_at'] = time.time()
        res = self._col.insert_one(data)
        return res.inserted_id

    def insert_many(self, data: list):
        data['created_at'] = time.time()
        res = self._col.insert_many(data)
        return res.inserted_ids

    def find_one(self, query: dict):
        res = self._col.find_one(query)
        return res

    def find_all(self, query: dict):
        res = self._col.find(query)
        return res

    def delete_one(self, query: dict):
        res = self._col.delete_one(query)
        return res

    def delete_many(self, query: dict):
        res = self._col.delete_one(query)
        return res.deleted_count

    def update_one(self, query: dict, data: dict):
        data['updated_at'] = time.time()

        values = {
            '$set': data
        }

        res = self._col.update_one(query, values)
        return res

    def update_many(self, query: dict, data: dict):
        data['updated_at'] = time.time()

        values = {
            '$set': data
        }

        res = self._col.update_many(query, values)
        return res.modified_count
