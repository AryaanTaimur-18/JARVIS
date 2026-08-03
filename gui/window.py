from PySide6.QtCore import QThread, Signal
from gui.worker import AssistantWorker
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from gui.chat import ChatWidget
from gui.input_bar import InputBar
from gui.status_bar import StatusBar


class JarvisWindow(QMainWindow):

    process_message = Signal(str)

    def __init__(self, assistant):
        super().__init__()

        self.assistant = assistant

        self.setWindowTitle("JARVIS AI Assistant")
        self.resize(900, 600)

        self.setMinimumSize(900, 600)

        # Widgets
        self.chat = ChatWidget()
        self.input_bar = InputBar()
        self.status = StatusBar()

        # Layout
        central = QWidget()

        layout = QVBoxLayout(central)

        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        layout.addWidget(self.chat, 1)
        layout.addWidget(self.input_bar, 0)
        layout.addWidget(self.status, 0)

        self.setCentralWidget(central)

        self.thread = QThread()

        self.worker = AssistantWorker(self.assistant)

        self.process_message.connect(
        self.worker.process
        )

        self.worker.finished.connect(
        self.handle_assistant_response
        )

        self.worker.moveToThread(self.thread)

        self.thread.start()

        # Signals
        self.input_bar.send_message.connect(self.handle_user_message)

        # Welcome message
        self.chat.add_assistant_message(
        "Hello! I'm JARVIS. How can I help you today?"
        )

        self.status.set_ready()

        self.input_bar.focus()

    def handle_user_message(self, message):

        self.chat.add_user_message(message)

        self.status.set_thinking()

        self.input_bar.set_enabled(False)

        self.process_message.emit(message)

    def handle_assistant_response(self, response):

        self.chat.add_assistant_message(response)

        self.status.set_ready()

        self.input_bar.set_enabled(True)

        self.input_bar.focus()

    def closeEvent(self, event):

        self.thread.quit()

        self.thread.wait()

        event.accept()