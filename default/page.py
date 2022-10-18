from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pages.page import Page


class ClassName(Page):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('New Page')
        self.label.move(0, 0)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")
