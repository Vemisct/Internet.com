from PyQt5.QtWidgets import QMainWindow, QMessageBox
from pr_v1_s1_eng import Ui_Form
from random import randint

class Page1Engs1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.order)
        self.messageBox = QMessageBox()
        self.ui.listWidget.setCurrentRow(randint(0,self.ui.listWidget.count())-1)
        

    def order(self):
        n = self.ui.spinBox.value()
        i = self.ui.listWidget.currentItem()
        self.messageBox.setWindowTitle("Order result")
        self.messageBox.setText(f'Successfully ordered\nNumber of records: {n}\nSelected genre: {i.text()}')
        self.messageBox.exec_()
