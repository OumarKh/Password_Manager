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

        if not self.logged:
            self.label1 = QLabel("Log In Please", self)
            self.label1.move(210, 20)
            # Label and text field for the username
            self.label2 = QLabel("Username :", self)
            self.label2.move(100, 50)

            self.usernameText = QLineEdit(self)
            self.usernameText.move(100, 70)
            self.usernameText.resize(300, 30)
            # Label and text field for the password
            self.label3 = QLabel("Password :", self)
            self.label3.move(100, 110)

            self.password = QLineEdit(self)
            self.password.move(100, 130)
            self.password.resize(300, 30)
            self.password.setEchoMode(QLineEdit.Password)
            # button to login
            self.loginbtn = QPushButton("login", self)
            self.loginbtn.setIcon(QIcon('icons/login.png'))
            self.loginbtn.move(210, 180)
            self.loginbtn.resize(70, 40)
            self.loginbtn.clicked.connect(self.login)

            # layout of the password safe
            # Add Section; user can add the service name , username and the password
            self.label4 = QLabel("Add:", self)
            self.label4.move(30, 20)
            self.label4.hide()

            self.label5 = QLabel("Service :", self)
            self.label5.move(30, 50)
            self.label5.hide()

            self.service = QLineEdit(self)
            self.service.move(30, 70)
            self.service.resize(140, 30)
            self.service.hide()

            self.label6 = QLabel("Username :", self)
            self.label6.move(180, 50)
            self.label6.hide()

            self.username = QLineEdit(self)
            self.username.move(180, 70)
            self.username.resize(140, 30)
            self.username.hide()

            self.label7 = QLabel("Password :", self)
            self.label7.move(330, 50)
            self.label7.hide()

            self.passwd = QLineEdit(self)
            self.passwd.move(330, 70)
            self.passwd.resize(140, 30)
            self.passwd.setEchoMode(QLineEdit.Password)
            self.passwd.hide()

            self.savebtn = QPushButton("Save", self)
            self.savebtn.setIcon(QIcon('icons/save.png'))
            self.savebtn.move(200, 120)
            self.savebtn.clicked.connect(self.savedata)
            self.savebtn.hide()
            # Search Section ; the user can search his saved password either by username or by service
            self.label8 = QLabel("Search :", self)
            self.label8.move(30,160)
            self.label8.hide()

            self.searchbox = QLineEdit(self)
            self.searchbox.move(90,155)
            self.searchbox.hide()

            
    def savedata(self):
        pass

    def login(self):

        if self.usernameText.text() == 'Oumar' and self.password.text() == 'oumar':
            QMessageBox.information(self, "Logged In", "Welcome Oumar")
            # Clearing out the login tools after logging in
            self.usernameText.hide()
            self.label1.hide()
            self.label2.hide()
            self.label3.hide()
            self.password.hide()
            self.loginbtn.hide()
            #Showing the password Safe tool after logging in
            self.label4.show()
            self.label5.show()
            self.service.show()
            self.label6.show()
            self.username.show()
            self.label7.show()
            self.passwd.show()
            self.savebtn.show()
            self.label8.show()
            self.searchbox.show()

        else:
            QMessageBox.information(self, "Error", "Wrong Credentials")

    def GoToPassGen(self):
        self.hide()
        self.parent().show()
