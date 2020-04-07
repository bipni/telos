class Container:
    class __Container:
        _container_dict = {}

        def singleton(self, key, value):
            self._container_dict[key] = value

        def get(self, key):
            if key not in self._container_dict:
                return None

            return self._container_dict[key]

    instance: __Container = None

    def __init__(self):
        if not Container.instance:
            Container.instance = Container.__Container()

    def __getattr__(self, name):
        return getattr(Container.instance, name)