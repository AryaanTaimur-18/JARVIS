from PySide6.QtCore import QObject, Signal


class EventBus(QObject):

    thinking_started = Signal()
    thinking_finished = Signal()

    tool_started = Signal(str, dict)
    tool_succeeded = Signal(str, dict, str)
    tool_failed = Signal(str, dict, str)

    def __init__(self):
        super().__init__()


event_bus = EventBus()