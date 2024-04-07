import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from main_win import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure()

    def configure(self):
         self.pushButton.clicked.connect(self.change_lable_after_clc)

    def change_lable_after_clc(self):
        self.label.setText('1')
        self.label_2.setText('2')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()
