from PyQt5.QtWidgets import QMainWindow
from pr_v1_l4 import Ui_Form
#from  import

class Page2Uk(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)