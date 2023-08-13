from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QPushButton
from Classes import PassGen


class PassSafe(QDialog):
    def __init__(self, parent=PassGen):
        super().__init__(parent)
        self.setWindowTitle("Password Safe")
        self.resize(400, 300)
        self.setWindowIcon(QIcon("icons/padlock.png"))

        self.button = QPushButton("Password Generator ", self)
        self.button.move(260, 260)
        self.button.clicked.connect(self.GoToPassGen)

    def GoToPassGen(self):
        self.hide()
        self.parent().show()
