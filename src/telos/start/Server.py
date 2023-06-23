from src.telos.services.Container import Container

from src.telos.providers.ConfigProvider import ConfigProvider
from src.telos.providers.EventsProvider import EventsProvider
from src.telos.providers.MongoProvider import MongoProvider

import importlib
import threading


def run():
    container = Container()

    ConfigProvider(container)
    EventsProvider(container)

    config = container.get('config')
    databases = config['databases'].replace(' ', '').split(',')
    server_types = config['servers'].replace(' ', '').split(',')

    for database in databases:
        if database == 'mongo':
            MongoProvider(container)

    for server_type in server_types:
        package = f"src.telos.servers.{server_type}.Start"

        if importlib.util.find_spec(package) is not None:
            mod = importlib.import_module(package)

            if 'run' in dir(mod):
                server = threading.Thread(target=mod.run, args=(container,))
                server.start()
            else:
                print(f"run method not defined in {server_type} server")
