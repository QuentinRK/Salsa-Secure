from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from fileEncryptor_ui import Ui_MainWindow


class FileEncryptorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowOpacity(0.95)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        self.show()
        


if __name__ == "__main__":
    FileEncryptorWindow()
