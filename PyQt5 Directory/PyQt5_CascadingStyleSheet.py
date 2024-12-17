import sys 
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton,
                             QWidget, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cascading Style Sheet")
        self.button1 = QPushButton("RED", self)
        self.button2 = QPushButton("GREEN", self)
        self.button3 = QPushButton("BLUE", self)
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.button1.clicked.connect(self.on_click)
        self.button2.clicked.connect(self.on_click)
        self.button3.clicked.connect(self.on_click)

        self.setStyleSheet("""
                    QPushButton{
                        font-size: 40px;
                        font-family: Arial;
                        padding: 15px 75px;
                        margin: 25px;
                        border: 2px solid;
                        border-radius: 15px;
                    }
                    QPushButton#button1{
                        background-color: #4f000b;
                    }
                    QPushButton#button2{
                        background-color: #004b23;
                    }
                    QPushButton#button3{
                        background-color: #013a63;
                    }
                    
                    QPushButton#button1:hover{
                        background-color: #720026;
                    }
                    QPushButton#button2:hover{
                        background-color: #008000;
                    }
                    QPushButton#button3:hover{
                        background-color: #014f86;
                    }
                """)
    def on_click(self):
        print("You clicked the button")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()