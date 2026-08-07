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
from events.constants import Events

from gui.messages import TOOL_MESSAGES

from gui.typewriter import TypeWriter


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

        from PySide6.QtCore import Qt

        self.process_message.connect(
            self.worker.process,
            Qt.QueuedConnection
        )

        self.worker.finished.connect(
            self.worker.process,
            Qt.QueuedConnection
        )
    
        self.worker.moveToThread(self.thread)

        self.thread.start()

        self.worker.thinking_started.connect(
            self.worker.process,
            Qt.QueuedConnection
        )

        self.worker.thinking_finished.connect(
            self.worker.process,
            Qt.QueuedConnection
        )

        self.worker.tool_started.connect(
            self.worker.process,
            Qt.QueuedConnection
        )

        self.worker.tool_finished.connect(
            self.worker.process,
            Qt.QueuedConnection
        )

        self.worker.tool_failed.connect(
            self.worker.process,
            Qt.QueuedConnection
        )

        self.typewriter = TypeWriter()

        # Signals
        self.input_bar.send_message.connect(self.handle_user_message)

        # Welcome message
        self.chat.add_assistant_message(
        """👋 Hello! I'm JARVIS.

        I'm ready to help you with:

        • Opening applications
        • Browsing the web
        • Creating folders
        • Taking screenshots

        How can I assist you today?"""
        )

        self.status.set_ready()

        self.input_bar.focus()

    def handle_user_message(self, message):

        self.chat.add_user_message(message)

        self.input_bar.set_enabled(False)

        self.process_message.emit(message)

    def handle_assistant_response(self, response):

        self.typewriter.start(
            response,
            self.update_typing
        )
    def update_typing(self, partial_text):

        self.chat.update_last_assistant_message(
            partial_text
        )

    def closeEvent(self, event):

        self.thread.quit()
        self.thread.wait()

        event.accept()

    def on_thinking_started(self):

        self.status.set_thinking()

    def on_thinking_finished(self):

        self.status.set_ready()

        self.input_bar.set_enabled(True)

        self.input_bar.focus()

    def on_tool_succeeded(
            self,
            tool_name,
            arguments,
            result
    ):

        message = TOOL_MESSAGES.get(tool_name)

        if message:

            self.chat.add_system_message(
                message["success"]
            )

        else:

            self.chat.add_system_message(
                "✅ Tool completed."
            )
    def on_tool_failed(
            self,
            tool_name,
            arguments,
            error
    ):

        message = TOOL_MESSAGES.get(tool_name)

        if message:

            self.chat.add_system_message(
                message["failed"]
            )

        else:

            self.chat.add_system_message(
                "❌ Tool failed."
            )
    def on_tool_started(self, tool_name, arguments):

        message = TOOL_MESSAGES.get(tool_name)

        if message:

            self.chat.add_system_message(
                message["started"]
            )

        else:

            self.chat.add_system_message(
                "🛠 Executing tool..."
            )

