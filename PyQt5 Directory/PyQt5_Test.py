# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test GUI")
#         self.setGeometry(700, 300, 500, 300)
#         self.setWindowIcon(QIcon("icon.jpg"))
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel       # GUI AND LABELS
# from PyQt5.QtGui import QIcon, QFont                                # FAVICON AND FONTSTYLE
# from PyQt5.QtCore import Qt                                         # ALIGNMENT
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Maris Racal")
#         self.setGeometry(700, 250, 500, 700)
#         self.setWindowIcon(QIcon("Images/Maris.jpg"))
#
#         label = QLabel("Hmmm", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 15, 84, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Can we delete msgs", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 60, 188, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Okay", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(400, 105, 80, 40)
#         label.setStyleSheet("color: #f1faee;"
#                             "background-color: #0077b6;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Sarap", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 150, 78, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("But i'll touch myself na lang", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 195, 242, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Hahahah ipahinga mo na yan", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(222, 240, 260, 40)
#         label.setStyleSheet("color: #f1faee;"
#                             "background-color: #0077b6;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Ugh, yung amoy ng sweater mo", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 285, 275, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Im sad nauubos ko na yung amoy", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 330, 290, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Sayo na muna yan", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(300, 375, 180, 40)
#         label.setStyleSheet("color: #f1faee;"
#                             "background-color: #0077b6;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("hihihi", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(398, 420, 82, 40)
#         label.setStyleSheet("color: #f1faee;"
#                             "background-color: #0077b6;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("05/12/2024", self)
#         label.setFont(QFont("Arial", 8))
#         label.setGeometry(158, 465, 200, 40)
#         label.setStyleSheet("color: #212529;")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Rencyyyy", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 510, 110, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("yes?", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(408, 555, 72, 40)
#         label.setStyleSheet("color: #f1faee;"
#                             "background-color: #0077b6;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("Umm when?????", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 600, 168, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         label = QLabel("U miss my body? :)", self)
#         label.setFont(QFont("Arial", 12))
#         label.setGeometry(8, 645, 180, 40)
#         label.setStyleSheet("color: #212529;"
#                             "background-color: #ced4da;"
#                             "border-radius: 18px;"
#                             "font-weight: bold")
#
#         label.setAlignment(Qt.AlignCenter)
#
#
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QPixmap, QIcon
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.setWindowTitle("Inserting Image Testing")
#
#         label = QLabel(self)
#         label.setGeometry(0, 0, 250, 250)
#
#         pixmap = QPixmap("Images/Insert_Image.jpg")
#         label.setPixmap(pixmap)
#         label.setScaledContents(True)
#
#         label.setGeometry((self.width() - label.width()) // 2,
#                           (self.height() - label.height()) // 2,
#                           label.width(),
#                           label.height())
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QPixmap, QIcon, QFont
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("ICON, TEXT LABEL, AND IMAGES")
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.setGeometry(700, 300, 500, 500)
#
#         label = QLabel("HELLO WORLD, GOODBYE", self)
#         label.setFont(QFont("Arial", 15))
#         label.setGeometry(0,0,500,50)
#         label.setStyleSheet("color: #fefae0;"
#                             "background-color: #283618;"
#                             "font-weight: bold;")
#         label.setAlignment(Qt.AlignCenter)
#
#         imageLabel = QLabel(self)
#         pixMap = QPixmap("Images/Maris.jpg")
#         imageLabel.setPixmap(pixMap)
#         imageLabel.setGeometry(0, 0, 250, 250)
#         imageLabel.setScaledContents(True)
#
#         imageLabel.setGeometry((self.width() - imageLabel.width()) // 2,
#                                (self.height() - imageLabel.height()) // 2,
#                                imageLabel.width(),
#                                imageLabel.height())
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QIcon, QFont, QPixmap
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test")
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.setGeometry(700, 300, 500, 500)
#
#         label = QLabel("Hello World, Goodbye", self)
#         label.setFont(QFont("Arial", 15))
#         label.setGeometry(0, 0, 500, 40)
#         label.setStyleSheet("color: #FFFFFF;"
#                             "background-color: #000000;"
#                             "font-weight: bold;")
#
#         label.setAlignment(Qt.AlignCenter)
#
#         image = QLabel(self)
#         pixmap = QPixmap("Images/Maris.jpg")
#         image.setPixmap(pixmap)
#         image.setGeometry(0, 0, 250, 250)
#         image.setScaledContents(True)
#
#         image.setGeometry((self.width() - image.width()) // 2,
#                           (self.height() - image.height()) // 2,
#                           image.width(),
#                           image.height())
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
#                              QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
# from PyQt5.QtGui import QIcon
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Lay out testing")
#         self.setGeometry(700, 300, 500, 500)
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.initUI()
#
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         label1 = QLabel("#1")
#         label2 = QLabel("#2")
#         label3 = QLabel("#3")
#         label4 = QLabel("#4")
#         label5 = QLabel("#5")
#
#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: yellow;")
#         label3.setStyleSheet("background-color: green;")
#         label4.setStyleSheet("background-color: blue;")
#         label5.setStyleSheet("background-color: purple;")
#
#         grid = QGridLayout()
#
#         grid.addWidget(label1, 0, 0)
#         grid.addWidget(label2, 0, 1)
#         grid.addWidget(label3, 1, 0)
#         grid.addWidget(label4, 1, 1)
#         grid.addWidget(label5, 2, 3)
#
#         central_widget.setLayout(grid)
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button")
#         self.setGeometry(700,300,500,500)
#         self.button = QPushButton("Click me!", self)
#         self.label = QLabel("Hello!", self)
#         self.initUI()
#
#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("font-size: 30px;")
#         # self.button.clicked.connect(self.on_click)
#         self.button.clicked.connect(self.on_click)
#
#         self.label.setGeometry(150, 300, 200, 100)
#         self.label.setStyleSheet("font-size: 50px;")
#
#     def on_click(self):
#         self.label.setText("Goodbye!")
#         # self.button.setDisabled(True)         Disabled after click
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------

