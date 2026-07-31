from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from gui.chat import ChatWidget
from gui.input_bar import InputBar
from gui.status_bar import StatusBar


class JarvisWindow(QMainWindow):

    def __init__(self, assistant):
        super().__init__()

        self.assistant = assistant

        self.setWindowTitle("JARVIS")
        self.resize(900, 600)

        # Widgets
        self.chat = ChatWidget()
        self.input_bar = InputBar()
        self.status = StatusBar()

        # Layout
        central = QWidget()

        layout = QVBoxLayout(central)

        layout.addWidget(self.chat)
        layout.addWidget(self.input_bar)
        layout.addWidget(self.status)

        self.setCentralWidget(central)

        # Signals
        self.input_bar.send_message.connect(self.handle_user_message)

        # Welcome message
        self.chat.add_assistant_message(
            "Welcome to JARVIS!"
        )

    def handle_user_message(self, message):

        self.chat.add_user_message(message)

        self.status.set_thinking()

        response = self.assistant.process(message)

        self.chat.add_assistant_message(response)

        self.status.set_ready()