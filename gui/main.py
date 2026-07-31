import sys

from PySide6.QtWidgets import QApplication

from gui.window import JarvisWindow


def run():

    app = QApplication(sys.argv)

    from brain.assistant import Assistant

    assistant = Assistant()

    window = JarvisWindow(assistant)
    window.show()

    sys.exit(app.exec())