#OVERALL TEST
# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
#                              QVBoxLayout, QHBoxLayout, QGridLayout,
#                              QWidget)
# from PyQt5.QtGui import QIcon, QFont, QPixmap
# from PyQt5.QtCore import Qt
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test all")
#         self.setGeometry(700, 300, 500, 500)
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.initUI()
#
#         header = QLabel("PyQt5 Test All", self)
#         header.setGeometry(0, 0, 500, 50)
#         header.setFont(QFont("Arial", 20))
#         header.setStyleSheet("color: white;"
#                              "background-color: green;"
#                              "font-weight: bold;"
#                              "font-style: italic;"
#                              "text-decoration: underline;")
#         header.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
#
#         image = QLabel(self)
#         pixmap = QPixmap("Images/Maris.jpg")
#         image.setPixmap(pixmap)
#
#         image.setGeometry(0, 0, 250, 250)
#         image.setScaledContents(True)
#
#         image.setGeometry((self.width() - image.width()) // 2,
#                           (self.height() - image.height()) // 2,
#                           image.width(),
#                           image.height())
#
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         redColor = QLabel("#1")
#         yellowColor = QLabel("#2")
#         greenColor = QLabel("#3")
#         blueColor = QLabel("#4")
#         purpleColor = QLabel("#5")
#
#         redColor.setStyleSheet("background-color: red;")
#         yellowColor.setStyleSheet("background-color: yellow;")
#         greenColor.setStyleSheet("background-color: green;")
#         blueColor.setStyleSheet("background-color: blue;")
#         purpleColor.setStyleSheet("background-color: purple;")
#
#         grid = QGridLayout()
#         grid.addWidget(redColor, 0, 0)
#         grid.addWidget(yellowColor, 0, 1)
#         grid.addWidget(greenColor, 1, 0)
#         grid.addWidget(blueColor, 1, 1)
#         grid.addWidget(purpleColor, 2, 2)
#
#         central_widget.setLayout(grid)
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5. QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Button Test")
#         self.setGeometry(700, 300, 500, 500)
#
#         self.button = QPushButton("Button", self)
#         self.greetings = QLabel("Hello", self)
#
#
#         self.initUI()
#
#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("font-size: 15px;")
#         self.button.clicked.connect(self.on_click)
#
#         self.greetings.setGeometry(150, 300, 200, 100)
#         self.greetings.setStyleSheet("font-size: 20px;"
#                                      "font-style: italic;")
#
#     def on_click(self):
#         print("Button clicked!")
#         self.button.setText("clicked!")             # Change the text of the button when clicked
#         # self.button.setDisabled(True)             # When button clicked then disabled after
#         self.greetings.setText("Goodbye!")
#         self.greetings.setStyleSheet("font-weight: bold;"
#                                      "font-style: italic;"
#                                      "font-size: 20px;")
#         self.greetings.setGeometry(300, 300, 200, 100)
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton,
#                              QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
# from PyQt5.QtGui import QIcon, QFont, QPixmap
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test all PyQt5")
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.setGeometry(450, 150, 1000, 800)
#
#         title = QLabel("PyQt5 All Topics", self)
#         title.setFont(QFont("Times New Roman", 30))
#         title.setGeometry(0, 0, 1000, 80)
#
#         title.setStyleSheet("color: #FFFFFF;"
#                             "background-color: #000000;"
#                             "font-weight: bold;")
#
#         #title.setAlignment(Qt.AlignCenter)
#         title.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
#
#         image = QLabel(self)
#         pixmap = QPixmap("Images/Maris.jpg")
#         image.setPixmap(pixmap)
#
#         image.setGeometry(0, 0, 500, 500)
#         image.setScaledContents(True)
#
#         image.setGeometry((self.width() - image.width()) // 2,
#                           (self.height() - image.height()) // 2,
#                           image.width(),
#                           image.height())
#
#         self.initUI()
#
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         label1 = QLabel("#1", self)
#         label2 = QLabel("#2", self)
#         label3 = QLabel("#3", self)
#         label4 = QLabel("#4", self)
#         label5 = QLabel("#5", self)
#
#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: yellow;")
#         label3.setStyleSheet("background-color: green;")
#         label4.setStyleSheet("background-color: blue;")
#         label5.setStyleSheet("background-color: violet;")
#
#         grid = QGridLayout()
#
#         grid.addWidget(label1, 0, 0)
#         grid.addWidget(label2, 1, 0)
#         grid.addWidget(label3, 0, 1)
#         grid.addWidget(label4, 1, 2)
#         grid.addWidget(label5, 1, 1)
#
#         central_widget.setLayout(grid)
#
#         self.button = QPushButton("Button", self)
#         self.label = QLabel("HELLO!", self)
#
#         self.button.setGeometry(100, 100, 150, 80)
#         self.button.clicked.connect(self.on_click)
#         self.label.setGeometry(400, 400, 300, 50)
#         self.label.setStyleSheet("background-color: orange;")
#
#     def on_click(self):
#         print("Button clicked!")
#         self.button.setText("Clicked!")
#         self.label.setText("Goodbye")
#         self.label.setStyleSheet("background-color: purple;")
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Checkbox Testing")
#         self.setGeometry(700, 300, 500, 500)
#         self.checkbox = QCheckBox("Do you have a crush on me?", self)
#         self.initUI()
#     def initUI(self):
#         self.checkbox.setGeometry(40, 200, 500, 50)
#         self.checkbox.setStyleSheet("font-family: Arial;"
#                                     "font-size: 30px;")
#         self.checkbox.setChecked(False)
#         self.checkbox.stateChanged.connect(self.checkbox_changed)
#
#     def checkbox_changed(self, state):
#         if state == Qt.Checked:
#             print("I knew it")
#         else:
#             print("I'll touch myself na lang")
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QCheckBox
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button test")
#         self.setGeometry(700, 300, 500, 500)
#         self.button = QPushButton("Click me", self)
#         self.checkbox = QCheckBox("DO you have a crush on me?", self)
#         self.label = QLabel("Hello", self)
#         self.initUI()
#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("color: red;")
#         self.button.clicked.connect(self.on_click)
#
#
#         self.label.setGeometry(150, 300, 200, 100)
#         self.label.setStyleSheet("font-size: 30px;")
#         self.checkbox.setGeometry(10, 100, 400, 60)
#         self.checkbox.setStyleSheet("font-size: 20px")
#         self.checkbox.stateChanged.connect(self.on_change)
#
#     def on_click(self):
#         print("Button clicked!")
#         self.button.setText("clicked!")
#         self.button.setDisabled(True)
#         self.label.setText("Goodbye")
#
#     def on_change(self, state):
#         if state == Qt.Checked:
#             print("I knew it!")
#         else:
#             print("I'll touch myself na lang")
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup, QLabel
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Radio Button Test")
#         self.setGeometry(700, 300, 500, 500)
#
#         #Payment Type
#         self.title1 = QLabel("Payment Type", self)
#         self.radio1 = QRadioButton("G-Cash",self)
#         self.radio2 = QRadioButton("Paymaya", self)
#         self.radio3 = QRadioButton("Paypal", self)
#         self.radio4 = QRadioButton("Mastercard", self)
#         self.radio5 = QRadioButton("Visa", self)
#
#         #Payment Method
#         self.title2 = QLabel("Payment Method", self)
#         self.radio6 = QRadioButton("In-Store", self)
#         self.radio7 = QRadioButton("Online", self)
#
#         #Group 2 radio button options
#         self.button_group_1 = QButtonGroup(self)
#         self.button_group_2 = QButtonGroup(self)
#
#         self.initUI()
#
#     def initUI(self):
#         self.title1.setGeometry(0, 0, 500, 60)
#         self.radio1.setGeometry(0, 50, 300, 50)
#         self.radio2.setGeometry(0, 100, 300, 50)
#         self.radio3.setGeometry(0, 150, 300, 50)
#         self.radio4.setGeometry(0, 200, 300, 50)
#         self.radio5.setGeometry(0, 250, 300, 50)
#
#         self.title2.setGeometry(0, 320, 500, 60)
#         self.radio6.setGeometry(0, 370, 300, 50)
#         self.radio7.setGeometry(0, 420, 300, 50)
#
#         self.title1.setStyleSheet("font-weight: bold;"
#                                   "font-family: Arial;"
#                                   "font-size: 30px;"
#                                   "padding: 10px;")
#         self.title2.setStyleSheet("font-weight: bold;"
#                                   "font-family: Arial;"
#                                   "font-size: 30px;"
#                                   "padding: 10px;")
#
#         self.setStyleSheet("QRadioButton{"
#                            "font-size: 30px;"
#                            "font-family: Arial;"
#                            "padding: 10px;"
#                            "}")
#
#
#         self.button_group_1.addButton(self.radio1)
#         self.button_group_1.addButton(self.radio2)
#         self.button_group_1.addButton(self.radio3)
#         self.button_group_1.addButton(self.radio4)
#         self.button_group_1.addButton(self.radio5)
#
#         self.button_group_2.addButton(self.radio6)
#         self.button_group_2.addButton(self.radio7)
#
#         self.radio1.toggled.connect(self.radio_onclick)
#         self.radio2.toggled.connect(self.radio_onclick)
#         self.radio3.toggled.connect(self.radio_onclick)
#         self.radio4.toggled.connect(self.radio_onclick)
#         self.radio5.toggled.connect(self.radio_onclick)
#         self.radio6.toggled.connect(self.radio_onclick)
#         self.radio7.toggled.connect(self.radio_onclick)
#
#     def radio_onclick(self):
#         radio_button = self.sender()
#         if radio_button.isChecked():
#             print(f"{radio_button.text()} is selected")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("LINE EDIT TEST")
#         self.setGeometry(700, 300, 500, 500)
#         self.line_edit = QLineEdit(self)
#         self.button = QPushButton("Submit", self)
#
#         self.initUI()
#     def initUI(self):
#         self.line_edit.setGeometry(10, 10, 210, 40)
#         self.line_edit.setStyleSheet("font-size: 20px;"
#                                      "font-family: Arial;")
#         self.button.setGeometry(220, 10, 100, 40)
#         self.button.setStyleSheet("font-size: 20px;"
#                                   "font-family: Arial;")
#         self.button.clicked.connect(self.submit)
#         self.line_edit.setPlaceholderText("Enter your name")
#     def submit(self):
#         text = self.line_edit.text()
#         print(f"Hello, {text}")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

