import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Push Button")
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me", self)                      # Transfer button to constructor
        self.label = QLabel("Hello", self)                               # Set text label
        self.initUI()                                                    # Set initUI function to constructor

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)                      # Set geometry of the button
        self.button.setStyleSheet("font-size: 15px;")                    # Set style of the button
        self.button.clicked.connect(self.on_click)                       # send signal to the button (self.func)

        self.label.setGeometry(150, 300, 200, 100)                       # set the geometry of the text label
        self.label.setStyleSheet("font-size: 20px;")                     # set the font size of the text label

    def on_click(self):
        print("Button clicked!")                                         # print something when button clicked
        self.button.setText("Clicked")                                   # change the text of the button

        self.label.setGeometry(300, 300, 200, 100)                       # set geometry of the text labe
        self.label.setText("Goodbye")                                    # change the text of the text label when button clicked

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
