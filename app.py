from PyQt5.QtWidgets import QApplication
import sys
from pages.LoginPage import LoginPage

from pages.WelcomePage import WelcomePage


class App():
    def __init__(self):
        self.initWindow = LoginPage()
        self.initWindow.show()

    def tes(self):
        print("tes")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
