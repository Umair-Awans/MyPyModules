from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel


class ClickableLabel(QLabel):
    leftClicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def __init__(self, text=""):
        super().__init__(text)
        self.setCursor(Qt.PointingHandCursor)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftClicked.emit()
        elif event.button() == Qt.RightButton:
            self.rightClicked.emit()
