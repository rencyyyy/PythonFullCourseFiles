import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Layout")
        self.setWindowIcon(QIcon("Images/icon.jpg"))
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

        # headerText = QLabel("CHESS", self)
        # headerText.setGeometry(0,0, 500, 50)
        # headerText.setFont(QFont("Arial", 20))
        # headerText.setStyleSheet("background-color: #6f4518;"
        #                          "color: #fffcf2;"
        #                          "font-weight: bold;")
        #
        # headerText.setAlignment(Qt.AlignCenter)

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        rook1 = QLabel("rook1", self)
        horse1 = QLabel("horse1", self)
        bishop1 = QLabel("bishop1", self)
        king1 = QLabel("king", self)
        queen1 = QLabel("Queen", self)
        bishop2 = QLabel("bishop2", self)
        horse2 = QLabel("horse2", self)
        rook2 = QLabel("rook2", self)

        pawn1 = QLabel("pawn1", self)
        pawn2 = QLabel("pawn2", self)
        pawn3 = QLabel("pawn3", self)
        pawn4 = QLabel("pawn4", self)
        pawn5 = QLabel("pawn5", self)
        pawn6 = QLabel("pawn6", self)
        pawn7 = QLabel("pawn7", self)
        pawn8 = QLabel("pawn8", self)

        rook3 = QLabel("rook3", self)
        horse3 = QLabel("horse3", self)
        bishop3 = QLabel("bishop3", self)
        king2 = QLabel("king2", self)
        queen2 = QLabel("queen2", self)
        bishop4 = QLabel("bishop4", self)
        horse4 = QLabel("horse4", self)
        rook4 = QLabel("rook4", self)

        pawn9 = QLabel("pawn9", self)
        pawn10 = QLabel("pawn10", self)
        pawn11 = QLabel("pawn11", self)
        pawn12 = QLabel("pawn12", self)
        pawn13 = QLabel("pawn13", self)
        pawn14 = QLabel("pawn14", self)
        pawn15 = QLabel("pawn15", self)
        pawn16 = QLabel("pawn16", self)

        space1 = QLabel()
        space2 = QLabel()
        space3 = QLabel()
        space4 = QLabel()
        space5 = QLabel()
        space6 = QLabel()
        space7 = QLabel()
        space8 = QLabel()

        space9 = QLabel()
        space10 = QLabel()
        space11 = QLabel()
        space12 = QLabel()
        space13 = QLabel()
        space14 = QLabel()
        space15 = QLabel()
        space16 = QLabel()

        space17 = QLabel()
        space18 = QLabel()
        space19 = QLabel()
        space20 = QLabel()
        space21 = QLabel()
        space22 = QLabel()
        space23 = QLabel()
        space24 = QLabel()

        space25 = QLabel()
        space26 = QLabel()
        space27 = QLabel()
        space28 = QLabel()
        space29 = QLabel()
        space30 = QLabel()
        space31 = QLabel()
        space32 = QLabel()


        rook1.setStyleSheet("background-color: #ffedd8;"
                           "color: #ffffff;")
        rook1.setAlignment(Qt.AlignCenter)
        horse1.setStyleSheet("background-color: #403d39;"
                           "color: #ffffff;")
        horse1.setAlignment(Qt.AlignCenter)
        bishop1.setStyleSheet("background-color: #ffedd8;"
                           "color: #ffffff;")
        bishop1.setAlignment(Qt.AlignCenter)
        king1.setStyleSheet("background-color: #403d39;"
                           "color: #ffffff;")
        king1.setAlignment(Qt.AlignCenter)
        queen1.setStyleSheet("background-color: #ffedd8;"
                           "color: #ffffff;")
        queen1.setAlignment(Qt.AlignCenter)
        bishop2.setStyleSheet("background-color: #403d39;"
                              "color: #ffffff;")
        bishop2.setAlignment(Qt.AlignCenter)
        horse2.setStyleSheet("background-color: #ffedd8;"
                             "color: #ffffff;")
        horse2.setAlignment(Qt.AlignCenter)
        rook2.setStyleSheet("background-color: #403d39;"
                            "color: #ffffff;")
        rook2.setAlignment(Qt.AlignCenter)
        pawn1.setStyleSheet("background-color: #403d39;"
                            "color: #ffffff;")
        pawn1.setAlignment(Qt.AlignCenter)
        pawn2.setStyleSheet("background-color: #ffedd8;"
                            "color: #ffffff;")
        pawn2.setAlignment(Qt.AlignCenter)
        pawn3.setStyleSheet("background-color: #403d39;"
                            "color: #ffffff;")
        pawn3.setAlignment(Qt.AlignCenter)
        pawn4.setStyleSheet("background-color: #ffedd8;"
                            "color: #ffffff;")
        pawn4.setAlignment(Qt.AlignCenter)
        pawn5.setStyleSheet("background-color: #403d39;"
                            "color: #ffffff;")
        pawn5.setAlignment(Qt.AlignCenter)
        pawn6.setStyleSheet("background-color: #ffedd8;"
                            "color: #ffffff;")
        pawn6.setAlignment(Qt.AlignCenter)
        pawn7.setStyleSheet("background-color: #403d39;"
                            "color: #ffffff;")
        pawn7.setAlignment(Qt.AlignCenter)
        pawn8.setStyleSheet("background-color: #ffedd8;"
                            "color: #ffffff;")
        pawn8.setAlignment(Qt.AlignCenter)

        rook3.setStyleSheet("background-color: #403d39;"
                           "color: #000000;")
        rook3.setAlignment(Qt.AlignCenter)
        horse3.setStyleSheet("background-color: #ffedd8;"
                           "color: #000000;")
        horse3.setAlignment(Qt.AlignCenter)
        bishop3.setStyleSheet("background-color: #403d39;"
                           "color: #000000;")
        bishop3.setAlignment(Qt.AlignCenter)
        king2.setStyleSheet("background-color: #403d39;"
                           "color: #000000;")
        king2.setAlignment(Qt.AlignCenter)
        queen2.setStyleSheet("background-color: #ffedd8;"
                           "color: #000000;")
        queen2.setAlignment(Qt.AlignCenter)
        bishop4.setStyleSheet("background-color: #ffedd8;"
                              "color: #000000;")
        bishop4.setAlignment(Qt.AlignCenter)
        horse4.setStyleSheet("background-color: #403d39;"
                             "color: #000000;")
        horse4.setAlignment(Qt.AlignCenter)
        rook4.setStyleSheet("background-color: #ffedd8;"
                            "color: #000000;")
        rook4.setAlignment(Qt.AlignCenter)
        pawn9.setStyleSheet("background-color: #ffedd8;"
                            "color: #000000;")
        pawn9.setAlignment(Qt.AlignCenter)
        pawn10.setStyleSheet("background-color: #403d39;"
                            "color: #000000;")
        pawn10.setAlignment(Qt.AlignCenter)
        pawn11.setStyleSheet("background-color: #ffedd8;"
                            "color: #000000;")
        pawn11.setAlignment(Qt.AlignCenter)
        pawn12.setStyleSheet("background-color: #403d39;"
                            "color: #000000;")
        pawn12.setAlignment(Qt.AlignCenter)
        pawn13.setStyleSheet("background-color: #ffedd8;"
                            "color: #000000;")
        pawn13.setAlignment(Qt.AlignCenter)
        pawn14.setStyleSheet("background-color: #403d39;"
                            "color: #000000;")
        pawn14.setAlignment(Qt.AlignCenter)
        pawn15.setStyleSheet("background-color: #ffedd8;"
                            "color: #000000;")
        pawn15.setAlignment(Qt.AlignCenter)
        pawn16.setStyleSheet("background-color: #403d39;"
                            "color: #000000;")
        pawn16.setAlignment(Qt.AlignCenter)

        space1.setStyleSheet("background-color: #ffedd8;")
        space2.setStyleSheet("background-color: #403d39;")
        space3.setStyleSheet("background-color: #ffedd8;")
        space4.setStyleSheet("background-color: #403d39;")
        space5.setStyleSheet("background-color: #ffedd8;")
        space6.setStyleSheet("background-color: #403d39;")
        space7.setStyleSheet("background-color: #ffedd8;")
        space8.setStyleSheet("background-color: #403d39;")

        space9.setStyleSheet("background-color: #403d39;")
        space10.setStyleSheet("background-color: #ffedd8;")
        space11.setStyleSheet("background-color: #403d39;")
        space12.setStyleSheet("background-color: #ffedd8;")
        space13.setStyleSheet("background-color: #403d39;")
        space14.setStyleSheet("background-color: #ffedd8;")
        space15.setStyleSheet("background-color: #403d39;")
        space16.setStyleSheet("background-color: #ffedd8;")

        space17.setStyleSheet("background-color: #ffedd8;")
        space18.setStyleSheet("background-color: #403d39;")
        space19.setStyleSheet("background-color: #ffedd8;")
        space20.setStyleSheet("background-color: #403d39;")
        space21.setStyleSheet("background-color: #ffedd8;")
        space22.setStyleSheet("background-color: #403d39;")
        space23.setStyleSheet("background-color: #ffedd8;")
        space24.setStyleSheet("background-color: #403d39;")

        space25.setStyleSheet("background-color: #403d39;")
        space26.setStyleSheet("background-color: #ffedd8;")
        space27.setStyleSheet("background-color: #403d39;")
        space28.setStyleSheet("background-color: #ffedd8;")
        space29.setStyleSheet("background-color: #403d39;")
        space30.setStyleSheet("background-color: #ffedd8;")
        space31.setStyleSheet("background-color: #403d39;")
        space32.setStyleSheet("background-color: #ffedd8;")

        grid = QGridLayout()

        grid.addWidget(rook1, 0, 0)
        grid.addWidget(horse1, 0, 1)
        grid.addWidget(bishop1, 0, 2)
        grid.addWidget(king1, 0, 3)
        grid.addWidget(queen1, 0, 4)
        grid.addWidget(bishop2, 0, 5)
        grid.addWidget(horse2, 0, 6)
        grid.addWidget(rook2, 0, 7)

        grid.addWidget(pawn1, 1, 0)
        grid.addWidget(pawn2, 1, 1)
        grid.addWidget(pawn3, 1, 2)
        grid.addWidget(pawn4, 1, 3)
        grid.addWidget(pawn5, 1, 4)
        grid.addWidget(pawn6, 1, 5)
        grid.addWidget(pawn7, 1, 6)
        grid.addWidget(pawn8, 1, 7)

        grid.addWidget(space1, 2, 0)
        grid.addWidget(space2, 2, 1)
        grid.addWidget(space3, 2, 2)
        grid.addWidget(space4, 2, 3)
        grid.addWidget(space5, 2, 4)
        grid.addWidget(space6, 2, 5)
        grid.addWidget(space7, 2, 6)
        grid.addWidget(space8, 2, 7)

        grid.addWidget(space9, 3, 0)
        grid.addWidget(space10, 3, 1)
        grid.addWidget(space11, 3, 2)
        grid.addWidget(space12, 3, 3)
        grid.addWidget(space13, 3, 4)
        grid.addWidget(space14, 3, 5)
        grid.addWidget(space15, 3, 6)
        grid.addWidget(space16, 3, 7)

        grid.addWidget(space17, 4, 0)
        grid.addWidget(space18, 4, 1)
        grid.addWidget(space19, 4, 2)
        grid.addWidget(space20, 4, 3)
        grid.addWidget(space21, 4, 4)
        grid.addWidget(space22, 4, 5)
        grid.addWidget(space23, 4, 6)
        grid.addWidget(space24, 4, 7)

        grid.addWidget(space25, 5, 0)
        grid.addWidget(space26, 5, 1)
        grid.addWidget(space27, 5, 2)
        grid.addWidget(space28, 5, 3)
        grid.addWidget(space29, 5, 4)
        grid.addWidget(space30, 5, 5)
        grid.addWidget(space31, 5, 6)
        grid.addWidget(space32, 5, 7)

        grid.addWidget(pawn9, 6, 0)
        grid.addWidget(pawn10, 6, 1)
        grid.addWidget(pawn11, 6, 2)
        grid.addWidget(pawn12, 6, 3)
        grid.addWidget(pawn13, 6, 4)
        grid.addWidget(pawn14, 6, 5)
        grid.addWidget(pawn15, 6, 6)
        grid.addWidget(pawn16, 6, 7)

        grid.addWidget(rook3, 7, 0)
        grid.addWidget(horse3, 7, 1)
        grid.addWidget(bishop3, 7, 2)
        grid.addWidget(queen2, 7, 3)
        grid.addWidget(king2, 7, 4)
        grid.addWidget(bishop4, 7, 5)
        grid.addWidget(horse4, 7, 6)
        grid.addWidget(rook4, 7, 7)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()