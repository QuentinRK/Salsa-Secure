import os
import shutil
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, QThread, pyqtSignal, QRect
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QInputDialog,
                             QSizeGrip, QVBoxLayout, QWidget)

from encryptor import encryptor
from encryptor_ui import Ui_MainWindow



class Thread(QThread):
    _signal = pyqtSignal(int)
    _percentageText = pyqtSignal(str)

    def __init__(self, type='encryption'):
        super(Thread, self).__init__()
        if type == 'decryption':
            self.msg1 = 'Initiating Decryption'
            self.msg2 = 'Decompressing Folder'
            self.msg3 = 'Decrypting Contents'
            self.msg4 = 'Finalizing Decryption'
        elif type == 'encryption':
            self.msg1 = 'Initiating Encryption'
            self.msg2 = 'Compressing Folder'
            self.msg3 = 'Encrypting Contents'
            self.msg4 = 'Finalizing Encryption'
        else:
            print('no valid type has been entered')

    def run(self):
        for i in range(100):
            time.sleep(0.1)
            self._signal.emit(i)
            if i == 0:
                self._percentageText.emit(self.msg1)
            elif i == 25:
                self._percentageText.emit(self.msg2)
            elif i == 50:
                self._percentageText.emit(self.msg3)
            elif i == 75:
                self._percentageText.emit(self.msg4)
            elif i == 99:
                self._percentageText.emit('Ready')


class CreateZip(QThread):
    def __init__(self, dir):
        super().__init__()
        self.dir = dir

    def run(self):
        self.runEncryption()

    def createZip(self, dir):
        dirList = dir.split('/')
        self.folderName = dirList[-1]
        dirList.pop()
        self.newDir = '/'.join(dirList)
        os.chdir(self.newDir)

        shutil.make_archive(self.folderName, 'tar', dir)

    def runEncryption(self):
        self.createZip(self.dir)


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

        self.statusScreen.setGeometry(QtCore.QRect(90, 150, 221, 101))

        self.progressBar.setVisible(False)
        self.percentage.setVisible(False)

        self.progressBar.setValue(0)
        # -------------- Setting Functions To Window Buttons -----
        self.MaximizeWin.clicked.connect(self.maximize)
        self.MinimizeWin.clicked.connect(self.minimize)
        self.ExitWin.clicked.connect(QtWidgets.qApp.quit)
        self.MaximizeWin.setCheckable(True)
        self.oldPos = self.pos()
        # ------------------------- End --------------------------

        # self.browse_btn.clicked.connect(self.browse)
        self.encrypt_btn.clicked.connect(self.encrypt)
        self.decrypt_btn.clicked.connect(self.decrypt)

    def encrypt(self):
        # Gather the location of the folder to encrypt
        self.folder_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        # Create a zip file from the folder
        self.threadFunc(self.folder_dir, "encryption")

        # Store the new zip file directory 
        zip_directory = self.folder_dir + ".tar"

        # pass the directory and key to the encrypt function 

        # TODO: Must implement a way for this response to wait for the thread to finish 
        time.sleep(5)

        # TODO: Must gather user input for the key 
        encryptor.encrypt(self, key="hello", file=zip_directory)




    def decrypt(self):
         # Gather the location of the folder to encrypt
        options = QFileDialog.Options()
        self.folder_dir = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","Zip Files (*.tar)", options=options)

        # TODO: Need to gather user input for validation 
        encryptor.decrypt(self, self.folder_dir[0])

    def threadFunc(self, directory, type):
        self.startZip = CreateZip(dir=directory)
        self.startZip.start()
        self.statusScreen.setText('Compressing Folder\nPlease Wait')
        self.startZip.finished.connect(lambda: self.startProgress(type))

    def progress(self, cnt):
        self.progressBar.setValue(cnt)
        self.percentage.setText(str(cnt) + '%')
        if self.progressBar.value() == 99:
            self.progressBar.setValue(0)
            self.statusScreen.setGeometry(QtCore.QRect(90, 150, 221, 101))
            self.progressBar.setVisible(False)
            self.percentage.setVisible(False)

    def startProgress(self, type="encryption"):
        if type == "decryption":
            threadType = "decryption"
        else:
            threadType= "encryption"

        self.thread = Thread(type=threadType)
        self.statusScreen.setGeometry(QtCore.QRect(90, 100, 221, 101))
        self.progressBar.setVisible(True)
        self.percentage.setVisible(True)
        self.thread._signal.connect(self.progress)
        self.thread._percentageText.connect(self.setLoadingScreenText)
        self.thread.start()

    def setLoadingScreenText(self, msg):
        self.statusScreen.setText(msg)

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
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    # ----------------------------------- End -----------------#

if __name__ == "__main__":
    FileEncryptorWindow()