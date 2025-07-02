from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt


class MyButton(QPushButton):

    def __init__(self, text=""):
        super().__init__(text)
        self.setCursor(Qt.PointingHandCursor)
        
