from PyQt5.QtWidgets import QMainWindow
from pr_v1_l7_eng import Ui_Form
from page_5eng_sl1 import Page5Engsl1

class Page5Eng(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.go)

    def go(self):
        self.hide()
        self.w2 = Page5Engsl1()
        self.w2.show()
        self.w2.ui.pushButton.clicked.connect(self.back_to)

    def back_to(self):
        self.show()
        self.w2.close()