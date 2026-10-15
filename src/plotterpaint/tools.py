from enum import Enum
from PySide6.QtGui import (QAction, QColor, QPainterPath, QPen,)
from PySide6.QtWidgets import QGraphicsPathItem, QGraphicsScene

class Brush(QAction):
    def __init__(self, color="black", *args, **kwargs):
        super().__init__(color, *args, **kwargs)
        self._current_item = None
        self._start_point = None
        self._pen = QPen(QColor(color), 200)

    def mousePress(self, scene, pos):
        self._start_point = pos
        self._current_item = QGraphicsPathItem()
        self._current_item.setPen(self._pen)
        path = QPainterPath()
        path.moveTo(self._start_point)

    def mouseMove(self, scene, pos):
        if self._start_point and self._current_item:
            current_point = pos
            path = self._current_item.path()
            path.lineTo(current_point)
            self._current_item.setPath(path)
        else:
            pass

    def mouseRelease(self, scene, pos):
        scene.addItem(self._current_item)
        self._start_point = None
        self._current_item = None


class Eraser(QAction):
    def __init__(self, *args, **kwargs):
        super().__init__("eraser", *args, **kwargs)

    def mousePress(self, scene, pos):
        pass
