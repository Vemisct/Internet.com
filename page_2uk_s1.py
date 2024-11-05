from PyQt5.QtWidgets import QWidget
from pr_v1_s2 import Ui_Form

class Page2Uks1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)