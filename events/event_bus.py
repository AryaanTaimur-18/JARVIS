from collections import defaultdict


class EventBus:

    def __init__(self):

        self._listeners = defaultdict(list)

    def on(self, event_name, callback):

        self._listeners[event_name].append(callback)

    def off(self, event_name, callback):
    
            if callback in self._listeners[event_name]:
                self._listeners[event_name].remove(callback)

    def emit(self, event_name, **data):

        for callback in self._listeners[event_name]:
            callback(**data) 

event_bus = EventBus()

    