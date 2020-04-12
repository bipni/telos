from pymongo import MongoClient

class Mongo:
    def __init__(self, hosts: list, ports: list, db_names: list):
        self._dbs = {}
        self._clients = {}

        for i in range(len(hosts)):
            self._clients[f'{hosts[i]}:{ports[i]}:{db_names[i]}'] = MongoClient(hosts[i], int(ports[i]))
        
        print(self._clients)