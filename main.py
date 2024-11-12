#python -m PyQt5.uic.pyuic -x my_project.ui -o ui.py
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from pr_v1_l1 import Ui_Form
from main_uk import MainUk
from main_eng import MainEng

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.next)
    
    def next(self):
        if self.ui.radioButton_2.isChecked():
            self.ui2 = MainUk()
            self.ui2.show()
            self.close()
        if self.ui.radioButton.isChecked():
            self.ui2 = MainEng()
            self.ui2.show()
            self.close()

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()