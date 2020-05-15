from src.telos.services.Container import Container
from src.telos.services.Mongo import Mongo

def MongoProvider(container: Container):
    config = container.get('config')['mongo']

    hosts = config['hosts'].replace(' ', '').split(',')
    ports = config['ports'].replace(' ', '').split(',')

    if len(hosts) == len(ports):
        Mongo(hosts, ports)
    else:
        raise Exception('Mongo DB Hosts and Ports Mismatch')