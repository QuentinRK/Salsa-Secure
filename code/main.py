import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from encryptor_win import FileEncryptorWindow

app = QApplication(sys.argv)
 
calculator = FileEncryptorWindow()

sys.exit(app.exec_())

