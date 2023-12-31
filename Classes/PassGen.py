from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QSlider, QLineEdit, QCheckBox, QMessageBox,QApplication
from PyQt5.QtCore import Qt
from Classes import PassSafe
import random


class PassGen(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setting the window layout
        self.setWindowTitle("Password Generator")
        self.resize(400, 300)
        self.setWindowIcon(QIcon("icons/key.png"))
        # Slider Label
        label1 = QLabel("Choose Length :", self)
        label1.move(10, 10)
        # Slider layout
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(6)
        slider.setMaximum(24)
        slider.setValue(6)
        slider.setGeometry(30, 30, 250, 30)
        slider.move(100, 50)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        slider.valueChanged.connect(self.update_txbx)
        # Text Box layout and connecting it to the slider, so it shows the value pointed to by the slider
        self.length_txbx = QLineEdit(self)
        self.length_txbx.setAlignment(Qt.AlignCenter)
        self.length_txbx.setReadOnly(True)
        self.length_txbx.setText("6")
        self.length_txbx.move(30, 45)
        self.length_txbx.resize(40, 30)

        # Checkbox area Label
        label2 = QLabel("Includes :", self)
        label2.move(10, 80)
        # Checkboxes for password customisation
        self.uppcase = QCheckBox("Upper Case", self)
        self.uppcase.move(50, 110)
        self.lowcase = QCheckBox("Lower Case", self)
        self.lowcase.move(160, 110)
        self.nums = QCheckBox("Numbers", self)
        self.nums.move(270, 110)
        self.specchar = QCheckBox("Characters", self)
        self.specchar.move(160, 140)

        # Setting the window functionalities
        # A button to pass to the Password safe window
        self.button = QPushButton("Password Safe", self)
        self.button.move(290, 260)
        self.button.clicked.connect(self.GoToPassSafe)
        self.pass_safe_window = None

        # Label for the generator Password
        label3 = QLabel("Generated Password :", self)
        label3.move(10, 170)
        label3.setMinimumSize(140, 20)
        # Setting up the text box where the generated password will appear
        self.genPass = QLineEdit(self)
        self.genPass.setAlignment(Qt.AlignCenter)
        self.genPass.setReadOnly(False)
        self.genPass.move(10, 200)
        self.genPass.resize(300, 30)

        # Adding a button to execute the password generation
        GenButton = QPushButton("Generate", self)
        GenButton.move(20, 260)
        GenButton.clicked.connect(self.GeneratePassword)


        #Adding a litte button to make it easier to copy the generated passsword
        self.cpbutton =QPushButton("",self)
        self.cpbutton.setIcon(QIcon('icons/copy.png'))
        self.cpbutton.move(320,200)
        self.cpbutton.resize(50,30)
        self.cpbutton.clicked.connect(self.CopyToClipboard)

    def CopyToClipboard(self):
        text = self.genPass.text()
        if text :
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            QMessageBox.information(self, "Copied", "Text has been copied to clipboard.")
        else:
            QMessageBox.warning(self, "Error", "No text to copy.")
    #This function creates to password with the chosen parameters
    def GeneratePassword(self):
        upp = "QWERTYUIOPASDFGHJKLZXCBNM"
        low = "qwertyuiopasdfghjklzxcbnm"
        num = "1234567890"
        car = "!@#$%&*=+-_[}]{/?"
        usedStr =""
        if self.uppcase.isChecked():
            usedStr = usedStr + upp
        if self.lowcase.isChecked():
            usedStr = usedStr + low
        if self.nums.isChecked():
            usedStr = usedStr + num
        if self.specchar.isChecked():
            usedStr = usedStr + car
        passleng = int(self.length_txbx.text())
        generatedPassword = ''.join((random.choice(usedStr) for x in range(passleng)))
        self.genPass.setText(generatedPassword)

    #This function sets the textbox beside the slider to the corresponding value from the slider
    def update_txbx(self, value):
        self.length_txbx.setText(str(value))

    # Defining the function that changes the window from pasword Generator to Password Safe
    def GoToPassSafe(self):
        self.hide()
        if not self.pass_safe_window:
            self.pass_safe_window = PassSafe.PassSafe(self)
        self.pass_safe_window.exec_()
        self.show()
