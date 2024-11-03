#python -m PyQt5.uic.pyuic -x my_project.ui -o ui.py
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_Newpassword
from random import*
from time import*

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_Newpassword()
        self.ui.setupUi(self)
        self.ui.pb_1.clicked.connect(self.create)
        self.ui.pb_2.clicked.connect(self.show_cb)
        self.ui.ch_box4.setHidden(True)
        self.ui.ch_box4.setEnabled(False)
        self.i = 0

    def create(self):
        signin = ''
        if self.ui.ch_box1.isChecked():
            signin += 'abcdefghijklmnopqrstuvwxyz'
        if self.ui.ch_box2.isChecked():
            signin += '0123456789'
        if self.ui.ch_box3.isChecked():
            signin += '!@#$%^&*()'
        if self.ui.ch_box4.isChecked():
            signin = ['Mua','mi','amigo!']   
            result = signin[self.i]
            self.ui.l_result.setText(result)
            
            self.i += 1

            if self.i == len(signin):
                self.i = 0
            return
        if len(signin) == 0:
            self.ui.l_result.setText('Будь-ласка, оберіть один з пунктів.')
            return

        result = ''
        n = randint(6, 12)
        for i in range(n):
            result += choice(signin)
        self.ui.l_result.setText(result)

    def show_cb(self):
        self.ui.ch_box4.setHidden(False)
        self.ui.ch_box4.setEnabled(True)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()