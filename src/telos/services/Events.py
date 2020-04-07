from typing import Callable
from collections import defaultdict

class Events:
    def __init__(self):
        self._data = {}
        self._listener = defaultdict(list)
    
    def fire(self, event_name: str, data: dict):
        self._data[event_name] = data
        
        listeners = self._listener[event_name] if self._listener[event_name] else []

        for listener in listeners:
            listener(self._data[event_name])

    def catch(self, event_name: str, listener: Callable[[dict], None]):
        self._listener[event_name].append(listener)