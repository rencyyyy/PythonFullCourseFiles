import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line Edit")
        self.setGeometry(700, 300 ,500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 210, 40)
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     "font-family: Arial;")
        self.button.setGeometry(219, 10, 100, 40)
        self.button.setStyleSheet("font-size: 20px;"
                                  "font-family: Arial;")
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter your name")

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
