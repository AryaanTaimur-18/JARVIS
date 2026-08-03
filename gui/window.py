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
from events.event_bus import event_bus
from events.constants import Events


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

        event_bus.on(
            Events.THINKING_STARTED,
            self.on_thinking_started
        )

        event_bus.on(
            Events.THINKING_FINISHED,
            self.on_thinking_finished
        )

        event_bus.on(
            Events.TOOL_STARTED,
            self.on_tool_started
        )

        event_bus.on(
            Events.TOOL_SUCCEEDED,
            self.on_tool_succeeded
        )

        event_bus.on(
            Events.TOOL_FAILED,
            self.on_tool_failed
        )

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

        self.input_bar.set_enabled(False)

        self.process_message.emit(message)

    def handle_assistant_response(self, response):

        self.chat.add_assistant_message(response)

    def closeEvent(self, event):

        event_bus.off(
            Events.THINKING_STARTED,
            self.on_thinking_started
        )

        event_bus.off(
            Events.THINKING_FINISHED,
            self.on_thinking_finished
        )

        event_bus.off(
            Events.TOOL_STARTED,
            self.on_tool_started
        )

        event_bus.off(
            Events.TOOL_SUCCEEDED,
            self.on_tool_succeeded
        )

        event_bus.off(
            Events.TOOL_FAILED,
            self.on_tool_failed
        )

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

            self.chat.add_system_message(
                f"✅ {tool_name} completed."
            )
    def on_tool_failed(
            self,
            tool_name,
            arguments,
            error
    ):

            self.chat.add_system_message(
                f"❌ {tool_name} failed."
            )
    def on_tool_started(self, tool_name, arguments):

        self.chat.add_system_message(
            f"🛠 Executing {tool_name}..."
        )

