from PyQt5.QtWidgets import QMainWindow
from pr_v1_l4_eng import Ui_Form
from page_3eng import Page3Eng
from page_2eng_s1 import Page2Engs1

class Page2Eng(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
        self.ui.pushButton_2.clicked.connect(self.go)

    def next(self):
        self.hide()
        self.ui2 = Page3Eng()
        self.ui2.ui.pushButton_3.clicked.connect(self.back_from_page2)
        self.ui2.show()

    def back_from_page2(self):
        self.show()
        self.ui2.close()

    def go(self):
        self.hide()
        self.w2 = Page2Engs1()
        self.w2.show()
        self.w2.ui.pushButton.clicked.connect(self.back_to)
    
    def back_to(self):
        self.show()
        self.w2.close()
        