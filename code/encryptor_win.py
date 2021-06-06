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
from dialogs.password import Ui_Password as passWin


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

        self.folderName += '(encrypted)'
        shutil.make_archive(self.folderName, 'tar', dir)

    def runEncryption(self):
        self.createZip(self.dir)


class FileEncryptorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    folder_dir = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
<<<<<<< HEAD:code/encryptor_win.py
        self.windowOpacity()
        self.setWindowFlags(QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
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
<<<<<<< HEAD
=======
        # self.setWindowOpacity(0.95)
        # self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   
=======

        # self.browse_btn.clicked.connect(self.browse)
        self.encrypt_btn.clicked.connect(self.encrypt)
        self.decrypt_btn.clicked.connect(self.decrypt)

    def encrypt(self):
        self.passwin = Password()
>>>>>>> 495fb434ac4f986a839ce1062a131df2d46bec82

        self.passwin.Passwordfunc()
        # self.showPassword()

<<<<<<< HEAD
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
        

=======
        # self.folder_dir = str(
        #     QFileDialog.getExistingDirectory(self, "Select Directory"))

    def showSecondwin(self):
        self.PasswordWin = QtWidgets.QMainWindow()
        self.ui = Ui_PasswordWin()
        self.ui.setupUi(self.PasswordWin)
        self.PasswordWin.show()

    def decrypt(self):
        self.threadFunc(type='decryption')
>>>>>>> 495fb434ac4f986a839ce1062a131df2d46bec82

    def threadFunc(self, directory, type='encryption'):
        if type == 'encryption':
            self.thread = Thread()
        else:
            self.thread = Thread(type='decryption')

        self.startZip = CreateZip(dir=directory)
        self.startZip.start()
        self.statusScreen.setText('Compressing Folder\nPlease Wait')
        self.startZip.finished.connect(self.startProgress)

    def progress(self, cnt):
        self.progressBar.setValue(cnt)
        self.percentage.setText(str(cnt) + '%')
        if self.progressBar.value() == 99:
            self.progressBar.setValue(0)
            self.statusScreen.setGeometry(QtCore.QRect(90, 150, 221, 101))
            self.progressBar.setVisible(False)
            self.percentage.setVisible(False)

    def startProgress(self):
        self.statusScreen.setGeometry(QtCore.QRect(90, 100, 221, 101))
        self.progressBar.setVisible(True)
        self.percentage.setVisible(True)
        self.thread._signal.connect(self.progress)
        self.thread._percentageText.connect(self.setLoadingScreenText)
        self.thread.start()

    def setLoadingScreenText(self, msg):
        self.statusScreen.setText(msg)

<<<<<<< HEAD
>>>>>>> parent of 4b45dfc... frameless window feature has been added with the respective buttons:code/file_encryptor.py

   





=======
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
    # ----------------------------------- End --------------------------------
>>>>>>> 495fb434ac4f986a839ce1062a131df2d46bec82


class Password:
    def __init__(self):
        self.passwordWin = QtWidgets.QDialog()
        self.window = passWin()
        self.window.setupUi(self.passwordWin)

    def Passwordfunc(self):
        passwordInput = self.window.password.text()
        confirmPasswordInput = self.window.confirmPassword.text()

        if self.passwordWin.exec_() and (self.window.password.text() and self.window.confirmPassword.text()) != "":
            self.passwordValidator(
                self.window.password.text(), self.window.confirmPassword.text())

    def passwordValidator(self, a, b):
        if a != b:
            print('FAILURE')
            self.window.password.clear()
            self.window.confirmPassword.clear()
            self.passwordWin.exec_()
            print(a)
            print(b)
        else:
            print('SUCCESS')


if __name__ == "__main__":
    FileEncryptorWindow()
<<<<<<< HEAD
<<<<<<< HEAD:code/encryptor_win.py



=======
>>>>>>> parent of 4b45dfc... frameless window feature has been added with the respective buttons:code/file_encryptor.py
=======
>>>>>>> 495fb434ac4f986a839ce1062a131df2d46bec82
