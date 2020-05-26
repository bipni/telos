from src.telos.services.Container import Container

import importlib

def register_plugins(container: Container):
    server = container.get('flask')
    config = container.get('config')
    plugins = config['plugins'].replace(' ', '').split(',')

    for plugin in plugins:
        package = "src.telos.plugins.%s.server.Start" % (plugin)

        if importlib.util.find_spec(package) is not None:
            mod = importlib.import_module(package)

        if 'register_routes' in dir(mod):
            mod.register_routes(container)
        else:
            print(f"register_routes method not defined in package {package}")

        if 'register_events' in dir(mod):
            mod.register_events(container)
        else:
            print(f"register_events method not defined in package {package}")

