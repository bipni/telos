from src.telos.Container import Container
from src.telos.providers.ConfigProvider import ConfigProvider
from src.telos.providers.EventsProvider import EventsProvider
from src.telos.helpers.Welcome import Welcome

import sys
import importlib

def launch():
    args = sys.argv[1:]

    container = Container()

    ConfigProvider(container)
    EventsProvider(container)

    for arg in args:
        if arg == 'hello':
            Welcome()

        else:
            package = f"stock.{arg}"

            if importlib.util.find_spec(package) is not None:
                mod = importlib.import_module(package)

                if 'run' in dir(mod):
                    value = mod.run()
                    print(value)
                else:
                    print("run method not defined")
            else:
                print("Package Not Found")



def main():
    launch()