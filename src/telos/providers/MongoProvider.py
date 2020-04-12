from src.telos.services.Container import Container
from src.telos.services.Mongo import Mongo

def MongoProvider(container: Container):
    config = container.get('config')['mongo']

    hosts = config['hosts'].replace(' ', '').split(',')
    ports = config['ports'].replace(' ', '').split(',')
    db_names = config['names'].replace(' ', '').split(',')

    hosts_len = len(hosts)
    ports_len = len(ports)
    db_names_len = len(db_names)

    max_value = max(hosts_len, ports_len, db_names_len)
    
    while not hosts_len == max_value:
        hosts.append(hosts[hosts_len-1])
        hosts_len = len(hosts)
    
    while not ports_len == max_value:
        ports.append(ports[ports_len-1])
        ports_len = len(ports)
    
    while not db_names_len == max_value:
        db_names.append(db_names[db_names_len-1])
        db_names_len = len(db_names)

    Mongo(hosts, ports, db_names)