from PySide6.QtWidgets import (QToolBar)
from PySide6.QtGui import (QActionGroup)
from ..tools import (Brush, Eraser)

class toolbox(QActionGroup):
    pass

class toolboxWidget(QToolBar):
    """
    Custom QT Toolbar for presenting the painting tools.
    """
    def __init__(self):
        super().__init__()
        self.tools = QActionGroup(self)
        self.tools.setExclusive(True)
        # TODO: replace with a call to load tools from a configuration file
        _tools = [
            Brush("red", checkable=True),
            Brush("yellow", checkable=True),
            Brush("blue", checkable=True),
            Eraser(checkable=True)
        ]
        for tool in _tools:
            self.addAction(tool)
            self.tools.addAction(tool)
        # set the first tool to be selected
        self.tools.actions()[0].setChecked(True)
