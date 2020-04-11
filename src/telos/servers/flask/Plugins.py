from src.telos.services.Container import Container

import importlib

def register_plugins(container: Container):
    server = container.get('flask')
    config = container.get('config')
    plugins = config['plugins'].replace(' ', '').split(',')

    for plugin in plugins:
        module_path = "src.telos.plugins.%s.Start" % (plugin)

        try:
            module_spec = importlib.util.find_spec(module_path)
        except Exception as e:
            print(e)
            continue

        mod = importlib.import_module(module_path)

        if 'register_routes' in dir(mod):
            mod.register_routes(container)

