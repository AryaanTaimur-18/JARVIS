from PySide6.QtCore import QObject, QTimer, Signal

class TypeWriter(QObject):

    finished = Signal()

    def __init__(self):

        super().__init__()

        self.timer = QTimer()

        self.timer.timeout.connect(self._next_character)

        self.text = ""
        self.index = 0
        self.callback = None

    def start(self, text, callback, interval=20):

        self.text = text
        self.index = 0
        self.callback = callback

        self.timer.start(interval)

    def _next_character(self):

        if self.index >= len(self.text):

            self.timer.stop()

            self.finished.emit()

            return

        self.index += 1

        self.callback(
            self.text[:self.index]
        )