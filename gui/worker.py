from PySide6.QtCore import QObject, Signal, Slot


class AssistantWorker(QObject):

    finished = Signal(str)

    def __init__(self, assistant):
        super().__init__()

        self.assistant = assistant

    @Slot(str)
    def process(self, message):

        response = self.assistant.process(message)

        self.finished.emit(response)