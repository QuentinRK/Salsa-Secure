from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip, QFileDialog, QInputDialog
from PyQt5.QtGui import QColor, QPalette, QBrush
from fileEncryptor_ui import Ui_MainWindow
import shutil
import os


class FileEncryptorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    folder_dir = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        # self.setWindowOpacity(0.95)
        # self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   


        self.show()

        self.browse_btn.clicked.connect(self.browse)
        self.encrypt_btn.clicked.connect(self.compress)

    def browse(self):
        options = QFileDialog.Options()
        self.folder_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        self.search.setText(self.folder_dir)
    
    def compress(self):
        
        fileFormat = 'zip'

        compressName = QInputDialog.getText(self, 'Zip Filename', 'Provide a name for the zip file: ')
      
        shutil.make_archive(compressName[0], fileFormat, self.folder_dir)

        base = os.getcwd()
    
        shutil.move((base +'/{}.{}'.format(compressName[0], fileFormat)), (self.folder_dir +'/{}.{}'.format(compressName[0], fileFormat)))
        










if __name__ == "__main__":
    FileEncryptorWindow()
