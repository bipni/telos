from src.telos.services.Container import Container
from src.telos.providers.ConfigProvider import ConfigProvider
from src.telos.providers.EventsProvider import EventsProvider

def Bind(container: Container):
    ConfigProvider(container)
    EventsProvider(container)