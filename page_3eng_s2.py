from PyQt5.QtWidgets import QWidget, QMessageBox
from pr_v1_s3_l1_eng import Ui_Form

class Page3Engs2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.messageBox = QMessageBox()
        self.ui.pushButton.clicked.connect(self.order)

    def order(self):
        n1 = int(self.ui.spinBox.value())*900
        n2 = int(self.ui.spinBox_2.value())*1200
        n3 = int(self.ui.spinBox_3.value())*1800
        self.messageBox.setWindowTitle("Order result")
        self.messageBox.setText(f'Successfully issued\nPayable: {n1+n2+n3}\nThank you for your purchase!')
        self.messageBox.exec_()