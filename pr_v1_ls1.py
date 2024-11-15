# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prototype_v.1_ls1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 0, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(25, 50, 450, 275))
        self.calendarWidget.setStyleSheet("\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(84, 84, 84);\n"
"selection-background-color: rgb(84, 84, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 340, 100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Календар"))
        self.pushButton.setText(_translate("Form", "Повернутися"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
