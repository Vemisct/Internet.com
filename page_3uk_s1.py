from PyQt5.QtWidgets import QWidget
from pr_v1_s3 import Ui_Form
from page_3uk_s2 import Page3Uks2
#from page_3uk import Page3Uk

class Page3Uks1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go)

    def go(self):
        self.hide()
        self.w2 = Page3Uks2()
        #self.w3.ui = Page3Uk
        self.w2.show()
        self.w2.ui.pushButton.clicked.connect(self.back_to)

    def back_to(self):
        #self.w3.ui.show()
        self.close()
        self.w2.close()