from src.telos.services.Container import Container

import importlib
import multiprocessing

def run(container: Container):
    config = container.get('config')

    server_types = config['server'].split(',')

    for server_type in server_types:
        package = f"src.telos.servers.{server_type}.start"

        if importlib.util.find_spec(package) is not None:
            mod = importlib.import_module(package)

            if 'run' in dir(mod):
                server = multiprocessing.Process(target=mod.run, args=(container,))
                server.start()
            else:
                print(f"run method not defined in {server_type} server")