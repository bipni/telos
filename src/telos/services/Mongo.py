from pymongo import MongoClient


class Mongo:
    def __init__(self, hosts: list, ports: list):
        self._clients = {}

        for i in range(len(hosts)):
            self._clients[f'{hosts[i]}:{ports[i]}'] = MongoClient(
                hosts[i], int(ports[i]))

    def get_client(self, client: str):
        if client in self._clients:
            return self._clients[client]
        else:
            raise Exception('Client Not Found')
