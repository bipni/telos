from src.telos.Container import Container
from src.telos.providers.ConfigProvider import ConfigProvider
from src.telos.providers.EventsProvider import EventsProvider

def launch():
    container = Container()

    ConfigProvider(container)
    EventsProvider(container)


def main():
    launch()