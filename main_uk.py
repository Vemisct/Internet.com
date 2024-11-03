#python -m PyQt5.uic.pyuic -x my_project.ui -o ui.py
from PyQt5.QtWidgets import QMainWindow
from page_1uk import Page1Uk
from pr_v1_l2 import Ui_Form

class MainUk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)

    def next(self):
        self.close()
        self.ui2 = Page1Uk()
        self.ui2.show()