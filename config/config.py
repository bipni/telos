from config.app import app
from config.databases import databases

def config():
    return dict(
        **app(),
        **databases()
    )