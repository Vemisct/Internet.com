from PyQt5.QtWidgets import QMainWindow
from pr_v1_l3 import Ui_Form
from page_2uk import Page2Uk
from page_1uk_s1 import Page1Uks1

class Page1Uk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
        self.ui.pushButton_2.clicked.connect(self.go)

    def next(self):
        self.hide()
        self.ui2 = Page2Uk()
        self.ui2.ui.pushButton_3.clicked.connect(self.back_from_page1)
        self.ui2.show()

    def go(self):
        self.hide()
        self.w2 = Page1Uks1()
        self.w2.show()
        self.w2.messageBox.finished.connect(self.back_to)
    
    def back_to(self):
        self.show()
        self.w2.close()

    def back_from_page1(self):
        self.show()
        self.ui2.close()