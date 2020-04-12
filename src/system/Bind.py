from src.telos.services.Container import Container
from src.telos.providers.ConfigProvider import ConfigProvider
from src.telos.providers.EventsProvider import EventsProvider
from src.telos.providers.MongoProvider import MongoProvider

def Bind(container: Container):
    ConfigProvider(container)
    EventsProvider(container)

    config = container.get('config')

    databases = config['databases'].replace(' ', '').split(',')

    for database in databases:
        if database == 'mongo':
            MongoProvider(container)