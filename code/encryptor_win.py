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




# -------------------Start Of Thread (Password Window)------------ #
class PasswordWin(QDialog):

    # encryption password validation is the default  
    def __init__(self, parent=None, type="encryption"):
        super().__init__(parent)
        if type == "decryption":

            self.password_ui = decryptionPass.Ui_Dialog()
        else:
            self.password_ui = encryptionPass.Ui_Dialog()
        
        self.password_ui.setupUi(self)       
# -------------------Start Of Thread (Password Window)------------ #


# -------------------Start Of Thread (ProgressBar)---------------- #
class Progress(QThread):
    _signal = pyqtSignal(int)
    _percentageText = pyqtSignal(str)

    def __init__(self, type='encryption'):
        super(Progress, self).__init__()
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
# -------------------End Of Thread (ProgressBar)------------------ #


# -------------------Start Of Thread (ZipFile)-------------------- #
class CreateZip(QThread):

    def __init__(self, directory):
        super().__init__()
        self.directory = directory

    def run(self):
        self.run_zip()

    def createZip(self, directory):

        # split directory into individual strings   
        directory_list = directory.split('/')

        # select the last string in the list for the folder name
        self.folder_name = directory_list[-1]

        # remove the last items from the list 
        directory_list.pop()

        # join the remainding strings to get the current working directory
        self.current_directory = '/'.join(directory_list)

        # move env to specified directory 
        os.chdir(self.current_directory)

        # make a tar file 
        shutil.make_archive(self.folder_name, 'tar', directory)
        


    def run_zip(self):
        self.createZip(self.directory)
# -------------------End Of Thread (ZipFile)---------------------- #



# -------------------Start Of Thread (Ciphers)-------------------- #
class RunCiphers(QThread):

    cipher_not_successful =  pyqtSignal(str)
    cipher_successful = pyqtSignal(bool)

    def __init__(self, directory, secret=None, mode="encrypt"):
        super().__init__()
        self.directory = directory
        self.key = secret
        self.mode = mode

    # mode is defaulted to encrypt 
    def run(self):
        if self.mode == "decrypt":
            self.decrypt()
        else:
            self.encrypt()

    # encryption thread 
    def encrypt(self):

        # creates a string that represents the target file 
        zip_directory = self.directory + ".tar"

        # MD5 hash for the users key (1st Hash)
        new_hash = MD5.new(bytes(self.key, 'utf-8'))
        key = new_hash.digest()

        # run the encryptor
        encryptor.encrypt(self, zip_directory, key)

    # decryption thread
    def decrypt(self):

        # MD5 hash for the users key 
        new_hash = MD5.new(bytes(self.key, 'utf-8'))
        key = new_hash.digest()

        # directory for the encrypted file 
        file = self.directory

        # the decrypt function returns True if successful 
        self.decrypt_result = encryptor.decrypt(self, file, key)

        # if decryption has failed emit the error message 
        if (not self.decrypt_result):
            self.cipher_not_successful.emit("Decryption Failed")
        else:
            # returns True and executes the decryption 
            self.cipher_successful.emit(True)

# -------------------End Of Thread (Ciphers)---------------------- #



