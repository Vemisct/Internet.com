from PyQt5.QtWidgets import QMainWindow
from pr_v1_l5 import Ui_Form
from page_4uk import Page4Uk
from page_3uk_s1 import Page3Uks1

class Page3Uk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
        self.ui.pushButton_2.clicked.connect(self.go)

    def next(self):
        self.hide()
        self.ui2 = Page4Uk()
        self.ui2.ui.pushButton_3.clicked.connect(self.back_from_page3)
        self.ui2.show()

    def back_from_page3(self):
        self.show()
        self.ui2.close()

    def go(self):
        self.hide()
        self.w2 = Page3Uks1()
        self.w2.show()

    def back_to(self):
        self.show()
        self.w2.close()