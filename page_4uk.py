from PyQt5.QtWidgets import QMainWindow
from pr_v1_l6 import Ui_Form
from page_5uk import Page5Uk
#from page_4uk_s1 import Page4Uks1

class Page4Uk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
        #self.ui.pushButton_2.clicked.connect(self.go)

    def next(self):
        self.hide()
        self.ui2 = Page5Uk()
        self.ui2.ui.pushButton_3.clicked.connect(self.back_from_page4)
        self.ui2.show()

    def back_from_page4(self):
        self.show()
        self.ui2.close()

    def go(self):
        self.hide()
        self.w2 = Page4Uks1()
        self.w2.show()

    def back_to(self):
        self.show()
        self.w2.close()