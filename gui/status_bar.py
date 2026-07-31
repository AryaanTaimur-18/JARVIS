from PySide6.QtWidgets import QLabel


class StatusBar(QLabel):

    def __init__(self):
        super().__init__()

        self.set_ready()

    def set_ready(self):
        self.setText("🟢 Ready")

    def set_listening(self):
        self.setText("🎤 Listening...")

    def set_thinking(self):
        self.setText("🧠 Thinking...")

    def set_tool(self):
        self.setText("🛠 Executing Tool...")

    def set_speaking(self):
        self.setText("🔊 Speaking...")