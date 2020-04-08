from src.telos.services.Container import Container
from src.telos.servers.http.start import HTTP

def run(container: Container):
    config = container.get('config')

    server = HTTP(container)
    container.singleton('server', server)
    server.start()