# -------------------Start Of Main Window------------------------- #
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
        self.encrypt_btn.clicked.connect(self.run_ciphers)
        self.decrypt_btn.clicked.connect(lambda: self.run_ciphers(mode="decrypt"))

    # runs the zip thread and calls the encrypt function 
    def thread_func(self, directory, mode="encrypt"):

        # initailise & start the zip thread 
        self.startZip = CreateZip(directory=directory)
        self.startZip.start()

        # run the encrypt function after the zip file has been made 
        self.statusScreen.setText('Compressing Folder\nPlease Wait')
        self.startZip.finished.connect(lambda: self.encrypt(directory=directory))


    """
    run_ciphers is connected to the encrypt and decrypt buttons. 

    It also gathers the directory of the file of interest
    """

    def run_ciphers(self, mode="encrypt"):

        # once the decrypt function is called
        if mode == "decrypt":

              # prompt the user for the location of the encrypted file 
              self.file_directory = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","Zip Files (*.tar)")

              # if the input is not empty then call the decrypt function   
              if self.file_directory != "":
                  self.decrypt(self.file_directory[0])
        else:

            # otherwise run the encrypt function 
            self.folder_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            if self.folder_dir != "":

                # the thread function is called to create a zip and encrypt the file 
                self.thread_func(self.folder_dir)


    # runs the encryption method
    def encrypt(self, directory):
        passord_window = PasswordWin(self)
        matching_passwords = True
        validation = False
        key = None

        # while matching the passwords
        while(matching_passwords):

            # rum the password window 
            passord_window.exec_()

            #store the user's input in variables  
            password = passord_window.password_ui.password.text().strip()
            confirm_password = passord_window.password_ui.confirm_password.text().strip()

            # if both passwords are the same then break out of the loop 
            if (password == confirm_password):
                validation = True
                key = password
                matching_passwords = False

            # other print an error message on the status screen 
            elif passord_window.close():
                validation = False
                self.statusScreen.setText('Password did not match')
                matching_passwords = False
                os.remove(directory + ".tar")
        
            # clear the input for the passwords
            passord_window.password_ui.confirm_password.clear()
            passord_window.password_ui.password.clear()

        # if the passwords have been validated
        if validation:  

            # run the cipher thread
            self.run_encrypt = RunCiphers(directory=directory, secret=key)
            self.run_encrypt.start()

            # once the thread has finished start the progress bar 
            self.run_encrypt.finished.connect(lambda: self.startProgress(type))


    # runs the decryption method
    def decrypt(self, directory):
        
        # initialise the password window 
        password_window = PasswordWin(self, type="decryption")

        # run the password window 
        if password_window.exec_():

            # store the user's input 
            password = password_window.password_ui.password.text()

            # strip all white spaces
            password = password.strip()

            # if the input has an input 
            if password != "":

                # close the dialog window
                password_window.close()

                # run the decryption cipher 
                self.run_decrypt = RunCiphers(directory=directory, mode="decrypt", secret=password)
                self.run_decrypt.start()
                self.statusScreen.setText('Decompressing Folder\nPlease Wait')

                # recieve the signals from the thread 
                # if unsuccessful the error message is printed 
                self.run_decrypt.cipher_not_successful.connect(lambda: self.statusScreen.setText("Decryption Failed"))

                # if successful then run the progression bar
                self.run_decrypt.cipher_successful.connect(lambda: self.startProgress(type="decryption"))
            else:
                self.statusScreen.setText('Invalid Input')
        

    # function that returns emited values for progress bar 
    def progress(self, cnt):

        # progress function for the status screen 
        self.progressBar.setValue(cnt)
        self.percentage.setText(str(cnt) + '%')

        # if the value emited is 99 then reset the values 
        if self.progressBar.value() == 99:
            self.progressBar.setValue(0)
            self.statusScreen.setGeometry(QtCore.QRect(90, 150, 221, 101))
            self.progressBar.setVisible(False)
            self.percentage.setVisible(False)


    # thread used for the progress bar 
    def startProgress(self, type="encryption"):
        
        """ 
        encryption is defaulted running the encryption messages 
        on the screen 
        
        """

        if type == "decryption":
            threadType = "decryption"
        else:
            threadType= "encryption"

        # run the thread for the progress bar 
        self.thread = Progress(type=threadType)
        self.statusScreen.setGeometry(QtCore.QRect(90, 100, 221, 101))
        self.progressBar.setVisible(True)
        self.percentage.setVisible(True)
        self.thread._signal.connect(self.progress)
        self.thread._percentageText.connect(self.setLoadingScreenText)
        self.thread.start()
        

    # function returns emitted message from progress thread
    def setLoadingScreenText(self, msg):
        self.statusScreen.setText(msg)


    # --------- Window Button Functions ------------------#

    def maximize(self):
        if (self.MaximizeWin.isChecked()):

            # when maximized alter the display  
            self.Container.setStyleSheet
            ("QFrame {\n"
            "background-color:rgb(50, 50, 50);\n"
            "borders:none;\n"
            "border-radius:0px;\n"
            "}")
            self.showMaximized()

        else:

            self.showNormal()

            # resest to the orignal dimensions 
            self.resize(self.width()+1, self.height()+1)

            # resets original border
            self.Container.setStyleSheet
            ("QFrame {\n"
             "background-color:rgb(50, 50, 50);\n"
             "borders:none;\n"
             "border-radius:10px;\n"
            "}")

    def minimize(self):
        self.showMinimized()
    # ------------------ End ---------------------------#



    # ------------------- Mouse Function ---------------------#
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    # ----------------------------------- End -----------------#


# -------------------END Of Main Window--------------------------- #



if __name__ == "__main__":
    FileEncryptorWindow()