from PyQt5.QtWidgets import QApplication
import sys
from pages.WelcomePage import WelcomePage


class App():
    def __init__(self):
        self.initWindow = WelcomePage()
        self.initWindow.show()

    def tes(self):
        print("tes")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
