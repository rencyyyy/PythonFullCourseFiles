import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Images/icon.jpg"))
        self.setGeometry(450, 200, 1024, 768)
        self.setWindowTitle("GUI Labels")

        label = QLabel("I'll touch myself na lang", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 1024, 80)
        label.setStyleSheet("color: #f4f3ee;"
                            "background-color: #3a86ff;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            # "text-decoration: underline;"
                            )

        #label.setAlignment(Qt.AlignBottom)                    # LABEL (TEXT) Align to bottom within geometry size
        #label.setAlignment(Qt.AlignRight)                     # LABEL Align to right
        #label.setAlignment(Qt.AlignLeft)                      # LABEL Align to Left
        #label.setAlignment(Qt.AlignVCenter)                   # LABEL Align to Center VERTICALLY within geometry size
        #label.setAlignment(Qt.AlignHCenter)                   # LABEL Align to Center HORIZONTALLY within geometry size

        #label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)   # RIGHT AND VERTICALLY CENTER
        #label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)    # LEFT AND VERTICALLY CENTER
        #label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)     # TOP AND HORIZONTALLY CENTER
        #label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)  # BOTTOM AND HORIZONTALLY CENTER

        #label.setAlignment(Qt.AlignTop | Qt.AlignRight)        # TOP AND RIGHT
        #label.setAlignment(Qt.AlignBottom | Qt.AlignRight)     # BOTTOM AND RIGHT
        #label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)      # LEFT AND BOTTOM
        #label.setAlignment(Qt.AlignTop | Qt.AlignLeft)         # TOP AND LEFT

        # CENTER VERTICALLY AND HORIZONTALLY
        label.setAlignment(Qt.AlignCenter)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()