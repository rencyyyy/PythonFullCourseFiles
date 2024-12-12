import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Images/icon.jpg"))
        self.setWindowTitle("Checkbox")
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you have a crush on me?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 50)
        self.checkbox.setStyleSheet("font-family: Arial;"
                                    "font-size: 30px;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("I knew it!")
        else:
            print("Okay, i'll touch myself na lang")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()