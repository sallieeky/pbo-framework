from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from controllers import controller
from pages.page import Page


class ClassName(Page):
    def __init__(self, data={}):
        super().__init__()
        self.data = data

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('New Page')
        self.label.move(0, 0)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")
