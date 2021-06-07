import sys
import time
from PyQt5.QtWidgets import QApplication
from encryptor_win import FileEncryptorWindow

# Inialise app
app = QApplication(sys.argv)

# Displays app
calculator = FileEncryptorWindow()

# Exit out of the app
sys.exit(app.exec_())
