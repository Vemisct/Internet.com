from PyQt5.QtWidgets import QWidget
from pr_v1_s3 import Ui_Form
from page_3uk_s2 import Page3Uks2

class Page3Uks1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go)
        self.w2 = Page3Uks2()

    def go(self):
        self.hide()
        self.w2.show()