from config.app import app
from config.databases import databases
from config.systems import systems
from config.servers import servers


def config():
    return dict(
        **app(),
        **systems(),
        **servers(),
        **databases()
    )
