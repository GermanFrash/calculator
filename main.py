import sys

from PyQt5 import QtWidgets
from main_win import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure()

    def configure(self):
        self.btn_clear.clicked.connect(
            lambda: self.lineResult.clear()
        )

        self.btn_result.clicked.connect(self.__handle_equal)

        for btn, val in self.__map_btn_values():
            btn.clicked.connect(self.__handle(val))

    def __handle(self, val: str):
        def wrap():
            math_op = ["*", "-", "+", "/"]
            new_text = self.lineResult.text()

            if new_text and (new_text[-1] in math_op) and (val in math_op):
                return

            new_text = new_text + val

            new_text = new_text.replace("++", "+")
            new_text = new_text.replace("--", "-")
            new_text = new_text.replace("**", "*")
            new_text = new_text.replace("//", "/")

            self.lineResult.setText(new_text)

        return wrap

    def __handle_equal(self):
        try:
            result = float(eval(self.lineResult.text()))
        except:
            result = self.lineResult.text()
            msg = (QtWidgets.QMessageBox(self))
            msg.setText('Ошибка при вычеслениях')
            msg.exec_()

        self.lineResult.setText(str(result))

    def __map_btn_values(self):
        return [
            (self.btn_num0, "0"),
            (self.btn_num1, "1"),
            (self.btn_num2, "2"),
            (self.btn_num3, "3"),
            (self.btn_num4, "4"),
            (self.btn_num5, "5"),
            (self.btn_num6, "6"),
            (self.btn_num7, "7"),
            (self.btn_num8, "8"),
            (self.btn_num9, "9"),

            (self.btn_plus, "+"),
            (self.btn_minus, "-"),
            (self.btn_mult, "*"),
            (self.btn_div, "/"),
        ]


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()