from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from helper.auth import Auth
from pages.HomePage import HomePage

from pages.page import Page


class LoginPage(Page):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Login Page')
        self.label.move(20, 20)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")

        self.username = QLabel(self)
        self.username.setText("Username")
        self.username.move(20, 80)

        self.usernameLe = QLineEdit(self)
        self.usernameLe.move(20, 100)

        self.password = QLabel(self)
        self.password.setText("Password")
        self.password.move(20, 140)

        self.passwordLe = QLineEdit(self)
        self.passwordLe.move(20, 160)
        self.passwordLe.setEchoMode(QLineEdit.Password)

        self.btnLogin = QPushButton("Login", self)
        self.btnLogin.move(20, 200)
        self.btnLogin.clicked.connect(self.login)

        self.status = QLabel(self)
        self.status.move(20, 240)
        self.status.setMinimumWidth(600)

    def login(self):
        auth = Auth()
        result = auth.login(self.usernameLe.text(), self.passwordLe.text())
        self.status.setText(
            "Gagal login username atau password salah" if result == False else "Username dan password benar, anda berhasil login")
        self.switchPage(HomePage()) if result == True else None