#-----------------------------------------------------------------------------------------------------------------------
# TEST ALL UPDATE

# import sys
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel,
#                              QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
#                              QPushButton, QCheckBox, QRadioButton, QLineEdit,
#                              QButtonGroup)
# from PyQt5.QtGui import QFont, QIcon, QPixmap
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test all update")
#         self.setGeometry(700, 300, 500, 500)
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#
#         # #LABEL
#         # label = QLabel("TESTING ALL UPDATE", self)
#         # label.setGeometry(0, 0, 500, 50)
#         # label.setFont(QFont("Times New Roman", 20))
#         # label.setStyleSheet("font-style: italic;"
#         #                     "color: yellow;"
#         #                     "background-color: blue;")
#
#         # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
#
#     #-----------------------------
#         # #IMAGE
#         # image = QLabel(self)
#         # image.setGeometry(0, 0, 250, 250)
#         # pixmap = QPixmap("Images/Maris.jpg")
#         # image.setPixmap(pixmap)
#         # image.setScaledContents(True)
#         #
#         # image.setGeometry((self.width() - image.width()) // 2,
#         #                   (self.height() - image.height()) // 2,
#         #                   image.width(),
#         #                   image.height())
#
#     # -----------------------------
#         # BUTTON
#         # self.button = QPushButton("click me", self)
#         # self.label = QLabel("Hello", self)
#
#     # -----------------------------
#         # # CHECKBOX
#         # self.check_box = QCheckBox("Crush mo ba ako?", self)
#
#     # -----------------------------
#         # # RADIO BUTTON
#         # self.button1 = QRadioButton("G-CASH", self)
#         # self.button2 = QRadioButton("CRYPTO", self)
#         # self.button3 = QRadioButton("PAYMAYA", self)
#         #
#         # self.button4 = QRadioButton("IN STORE", self)
#         # self.button5 = QRadioButton("ONLINE", self)
#         #
#         # self.button_group1 = QButtonGroup(self)
#         # self.button_group2 = QButtonGroup(self)
#
#     # -----------------------------
#         # # LINE EDIT
#         # self.line_edit = QLineEdit(self)
#         # self.button = QPushButton("Submit", self)
#         # self.initUI()
#     def initUI(self):
#         pass
#
#
#         # self.line_edit.setGeometry(10, 10, 210, 60)
#         # self.line_edit.setPlaceholderText("Enter your name...")
#         # self.line_edit.setStyleSheet("font-size: 20px;"
#         #                              "font-family: Arial;"
#         #                              "font-style: italic;")
#         #
#         # self.button.setGeometry(220, 10, 100, 60)
#         # self.button.setStyleSheet("font-size: 20px;"
#         #                           "font-family: Arial;")
#         # self.button.clicked.connect(self.on_submit)
#
#     # def on_submit(self):
#     #     text = self.line_edit.text()
#     #     print(f"Hello, {text}")
#     # ----------------------------------------------------------------
#         # central_widget = QWidget()
#         # self.setCentralWidget(central_widget)
#         #
#         # label1 = QLabel("#1")
#         # label2 = QLabel("#2")
#         # label3 = QLabel("#3")
#         # label4 = QLabel("#4")
#         # label5 = QLabel("#5")
#         #
#         # label1.setStyleSheet("background-color: red;")
#         # label2.setStyleSheet("background-color: yellow;")
#         # label3.setStyleSheet("background-color: green;")
#         # label4.setStyleSheet("background-color: blue;")
#         # label5.setStyleSheet("background-color: purple;")
#         #
#         # grid = QGridLayout()
#         #
#         # grid.addWidget(label1, 0, 0)
#         # grid.addWidget(label2, 0, 1)
#         # grid.addWidget(label3, 1, 1)
#         # grid.addWidget(label4, 1, 2)
#         # grid.addWidget(label5, 2, 2)
#         #
#         # central_widget.setLayout(grid)
#     # ----------------------------------------------------------------
#         # self.button.setGeometry(10, 10, 100, 40)
#         # self.button.setStyleSheet("font-family: Arial;"
#         #                           "font-size: 20px")
#         # self.label.setGeometry(150, 10, 150, 40)
#         # self.label.setStyleSheet("color: red;"
#         #                          "font-family: Arial;"
#         #                          "font-style: underlined;"
#         #                          "font-size: 30px;")
#         # self.button.clicked.connect(self.on_click)
#
#         # self.check_box.setGeometry(0, 0, 300, 50)
#         # self.check_box.setStyleSheet("font-family: Arial;"
#         #                              "font-size: 30px;"
#         #                              "padding: 10px")
#         # self.check_box.stateChanged.connect(self.on_check)
#     # ----------------------------------------------------------------
#         # self.button1.setGeometry(0, 0, 300, 50)
#         # self.button2.setGeometry(0, 50, 300, 50)
#         # self.button3.setGeometry(0, 100, 300, 50)
#         #
#         # self.button4.setGeometry(0, 170, 300, 50)
#         # self.button5.setGeometry(0, 220, 300, 50)
#         #
#         #
#         # self.setStyleSheet("QRadioButton{"
#         #                    "font-size: 30px;"
#         #                    "font-family: Arial;"
#         #                    "padding: 10px"
#         #                    "}")
#         #
#         # self.button_group1.addButton(self.button1)
#         # self.button_group1.addButton(self.button2)
#         # self.button_group1.addButton(self.button3)
#         #
#         # self.button_group2.addButton(self.button4)
#         # self.button_group2.addButton(self.button5)
#         #
#         # self.button1.toggled.connect(self.on_choose)
#         # self.button2.toggled.connect(self.on_choose)
#         # self.button3.toggled.connect(self.on_choose)
#         # self.button4.toggled.connect(self.on_choose)
#         # self.button5.toggled.connect(self.on_choose)
#     # ----------------------------------------------------------------
#     # def on_choose(self):
#     #     radio_button = self.sender()
#     #     if radio_button.isChecked():
#     #         print(f"You choose {radio_button.text()}")
#
#     # ----------------------------------------------------------------
#     # def on_check(self, state):
#     #     if state == Qt.Checked:
#     #         print("Alam ko.")
#     #     else:
#     #         print("I'll touch myself na lang")
#     # ----------------------------------------------------------------
#     # def on_click(self):
#     #     self.button.setText("clicked")
#     #     self.label.setText("Goodbye")
#     #     self.label.setGeometry(150, 10, 150, 40)
#     #     self.label.setStyleSheet("color: green;"
#     #                              "font-family: Times New Roman;"
#     #                              "font-size: 30px;")
#     #     print("Button clicked!")
#     #     self.button.setDisabled(True)
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()


