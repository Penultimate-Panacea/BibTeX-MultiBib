from ctypes import windll
from PyQt5 import QtGui, QtWidgets, uic
from sys import exit, argv

myappid = 'fantozzi.multibib.1.0'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
qtcreator_file  = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle('MultiBib')
        self.setFixedSize(680, 490)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = MyWindow()
    window.show()
    exit(app.exec_())

