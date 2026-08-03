from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
)


class InputBar(QWidget):

    send_message = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Type a message...")

        self.mic_button = QPushButton("🎤")

        self.send_button = QPushButton("Send")

        layout.addWidget(self.textbox)
        layout.addWidget(self.mic_button)
        layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.send)

        self.textbox.returnPressed.connect(self.send)

    def send(self):

        text = self.textbox.text().strip()

        if not text:
            return

        self.send_message.emit(text)

        self.textbox.clear()

    def set_enabled(self, enabled):

        self.textbox.setEnabled(enabled)
        self.send_button.setEnabled(enabled)
        self.mic_button.setEnabled(enabled)


    def focus(self):

        self.textbox.setFocus()