from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor


class ChatWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setPlaceholderText("Conversation will appear here...")

    def add_user_message(self, message):

        self.append(
        f"<b style='color:#4FC3F7;'>You:</b> {message}<br>"
        )

        self.append(
        f"<p><b style='color:#4FC3F7;'>You:</b> {message}</p>"
        )

        self.moveCursor(QTextCursor.End)

    def add_assistant_message(self, message):

        self.append(
        f"<b style='color:#81C784;'>JARVIS:</b> {message}<br>"
        )

        self.append(
        f"<p><b style='color:#81C784;'>JARVIS:</b> {message}</p>"
        )

        self.moveCursor(QTextCursor.End)

    def clear_chat(self):

        self.clear()

    def add_system_message(self, message):

        self.append(
            f"<p style='color:#BBBBBB;'>"
            f"{message}"
            f"</p>"
        )