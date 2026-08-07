from PySide6.QtCore import QObject, Signal, Slot


class AssistantWorker(QObject):

    thinking_started = Signal()
    thinking_finished = Signal()

    tool_started = Signal(str, dict)
    tool_finished = Signal(str, dict, str)
    tool_failed = Signal(str, dict, str)

    finished = Signal(str)

    def __init__(self, assistant):
        super().__init__()

        self.assistant = assistant

        # Connect Agent callbacks to Qt signals
        assistant.on_thinking_started = self.thinking_started.emit
        assistant.on_thinking_finished = self.thinking_finished.emit

        assistant.on_tool_started = self.tool_started.emit
        assistant.on_tool_finished = self.tool_finished.emit
        assistant.on_tool_failed = self.tool_failed.emit

    @Slot(str)
    def process(self, message):

        response = self.assistant.process(message)

        self.finished.emit(response)