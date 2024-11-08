from PyQt5.QtWidgets import QWidget
from pr_v1_s3_l1 import Ui_Form

class Page3Uks2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)