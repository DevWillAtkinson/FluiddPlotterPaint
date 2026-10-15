import sys
from PySide6.QtWidgets import (QApplication)
from .application import Window

def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
