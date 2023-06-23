from typing import Callable, Tuple
from collections import defaultdict


class Events:
    def __init__(self):
        self._data = {}
        self._listener = defaultdict(list)

    def fire(self, event_name: str, event_data: Tuple):
        self._data[event_name] = event_data

        listeners = self._listener[event_name] if self._listener[event_name] else [
        ]

        for listener in listeners:
            listener(*self._data[event_name])

    def catch(self, event_name: str, listener: Callable):
        self._listener[event_name].append(listener)
