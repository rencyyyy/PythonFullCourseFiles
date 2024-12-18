import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.time_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: #38b000;")
        self.setStyleSheet("background-color: #252422;")

        font_id = QFontDatabase.addApplicationFont("Font-uploaded/DS-DIGII.TTF")      # Adding costumized font
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]               # retrived the first element of font family
                                                                                      # because i'm working with a list
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)    # 1000 milliseconds
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss ap") # A - Anti meridium P - Post meridium
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())