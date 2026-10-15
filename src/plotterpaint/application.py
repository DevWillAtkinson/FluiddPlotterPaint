from plotterpaint.widgets.canvasWidget import canvasWidget
from plotterpaint.widgets.toolboxWidget import toolboxWidget

from PySide6.QtWidgets import (QMainWindow, QHBoxLayout, QMenu, QMenuBar, QWidget)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # The menu bar is where file controls and machine/document configuration will live.
        self.create_menu()

        toolbar = toolboxWidget()
        canvas = canvasWidget(toolbox=toolbar.tools,scene=None)

        self.setMenuBar(self._menu_bar)
        self.addToolBar(toolbar)
        self.setCentralWidget(canvas)

        # Title will not be visible but set it anyway
        self.setWindowTitle("Paint Plotter")

    # Define the menu in the titlebar
    def create_menu(self):
        self._menu_bar = QMenuBar(None)
        # Define a File action tray with Save, Open, Print, and Exit
        self._file_menu = QMenu("&File", self)
        self._save_action = self._file_menu.addAction("&Save")
        self._open_action = self._file_menu.addAction("&Open")
        self._print_action = self._file_menu.addAction("&Print")
        self._exit_action = self._file_menu.addAction("E&xit")
        self._menu_bar.addMenu(self._file_menu)
        # Connect to listeners for each action
        self._exit_action.triggered.connect(self.close)
