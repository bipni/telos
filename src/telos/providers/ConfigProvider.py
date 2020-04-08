from src.telos.services.Container import Container
from config.config import config

def ConfigProvider(container: Container):
    cfg = config()

    container.singleton('config', cfg)
