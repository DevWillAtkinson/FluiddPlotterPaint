from PySide6.QtWidgets import (QGraphicsView)
from .graphicsScene import graphicsScene

class canvasWidget(QGraphicsView):
    """
    QT Canvas Widget.
    """
    def __init__(self, toolbox=None, scene=None):
        super().__init__()
        # TODO: change these hardcoded values to load from config
        if self.scene() == None:
            print("constructed scene")
            self.setScene(graphicsScene(toolbox, 0, 0, 200, 200, self))
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
