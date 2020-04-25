import bibtexparser
from tqdm import tqdm
from ctypes import windll
from PyQt5 import QtGui, QtWidgets, uic
from sys import exit, argv

myappid = 'fantozzi.multibib.1.0'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
qtcreator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle('MultiBib')
        self.setFixedSize(680, 490)
        self.setupUi(self)
        self.dedupFileButton.clicked.connect(self.import_bibfile('d'))
    #    self.firstFileButton.clicked.connect(self.import_bibfile('1'))
    #    self.secondFileButton.clicked.connect(self.import_bibfile('2'))
        self.dedupDB = None
        self.firstDB = None
        self.secondDB = None

    def import_bibfile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, filter="BibTeX (*.bib)")
        with open(str(filename), encoding='utf8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
        if dictcode == 'd':
            self.dedupDB = bib_database
        elif dictcode == '1':
            self.firstDB = bib_database
        elif dictcode == '2':
            self.secondDB = bib_database
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = MyWindow()
    window.show()
    exit(app.exec_())
