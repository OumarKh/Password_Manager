from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit, QMessageBox
from Classes import PassGen


class PassSafe(QDialog):
    def __init__(self, parent=PassGen):
        super().__init__(parent)
        self.setWindowTitle("Password Safe")
        self.resize(500, 400)
        self.setWindowIcon(QIcon("icons/padlock.png"))

        self.button = QPushButton("Password Generator ", self)
        self.button.move(360, 360)
        self.button.clicked.connect(self.GoToPassGen)
        self.logged = False

        if not self.logged :
            self.label1 = QLabel("Log In Please",self)
            self.label1.move(210,20)
            # Label and text field for the username
            self.label2 = QLabel("Username :",self)
            self.label2.move(100,50)

            self.usernameText = QLineEdit(self)
            self.usernameText.move(100,70)
            self.usernameText.resize(300,30)
            #Label and text field for the password
            self.label3 = QLabel("Password :",self)
            self.label3.move(100, 110)

            self.password = QLineEdit(self)
            self.password.move(100,130)
            self.password.resize(300,30)
            #button to login
            self.loginbtn = QPushButton("login", self)
            self.loginbtn.setIcon(QIcon('icons/login.png'))
            self.loginbtn.move(210, 180)
            self.loginbtn.resize(70, 40)
            self.loginbtn.clicked.connect(self.login)
    def login (self):
        if self.usernameText.text() == "Oumar" and self.password.text() == "oumar":
            QMessageBox.information(self, "Logged In", "Welcome Oumar")
            #Clearing out the login tools after login in
            self.usernameText.hide()
            self.label1.hide()
            self.label2.hide()
            self.label3.hide()
            self.password.hide()
            self.loginbtn.hide()
        else:
            QMessageBox.information(self,"Error","Wrong Credentials")

    def GoToPassGen(self):
        self.hide()
        self.parent().show()
