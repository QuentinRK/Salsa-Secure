import sys
from PyQt5.QtWidgets import QApplication
from file_encryptor import FileEncryptorWindow

app = QApplication(sys.argv)

calculator = FileEncryptorWindow()

sys.exit(app.exec_())

