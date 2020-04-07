from src.telos.Container import Container
from config.config import config

from typing import Callable

def ConfigProvider(container: Container):
    cfg = config()

    container.singleton('config', cfg)
