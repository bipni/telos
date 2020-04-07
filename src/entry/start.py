from src.telos.Container import Container
from src.telos.providers.ConfigProvider import ConfigProvider

def launch():
    container = Container()

    ConfigProvider(container)


def main():
    launch()