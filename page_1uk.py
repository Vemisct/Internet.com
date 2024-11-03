from PyQt5.QtWidgets import QMainWindow
from pr_v1_l3 import Ui_Form
from page_2uk import Page2Uk

class Page1Uk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)

    def next(self):
        self.hide()
        self.ui2 = Page2Uk()
        self.ui2.show()
    
    def go(self):
        pass