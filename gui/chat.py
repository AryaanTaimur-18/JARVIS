from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor


class ChatWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setPlaceholderText("Conversation will appear here...")

    def add_user_message(self, message):

        self.append(f"You: {message}\n")

        self.moveCursor(QTextCursor.End)

    def add_assistant_message(self, message):

        self.append(f"JARVIS: {message}\n")

        self.moveCursor(QTextCursor.End)

    def clear_chat(self):

        self.clear()