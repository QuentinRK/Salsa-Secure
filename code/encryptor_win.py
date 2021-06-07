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
from password_dialog import decryptionPass, encryptionPass
from Crypto.Hash import MD5


class Password(QDialog):
    def __init__(self, parent=None, type="encryption"):
        super().__init__(parent)
        if type == "decryption":
            self.passui = decryptionPass.Ui_Dialog()
        else:
            self.passui = encryptionPass.Ui_Dialog()
        
        self.passui.setupUi(self)       

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
    directory = pyqtSignal(str)

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
        self.directory.emit(self.dir)

    def runEncryption(self):
        self.createZip(self.dir)

class RunCiphers(QThread):
    not_successful =  pyqtSignal(str)
    is_successful = pyqtSignal(bool)

    def __init__(self, directory, secret=None, mode="encrypt"):
        super().__init__()
        self.directory = directory
        self.key = secret
        self.mode = mode

        
    def run(self):
        if self.mode == "decrypt":
            self.decrypt()
        else:
            self.encrypt()

    def encrypt(self):
        zip_directory = self.directory + ".tar"

        new_hash = MD5.new(bytes(self.key, 'utf-8'))
        key = new_hash.digest()
        print(new_hash.hexdigest())

        encryptor.encrypt(self, zip_directory, key)


    def decrypt(self):

        new_hash = MD5.new(bytes(self.key, 'utf-8'))
        key = new_hash.digest()
    
        file = self.directory
        self.decryptresult = encryptor.decrypt(self, file, key)
        if (not self.decryptresult):
            self.not_successful.emit("Decryption Failed")
        else:
            self.is_successful.emit(True)

class FileEncryptorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

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
        self.encrypt_btn.clicked.connect(self.runCiphers)
        self.decrypt_btn.clicked.connect(lambda: self.runCiphers(mode="decrypt"))

    def threadFunc(self, directory, type="encrypt"):
        self.startZip = CreateZip(dir=directory)
        self.startZip.start()
        if type == "decrypt":
            self.startZip.finished.connect(lambda: self.decrpyt(directory=directory))

        self.statusScreen.setText('Compressing Folder\nPlease Wait')
        self.startZip.finished.connect(lambda: self.encrypt(directory=directory))

    def runCiphers(self, mode="encrypt"):
        if mode == "decrypt":
              self.folder_dir = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","Zip Files (*.tar)")
              if self.folder_dir != "":
                  self.decrypt(self.folder_dir[0])
        else:
            self.folder_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            if self.folder_dir != "":
                self.threadFunc(self.folder_dir)

    
    def encrypt(self, directory):
        passwin = Password(self)
        matching_password = True
        validation = False
        key = None

        while(matching_password):
            passwin.exec_()
            passw = passwin.passui.password.text()
            confirm_passw = passwin.passui.confirm_password.text()
            if (passw == confirm_passw):
                validation = True
                key = passw
                matching_password = False

            elif passwin.close():
                validation = False
                self.statusScreen.setText('Password did not match')
                matching_password = False
                os.remove(directory + ".tar")
        
            passwin.passui.confirm_password.clear()
            passwin.passui.password.clear()


        if validation:  
            self.run_encrypt = RunCiphers(directory=directory, secret=key)
            self.run_encrypt.start()
            self.run_encrypt.finished.connect(lambda: self.startProgress(type))

    def decrypt(self, directory):
        decrypt_cipher = Password(self, type="decryption")


        if decrypt_cipher.exec_():
            password = decrypt_cipher.passui.password.text()
            password = password.strip()
            if password != "":
                decrypt_cipher.close()
                self.run_decrypt = RunCiphers(directory=directory, mode="decrypt", secret=password)
                self.run_decrypt.start()
                self.statusScreen.setText('Decompressing Folder\nPlease Wait')
                self.run_decrypt.not_successful.connect(lambda: self.statusScreen.setText("Decryption Failed"))
                self.run_decrypt.is_successful.connect(lambda: self.startProgress(type="decryption"))
            else:
                self.statusScreen.setText('Invalid Input')
        
            

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

    # --------- Window Button Functions ------------------#

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
    # ------------------ End ---------------------------#

    # ------------------- Mouse Function ---------------------#
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