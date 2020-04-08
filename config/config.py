from config.app import app
from config.databases import databases
from config.systems import systems

def config():
    return dict(
        **app(),
        **systems(),
        **databases()
    )