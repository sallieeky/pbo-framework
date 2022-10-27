from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pages.page import Page


class HomePage(Page):
    def __init__(self, data={}):
        super().__init__()
        self.data = data

        self.initUi()

    def initUi(self):
        self.label = QLabel(self)
        self.label.setText('Halaman Home')
        self.label.move(0, 0)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")
