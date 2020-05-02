class Container:
    class __Container:
        _container_dict = {}

        def singleton(self, key, value):
            self._container_dict[key] = value

        def get(self, obj):
            if isinstance(obj, str):
                if obj not in self._container_dict:
                    return None

                return self._container_dict[obj]
            else:
                for key, value in self._container_dict.items():
                    if isinstance(value, obj):
                        return value
                else:
                    raise Exception("Object Not Found in Container")

    instance: __Container = None

    def __init__(self):
        if not Container.instance:
            Container.instance = Container.__Container()

    def __getattr__(self, name):
        return getattr(Container.instance, name)