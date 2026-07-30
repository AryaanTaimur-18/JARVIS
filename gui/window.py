from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
)
from PySide6.QtCore import Qt


class JarvisWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS")
        self.resize(900, 600)

        label = QLabel("Welcome to JARVIS")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)