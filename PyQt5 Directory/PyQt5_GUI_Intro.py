import sys
from PyQt5.QtWidgets import QApplication, QMainWindow           # Import for GUI
from PyQt5.QtGui import QIcon                                   # Import to set favicon to gui

class MainWindow(QMainWindow):                                  # main window class passing the QMainWindow imported from pyQtWidgets
    def __init__(self):                                         # Constructors of Main Window
        super().__init__()
        self.setWindowTitle("Intro GUI")                        # Set title of app
        self.setWindowIcon(QIcon("icon.jpg"))                   # set icon
        self.setGeometry(700,300,500,300)                       # set geometry | x, y (px) and width and height

def main():                                                     # MAIN FUNCTION
    app = QApplication(sys.argv)                                # create object app then call the QApp from QtWidgets then pass the sysmtem.argument
    window = MainWindow()                                       # create object = main window function
    window.show()                                               # call the object using show method (para mag show yung GUI)
    sys.exit(app.exec_())                                       # call sys.exit method tapos (app.exec_()) para magkaroon ng proper closing yung app.

if __name__ == '__main__':                                      # set to make sure that current file is running
    main()                                                      # Pag ni run yung app yung main ang mag open