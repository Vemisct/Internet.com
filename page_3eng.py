from PyQt5.QtWidgets import QMainWindow
from pr_v1_l5_eng import Ui_Form
from page_4eng import Page4Eng
from page_3eng_s1 import Page3Engs1

class Page3Eng(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
        self.ui.pushButton_2.clicked.connect(self.go)

    def next(self):
        self.hide()
        self.ui2 = Page4Eng()
        self.ui2.ui.pushButton_3.clicked.connect(self.back_from_page3)
        self.ui2.show()

    def back_from_page3(self):
        self.show()
        self.ui2.close()

    def go(self):
        self.hide()
        self.w2 = Page3Engs1()
        self.w2.w2.messageBox.finished.connect(self.back_to)
        self.w2.show()

    def back_to(self):
        self.show()
        self.w2.w2.close()
        self.w2.close()