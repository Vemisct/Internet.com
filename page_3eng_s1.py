from PyQt5.QtWidgets import QWidget
from pr_v1_s3_eng import Ui_Form
from page_3eng_s2 import Page3Engs2

class Page3Engs1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go)
        self.w2 = Page3Engs2()

    def go(self):
        self.hide()
        self.w2.show()