#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5. QtWidgets import (QMainWindow, QApplication, QPushButton,
#                               QWidget, QHBoxLayout)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("CSS Test")
#         self.button1 = QPushButton("RED", self)
#         self.button2 = QPushButton("GREEN", self)
#         self.button3 = QPushButton("BLUE", self)
#         self.initUI()
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         hbox = QHBoxLayout()
#
#         hbox.addWidget(self.button1)
#         hbox.addWidget(self.button2)
#         hbox.addWidget(self.button3)
#         central_widget.setLayout(hbox)
#
#         self.button1.setObjectName("button1")
#         self.button2.setObjectName("button2")
#         self.button3.setObjectName("button3")
#
#         self.setStyleSheet("""
#             QPushButton{
#                 font-size: 40px;
#                 font-family: Times New Roman;
#                 padding: 25px 75px;
#                 margin: 25px 10px;
#                 border: 2px solid;
#                 border-radius: 5px;
#             }
#             QPushButton#button1{
#                 background-color: #96031a;
#             }
#             QPushButton#button2{
#                 background-color: #70e000;
#             }
#             QPushButton#button3{
#                 background-color: #00a6fb;
#             }
#
#             QPushButton#button1:hover{
#                 background-color: #dd1c1a;
#             }
#             QPushButton#button2:hover{
#                 background-color: #ccff33;
#             }
#             QPushButton#button3:hover{
#                 background-color: #7fc8f8;
#             }
#         """)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5. QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("CSS TEST2")
#         self.button1 = QPushButton("#1", self)
#         self.button2 = QPushButton("#2", self)
#         self.button3 = QPushButton("#3", self)
#         self.initUI()
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#
#         hbox = QHBoxLayout()
#
#         hbox.addWidget(self.button1)
#         hbox.addWidget(self.button2)
#         hbox.addWidget(self.button3)
#
#         self.button1.setObjectName("button1")
#         self.button2.setObjectName("button2")
#         self.button3.setObjectName("button3")
#
#
#         self.setStyleSheet("""
#             QPushButton{
#                 font-size: 20px;
#                 font-family: Arial;
#                 border: 2px solid;
#                 padding: 25px 100px;
#                 margin: 25px 5px;
#                 border-radius: 5px;
#             }
#             QPushButton#button1{
#                 background-color: #bc6c25;
#             }
#             QPushButton#button2{
#                 background-color: #606c38;
#             }
#             QPushButton#button3{
#                 background-color: #2b2d42;
#             }
#
#             QPushButton#button1:hover{
#                 background-color: #dda15e;
#             }
#             QPushButton#button2:hover{
#                 background-color: #6a994e;
#             }
#             QPushButton#button3:hover{
#                 background-color: #8d99ae;
#             }
#         """)
#         central_widget.setLayout(hbox)
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt5.QtCore import QTime, QTimer, Qt
# from PyQt5.QtGui import QFont, QFontDatabase
#
# class DigitalClock(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Digital Clock Test")
#         self.time_label = QLabel(self)
#         self.timer = QTimer(self)
#
#         self.initUI()
#     def initUI(self):
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)
#         self.time_label.setAlignment(Qt.AlignCenter)
#
#         self.time_label.setStyleSheet("font-size: 150px;"
#                                       "color: #ffb627;")
#         self.setStyleSheet("background-color: #0d1321;")
#
#         font_id = QFontDatabase.addApplicationFont("Font-uploaded/DS-DIGII.TTF")
#         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#
#         my_font = QFont(font_family, 150)
#         self.time_label.setFont(my_font)
#
#         self.timer.timeout.connect(self.update_time)
#         self.timer.start()
#         self.update_time()
#     def update_time(self):
#         current_time = QTime.currentTime().toString("hh:mm:ss AP")
#         self.time_label.setText(current_time)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     clock = DigitalClock()
#     clock.show()
#     sys.exit(app.exec_())


