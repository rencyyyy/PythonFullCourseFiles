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
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel       # GUI AND LABELS
from PyQt5.QtGui import QIcon, QFont                                # FAVICON AND FONTSTYLE
from PyQt5.QtCore import Qt                                         # ALIGNMENT


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maris Racal")
        self.setGeometry(700, 250, 500, 700)
        self.setWindowIcon(QIcon("Images/Maris.jpg"))

        label = QLabel("Hmmm", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 15, 84, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Can we delete msgs", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 60, 188, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Okay", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(400, 105, 80, 40)
        label.setStyleSheet("color: #f1faee;"
                            "background-color: #0077b6;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Sarap", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 150, 78, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("But i'll touch myself na lang", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 195, 242, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Hahahah ipahinga mo na yan", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(222, 240, 260, 40)
        label.setStyleSheet("color: #f1faee;"
                            "background-color: #0077b6;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Ugh, yung amoy ng sweater mo", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 285, 275, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Im sad nauubos ko na yung amoy", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 330, 290, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Sayo na muna yan", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(300, 375, 180, 40)
        label.setStyleSheet("color: #f1faee;"
                            "background-color: #0077b6;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("hihihi", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(398, 420, 82, 40)
        label.setStyleSheet("color: #f1faee;"
                            "background-color: #0077b6;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("05/12/2024", self)
        label.setFont(QFont("Arial", 8))
        label.setGeometry(158, 465, 200, 40)
        label.setStyleSheet("color: #212529;")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Rencyyyy", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 510, 110, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("yes?", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(408, 555, 72, 40)
        label.setStyleSheet("color: #f1faee;"
                            "background-color: #0077b6;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("Umm when?????", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 600, 168, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)

        label = QLabel("U miss my body? :)", self)
        label.setFont(QFont("Arial", 12))
        label.setGeometry(8, 645, 180, 40)
        label.setStyleSheet("color: #212529;"
                            "background-color: #ced4da;"
                            "border-radius: 18px;"
                            "font-weight: bold")

        label.setAlignment(Qt.AlignCenter)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


