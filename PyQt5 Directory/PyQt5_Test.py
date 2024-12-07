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
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setWindowIcon(QIcon("Images/icon.jpg"))
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello World, Goodbye", self)
        label.setFont(QFont("Arial", 15))
        label.setGeometry(0, 0, 500, 40)
        label.setStyleSheet("color: #FFFFFF;"
                            "background-color: #000000;"
                            "font-weight: bold;")

        label.setAlignment(Qt.AlignCenter)

        image = QLabel(self)
        pixmap = QPixmap("Images/Maris.jpg")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 250, 250)
        image.setScaledContents(True)

        image.setGeometry((self.width() - image.width()) // 2,
                          (self.height() - image.height()) // 2,
                          image.width(),
                          image.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




















