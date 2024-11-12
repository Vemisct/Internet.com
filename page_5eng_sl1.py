from PyQt5.QtWidgets import QWidget
from pr_v1_ls1_eng import Ui_Form

class Page5Engsl1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)