#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt5.QtCore import QTime, QTimer, Qt
# from PyQt5.QtGui import QFont, QFontDatabase
#
# class DigitalClock(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Digital Clock")
#         self.time_label = QLabel(self)
#         self.timer = QTimer(self)
#
#         self.initUI()
#     def initUI(self):
#         self.setGeometry(600, 400, 300, 100)
#         self.time_label.setAlignment(Qt.AlignCenter)
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)
#         self.time_label.setStyleSheet("font-size: 150px;"
#                                       "color: #52b788;")
#         self.setStyleSheet("background-color: #353535;")
#
#         font_id = QFontDatabase.addApplicationFont("Font-uploaded/DS-DIGII.TTF")
#         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#         my_font = QFont(font_family, 150)
#         self.time_label.setFont(my_font)
#
#         self.timer.timeout.connect(self.update_time)
#         self.timer.start(1000)
#         self.update_time()
#     def update_time(self):
#         current_time = QTime.currentTime().toString("hh:mm:ss AP")
#         self.time_label.setText(current_time)
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     clock = DigitalClock()
#     clock.show()
#     sys.exit(app.exec_())


#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton,
#                              QWidget, QVBoxLayout, QHBoxLayout)
# from PyQt5.QtCore import QTime, QTimer, Qt
#
# class StopWatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label = QLabel("00:00:00:00", self)
#
#         self.start_button = QPushButton("Start", self)
#         self.stop_button = QPushButton("Stop", self)
#         self.reset_button = QPushButton("Reset", self)
#
#         self.timer = QTimer(self)
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle("STOP WATCH TEST")
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.time_label.setAlignment(Qt.AlignCenter)
#         self.setLayout(vbox)
#
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)
#
#         vbox.addLayout(hbox)
#
#         self.start_button.setObjectName("Start")
#         self.stop_button.setObjectName("Stop")
#         self.reset_button.setObjectName("Reset")
#
#         self.setStyleSheet("""
#             QPushButton, QLabel{
#                 padding: 15px;
#                 font-family: calibri;
#             }
#             QLabel{
#                 font-size: 120px;
#                 color: #fca311;
#                 background-color: #000000;
#             }
#             QPushButton{
#                 font-size: 50px;
#             }
#
#             QPushButton#Start{
#                 background-color: #b5e48c;
#             }
#             QPushButton#Stop{
#                 background-color: #9e2a2b;
#             }
#             QPushButton#Reset{
#                 background-color: #457b9d;
#             }
#
#             QPushButton#Start:hover{
#                 background-color: #76c893;
#             }
#             QPushButton#Stop:hover{
#                 background-color: #e5383b;
#             }
#             QPushButton#Reset:hover{
#                 background-color: #4cc9f0;
#             }
#         """)
#
#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)
#         self.timer.timeout.connect(self.update_display)
#
#     def start(self):
#         self.timer.start(10)
#
#     def stop(self):
#         self.timer.stop()
#
#     def reset(self):
#         self.timer.stop()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label.setText(self.format_time(self.time))
#
#     def format_time(self, time):
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         milliseconds = time.msec() // 10
#         return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
#
#     def update_display(self):
#         self.time = self.time.addMSecs(10)
#         self.time_label.setText(self.format_time(self.time))
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     stopwatch = StopWatch()
#     stopwatch.show()
#     sys.exit(app.exec_())

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton,
#                              QWidget, QVBoxLayout, QHBoxLayout)
#
# from PyQt5.QtCore import QTime, QTimer, Qt
# from PyQt5.QtGui import QIcon
#
# class StopWatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label = QLabel("00:00:00.00", self)
#
#         self.start_button = QPushButton("Start", self)
#         self.stop_button = QPushButton("Stop", self)
#         self.reset_button = QPushButton("Reset", self)
#
#         self.timer = QTimer(self)
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("STOP WATCH")
#         self.setWindowIcon(QIcon("Images/icon.jpg"))
#         self.time_label.setAlignment(Qt.AlignCenter)
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)
#
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)
#         vbox.addLayout(hbox)
#
#         self.start_button.setObjectName("start")
#         self.stop_button.setObjectName("stop")
#         self.reset_button.setObjectName("reset")
#
#         self.setStyleSheet("""
#             QLabel, QPushButton{
#                 padding: 30px;
#                 font-family: calibri;
#             }
#             QLabel{
#                 font-size: 120px;
#                 color: #eb5e28;
#                 background-color: #252422;
#             }
#             QPushButton{
#                 font-size: 40px;
#             }
#
#             QPushButton#start{
#                 color: #f4f3ee;
#                 background-color: #248232;
#             }
#             QPushButton#stop{
#                 color: #f4f3ee;
#                 background-color: #8d0801;
#             }
#             QPushButton#reset{
#                 color: #f4f3ee;
#                 background-color: #00509d;
#             }
#
#             QPushButton#start:hover{
#                 background-color: #adc178;
#             }
#             QPushButton#stop:hover{
#                 background-color: #bf4342;
#             }
#             QPushButton#reset:hover{
#                 background-color: #4cc9f0;
#             }
#         """)
#
#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)
#         self.timer.timeout.connect(self.update_display)
#
#     def start(self):
#         self.timer.start(10)
#
#     def stop(self):
#         self.timer.stop()
#
#     def reset(self):
#         self.timer.stop()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label.setText(self.format_time(self.time))
#
#     def format_time(self, time):
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         millisecond = time.msec() // 10
#         return f"{hours:02}:{minutes:02}:{seconds:02}.{millisecond:02}"
#
#     def update_display(self):
#         self.time = self.time.addMSecs(10)
#         self.time_label.setText(self.format_time(self.time))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     stopwatch = StopWatch()
#     stopwatch.show()
#     sys.exit(app.exec_())

