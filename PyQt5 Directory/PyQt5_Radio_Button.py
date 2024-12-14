import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button")
        self.setGeometry(700, 300, 500, 500)

        #Payment type
        self.radio1 = QRadioButton("G-Cash", self)
        self.radio2 = QRadioButton("Paymaya", self)
        self.radio3 = QRadioButton("Paypal", self)

        #Payment method
        self.radio4 = QRadioButton("Cash payment", self)
        self.radio5 = QRadioButton("Online Payment", self)

        self.button_group_1 = QButtonGroup(self)
        self.button_group_2 = QButtonGroup(self)

        self.initUI()
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)

        self.radio4.setGeometry(0, 170, 300, 50)
        self.radio5.setGeometry(0, 220, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px;"
                           "font-family: Times New Roman;"
                           "padding: 10px;"
                           "}")

        self.button_group_1.addButton(self.radio1)
        self.button_group_1.addButton(self.radio2)
        self.button_group_1.addButton(self.radio3)
        self.button_group_2.addButton(self.radio4)
        self.button_group_2.addButton(self.radio5)

        self.radio1.toggled.connect(self.button_onchange)
        self.radio2.toggled.connect(self.button_onchange)
        self.radio3.toggled.connect(self.button_onchange)
        self.radio4.toggled.connect(self.button_onchange)
        self.radio5.toggled.connect(self.button_onchange)

    def button_onchange(self):
        # create local object/variable and used sender method = determined which radio button is selected.
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())