from src.telos.Container import Container
from src.telos.services.Events import Events

def EventsProvider(container: Container):
    events = Events()

    container.singleton('events', events)