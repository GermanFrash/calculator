# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 725)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_num6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num6.setGeometry(QtCore.QRect(260, 370, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num6.setFont(font)
        self.btn_num6.setObjectName("btn_num6")
        self.btn_num4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num4.setGeometry(QtCore.QRect(20, 370, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num4.setFont(font)
        self.btn_num4.setObjectName("btn_num4")
        self.btn_num5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num5.setGeometry(QtCore.QRect(140, 370, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num5.setFont(font)
        self.btn_num5.setObjectName("btn_num5")
        self.btn_num9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num9.setGeometry(QtCore.QRect(260, 270, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num9.setFont(font)
        self.btn_num9.setObjectName("btn_num9")
        self.btn_num7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num7.setGeometry(QtCore.QRect(20, 270, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num7.setFont(font)
        self.btn_num7.setObjectName("btn_num7")
        self.btn_num8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num8.setGeometry(QtCore.QRect(140, 270, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num8.setFont(font)
        self.btn_num8.setObjectName("btn_num8")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(310, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(250, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(190, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(130, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(20, 200, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(20, 150, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_result.setFont(font)
        self.btn_result.setObjectName("btn_result")
        self.btn_comm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_comm.setGeometry(QtCore.QRect(200, 570, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_comm.setFont(font)
        self.btn_comm.setObjectName("btn_comm")
        self.btn_num0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num0.setGeometry(QtCore.QRect(20, 570, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num0.setFont(font)
        self.btn_num0.setObjectName("btn_num0")
        self.lineResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineResult.setGeometry(QtCore.QRect(20, 20, 351, 121))
        self.lineResult.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineResult.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineResult.setFont(font)
        self.lineResult.setTabletTracking(False)
        self.lineResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineResult.setAutoFillBackground(False)
        self.lineResult.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineResult.setObjectName("lineResult")
        self.btn_num1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num1.setGeometry(QtCore.QRect(20, 470, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num1.setFont(font)
        self.btn_num1.setObjectName("btn_num1")
        self.btn_num3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num3.setGeometry(QtCore.QRect(260, 470, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num3.setFont(font)
        self.btn_num3.setObjectName("btn_num3")
        self.btn_num2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_num2.setGeometry(QtCore.QRect(140, 470, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_num2.setFont(font)
        self.btn_num2.setObjectName("btn_num2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_num6.setText(_translate("MainWindow", "6"))
        self.btn_num4.setText(_translate("MainWindow", "4"))
        self.btn_num5.setText(_translate("MainWindow", "5"))
        self.btn_num9.setText(_translate("MainWindow", "9"))
        self.btn_num7.setText(_translate("MainWindow", "7"))
        self.btn_num8.setText(_translate("MainWindow", "8"))
        self.btn_mult.setText(_translate("MainWindow", "x"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn_comm.setText(_translate("MainWindow", ","))
        self.btn_num0.setText(_translate("MainWindow", "0"))
        self.lineResult.setPlaceholderText(_translate("MainWindow", "0"))
        self.btn_num1.setText(_translate("MainWindow", "1"))
        self.btn_num3.setText(_translate("MainWindow", "3"))
        self.btn_num2.setText(_translate("MainWindow", "2"))
