from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip, QFileDialog, QInputDialog
from PyQt5.QtGui import QColor, QPalette, QBrush
from encryptor_ui import Ui_MainWindow
import shutil
import os
from encryptor import encryptor 


class FileEncryptorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    folder_dir = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
<<<<<<< HEAD:code/encryptor_win.py
        self.windowOpacity()
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.show()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 

        # -------------- Setting Functions To Window Buttons -----
        self.MaximizeWin.clicked.connect(self.maximize)
        self.MinimizeWin.clicked.connect(self.minimize)
        self.ExitWin.clicked.connect(QtWidgets.qApp.quit)
        self.MaximizeWin.setCheckable(True)
        self.oldPos = self.pos()
        # ------------------------- End --------------------------
=======
        # self.setWindowOpacity(0.95)
        # self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   


        self.show()
>>>>>>> parent of 4b45dfc... frameless window feature has been added with the respective buttons:code/file_encryptor.py

        self.browse_btn.clicked.connect(self.browse)
        self.encrypt_btn.clicked.connect(self.compress) 

    def browse(self):
        options = QFileDialog.Options()
        self.folder_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.search.setText(self.folder_dir)
    
    def compress(self):
        e = encryptor()
        fileFormat = 'zip'
        compressName = QInputDialog.getText(self, 'Zip Filename', 'Provide a name for the zip file: ')
        zipfile = shutil.make_archive(compressName[0], fileFormat, self.folder_dir)
        e.encrypt(zipfile)
        # base = os.getcwd()
        # shutil.move( zipfile , (self.folder_dir +'/{}.{}'.format(compressName[0], fileFormat)))

    
<<<<<<< HEAD:code/encryptor_win.py
=======
        shutil.move((base +'/{}.{}'.format(compressName[0], fileFormat)), (self.folder_dir +'/{}.{}'.format(compressName[0], fileFormat)))
        



>>>>>>> parent of 4b45dfc... frameless window feature has been added with the respective buttons:code/file_encryptor.py

   






        

 
    



if __name__ == "__main__":
    FileEncryptorWindow()
<<<<<<< HEAD:code/encryptor_win.py



=======
>>>>>>> parent of 4b45dfc... frameless window feature has been added with the respective buttons:code/file_encryptor.py
