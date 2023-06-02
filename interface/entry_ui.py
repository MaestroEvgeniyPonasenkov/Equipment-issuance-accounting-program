# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Entry.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_Enter(object):

    def setupUi(self, Enter):
        Enter.setObjectName("Enter")
        Enter.resize(470, 150)
        Enter.setMinimumSize(QtCore.QSize(450, 140))
        Enter.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        Enter.setFont(font)
        Enter.setFocusPolicy(QtCore.Qt.NoFocus)
        Enter.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.centralwidget = QtWidgets.QWidget(Enter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet("")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.verticalLayout.addWidget(self.line_password)
        self.btn_entry = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_entry.setFont(font)
        self.btn_entry.setObjectName("btn_entry")
        self.verticalLayout.addWidget(self.btn_entry)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Enter.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Enter)
        self.statusBar.setObjectName("statusBar")
        Enter.setStatusBar(self.statusBar)

        self.retranslateUi(Enter)
        QtCore.QMetaObject.connectSlotsByName(Enter)

    def retranslateUi(self, Enter):
        _translate = QtCore.QCoreApplication.translate
        Enter.setWindowTitle(_translate("Enter", "Вход"))
        self.label.setText(_translate("Enter", "Введите пароль для входа в приложение"))
        self.btn_entry.setText(_translate("Enter", "Войти"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Enter = QtWidgets.QMainWindow()
    ui = Ui_Enter()
    ui.setupUi(Enter)
    Enter.show()
    sys.exit(app.exec_())