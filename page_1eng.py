from PyQt5.QtWidgets import QMainWindow
from pr_v1_l3_eng import Ui_Form
from page_2eng import Page2Eng
from page_1eng_s1 import Page1Engs1

class Page1Eng(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
        self.ui.pushButton_2.clicked.connect(self.go)

    def next(self):
        self.hide()
        self.ui2 = Page2Eng()
        self.ui2.ui.pushButton_3.clicked.connect(self.back_from_page1)
        self.ui2.show()

    def go(self):
        self.hide()
        self.w2 = Page1Engs1()
        self.w2.show()
        self.w2.messageBox.finished.connect(self.back_to)
    
    def back_to(self):
        self.show()
        self.w2.close()

    def back_from_page1(self):
        self.show()
        self.ui2.close()