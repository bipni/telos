from src.telos.services.Container import Container
from src.telos.helpers.Welcome import Welcome
from src.system.Bind import Bind

import sys
import importlib
import time

def launch():
    args = sys.argv[1:]

    container = Container()
    Bind(container)

    for arg in args:
        if arg == 'hello':
            Welcome()

        else:
            beg = time.time()

            package = f"stock.{arg}"

            if importlib.util.find_spec(package) is not None:
                mod = importlib.import_module(package)

                if 'run' in dir(mod):
                    values = mod.run()
                    print(values)
                else:
                    print(f"run method not defined in package {arg}")
            else:
                print("Package Not Found")
            
            duration = time.time() - beg
            print('\nFinished in {:.2f} seconds.'.format(duration))

    
    try:
        time.sleep(3600)
    except KeyboardInterrupt:
        print('Terminated')

def main():
    launch()