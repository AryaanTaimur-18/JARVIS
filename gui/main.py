import sys

from PySide6.QtWidgets import QApplication

from gui.window import JarvisWindow


def run():

    app = QApplication(sys.argv)

    window = JarvisWindow()
    window.show()

    sys.exit(app.exec())