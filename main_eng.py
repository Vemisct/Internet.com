#python -m PyQt5.uic.pyuic -x my_project.ui -o ui.py
from PyQt5.QtWidgets import QMainWindow
from page_1eng import Page1Eng
from pr_v1_l2_eng import Ui_Form

class MainEng(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)

    def next(self):
        self.close()
        self.ui2 = Page1Eng()
        self.ui2.show()