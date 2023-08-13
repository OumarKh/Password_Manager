import sys
from PyQt5.QtWidgets import QApplication
from Classes import PassGen


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pass_gen_win = PassGen.PassGen()
    pass_gen_win.show()
    sys.exit(app.exec_())