#-----------------------------------------------------------------------------------------------------------------------
# import sys
# import requests
# from PyQt5. QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit,
#                               QWidget, QVBoxLayout)
# from PyQt5. QtCore import Qt
# from PyQt5. QtGui import QIcon
#
# class WeatherApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.city_label = QLabel("Enter city name: ", self)
#         self.city_input = QLineEdit(self)
#         self.get_weather_button = QPushButton("Check weather", self)
#         self.temperature_label = QLabel(self)
#         self.emoji_label = QLabel(self)
#         self.description_label = QLabel(self)
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Window app test")
#         self.setWindowIcon(QIcon("Images/img.png"))
#
#         self.city_label.setAlignment(Qt.AlignCenter)
#         self.city_input.setAlignment(Qt.AlignCenter)
#         self.temperature_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_input)
#         vbox.addWidget(self.get_weather_button)
#         vbox.addWidget(self.temperature_label)
#         vbox.addWidget(self.emoji_label)
#         vbox.addWidget(self.description_label)
#         self.setLayout(vbox)
#
#         self.city_label.setObjectName("city_label")
#         self.city_input.setObjectName("city_input")
#         self.get_weather_button.setObjectName("get_weather_button")
#         self.temperature_label.setObjectName("temperature_label")
#         self.emoji_label.setObjectName("emoji_label")
#         self.description_label.setObjectName("description_label")
#
#         self.setStyleSheet("""
#             QLabel, QPushButton, QLineEdit{
#                 font-family: calibri;
#             }
#
#             QLabel#city_label{
#                 font-size: 20px;
#             }
#             QLineEdit#city_input{
#                 font-size: 30px;
#                 font-weight: bold;
#                 padding: 5px;
#             }
#             QPushButton#get_weather_button{
#                 font-size: 20px;
#             }
#             QLabel#temperature_label{
#                 font-size: 50px;
#             }
#             QLabel#emoji_label{
#                 font-size: 50px;
#             }
#             QLabel#description_label{
#                 font-size: 30px;
#             }
#         """)
#         self.get_weather_button.clicked.connect(self.get_weather)
#     def get_weather(self):
#         api_key = "751ee4b0321835ac5b40d533da1519ea"
#         city = self.city_input.text()
#
#         try:
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#             response = requests.get(url)
#             response.raise_for_status()
#             data = response.json()
#
#             if data["cod"] == 200:
#                 self.display_weather(data)
#
#         except requests.exceptions.HTTPError as http_error:
#             match response.status_code:
#                 case 400:
#                     self.display_error("Bad requests:\nPlease check your input")
#                 case 401:
#                     self.display_error("Unauthorized requests:\nInvalid API key")
#                 case 403:
#                     self.display_error("Forbidden:\nAccess is denied")
#                 case 404:
#                     self.display_error("Not Found:\nCity not found")
#                 case 500:
#                     self.display_error("Internal Server Error:\nPlease try again later")
#                 case 502:
#                     self.display_error("Bad Gateway:\nInvalid response from the server")
#                 case 503:
#                     self.display_error("Unavailable Service:\nServer is down")
#                 case 504:
#                     self.display_error("Gateway Timeout:\nNo response from the server")
#                 case _:
#                     self.display_error(f"HTTP error occurred:\n{http_error}")
#
#         except requests.exceptions.ConnectionError:
#             self.display_error("Connection Error:\nCheck your internet connection")
#         except requests.exceptions.Timeout:
#             self.display_error("Timeout Error:\nThe request timed out")
#         except requests.exceptions.TooManyRedirects:
#             self.display_error("Too many Redirects:\nCheck the URL")
#         except requests.exceptions.RequestException as req_error:
#             self.display_error(f"Request Error:\n{req_error}")
#
#     def display_error(self, message):
#         self.temperature_label.setStyleSheet("font-size: 20px;")
#         self.temperature_label.setText(message)
#         self.emoji_label.clear()
#         self.description_label.clear()
#     def display_weather(self, data):
#         self.temperature_label.setStyleSheet("font-size: 40px;")
#         temperature_k = data["main"]["temp"]  # kelvin
#         temperature_c = temperature_k - 273.15
#         temperature_f = (temperature_k * 9 / 5) - 459.67
#         weather_id = data["weather"][0]["id"]
#         weather_description = data["weather"][0]["description"]
#         self.temperature_label.setText(f"{temperature_f:.0f}°F")
#         self.emoji_label.setText(self.get_weather_emoji(weather_id))
#         self.description_label.setText(f"'{weather_description.capitalize()}'")
#
#     @staticmethod
#     def get_weather_emoji(weather_id):
#
#         if 200 <= weather_id <= 232:
#             return "⛈️"
#         elif 300 <= weather_id <= 321:
#             return "🌦️"
#         elif 500 <= weather_id <= 531:
#             return "🌧️"
#         elif 600 <= weather_id <= 622:
#             return "🌧️"
#         elif 701 <= weather_id <= 741:
#             return "🌫️"
#         elif weather_id == 762:
#             return "🌋"
#         elif weather_id == 771:
#             return "💨"
#         elif weather_id == 781:
#             return "🌪️"
#         elif weather_id == 800:
#             return "☀️"
#         elif 801 <= weather_id <= 804:
#             return "☁️"
#         else:
#             return ""
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     weather_app = WeatherApp()
#     weather_app.show()
#     sys.exit(app.exec_())

#-----------------------------------------------------------------------------------------------------------------------



























