from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QGraphicsScene)
from PySide6.QtCore import QSettings
from .toolboxWidget import toolboxWidget

class graphicsScene(QGraphicsScene):
    """
    Graphics Scene with necessary drawing logic
    """
    def __init__(self, toolbox, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action_group = toolbox

    def activeTool(self):
        return self.action_group.checkedAction()

    def mousePressEvent(self, event):
        pass
    def mouseMoveEvent(self, event):
        pass
    def mouseReleaseEvent(self, event):
        pass
