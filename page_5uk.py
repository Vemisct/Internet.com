from PyQt5.QtWidgets import QMainWindow
from pr_v1_l7 import Ui_Form
from page_5uk_sl1 import Page5Uksl1

class Page5Uk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.go)

    def go(self):
        self.hide()
        self.w2 = Page5Uksl1()
        self.w2.show()
        self.w2.ui.pushButton.clicked.connect(self.back_to)

    def back_to(self):
        self.show()
        self.w2.close()