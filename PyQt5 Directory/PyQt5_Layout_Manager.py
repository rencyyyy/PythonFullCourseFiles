import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Layout Manager")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)                         # Self argument is not necessary
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # VERTICAL ALIGNMENT - Patong-patong from top to bottom
        # vbox = QVBoxLayout()
        #
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        #HORIZONTAL ALIGNMENT - Magkakatabi from left to right
        # hbox = QHBoxLayout()
        #
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # GRID ALIGNMENT - 3 arguments the label, the vertical align, and the horizontal alignment
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 1)
        grid.addWidget(label3, 2, 2)
        grid.addWidget(label4, 3, 3)
        grid.addWidget(label5, 4, 4)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()