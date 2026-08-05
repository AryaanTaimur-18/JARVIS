from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor
from datetime import datetime


class ChatWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setPlaceholderText("Conversation will appear here...")

        self.messages = []

    def add_user_message(self, message):

        self.messages.append(
            ("user", message)
        )

        self.render_messages()

    def add_assistant_message(self, message):

        self.messages.append(
            ("assistant", message)
        )

        self.render_messages()

    def update_last_assistant_message(self, message):

        # If there is no previous assistant message,
        # create one.
        if (
            not self.messages or
            self.messages[-1][0] != "assistant"
        ):

            self.messages.append(
                ("assistant", message)
            )

        else:

            self.messages[-1] = (
                "assistant",
                message
            )

        self.render_messages()

    def clear_chat(self):

        self.messages.clear()

        self.clear()

    def add_system_message(self, message):

        self.messages.append(
            ("system", message)
        )

        self.render_messages()

    @staticmethod
    def timestamp():

        return datetime.now().strftime("%H:%M")

    def scroll_to_bottom(self):

        scrollbar = self.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def render_messages(self):

        self.clear()

        for role, message in self.messages:

            if role == "user":

                self.append(
                    f"<p><b style='color:#4FC3F7;'>You:</b> {message}</p>"
                )

            elif role == "assistant":

                self.append(
                    f"<p><b style='color:#81C784;'>JARVIS:</b> {message}</p>"
                )

            elif role == "system":

                self.append(
                    f"<p style='color:#BBBBBB;'>{message}</p>"
                )

        self.scroll_to_bottom()