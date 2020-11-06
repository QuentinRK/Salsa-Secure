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

    

   


    # --------- Window Button Functions ---------
    def maximize(self):
        if (self.MaximizeWin.isChecked()):
            self.Container.setStyleSheet("QFrame {\n"
        "    background-color:rgb(50, 50, 50);\n"
            "    borders:none;\n"
        "    border-radius:0px;\n"
        "}")      
            self.showMaximized()
           

        else:
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            # resets original border
            self.Container.setStyleSheet("QFrame {\n"
"    background-color:rgb(50, 50, 50);\n"
"    borders:none;\n"
"    border-radius:10px;\n"
"}")     
           

        
    def minimize(self):
        self.showMinimized()
    # ------------------ End --------------------

     # ------------------- Mouse Function For Moving Calculator ---------------
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    # ----------------------------------- End -------------------------------- 




        

 
    



if __name__ == "__main__":
    FileEncryptorWindow()



