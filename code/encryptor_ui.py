# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryptor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(450, 718)
        MainWindow.setMinimumSize(QtCore.QSize(400, 718))
        font = QtGui.QFont()
        font.setFamily(".AppleTraditionalChineseFont")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color:rgb(50, 50, 50);\n"
"    borders:none;\n"
"    border-radius:10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Container = QtWidgets.QFrame(self.centralwidget)
        self.Container.setMinimumSize(QtCore.QSize(0, 530))
        self.Container.setStyleSheet("QFrame {\n"
"    background-color:  #f8f7f9;\n"
"    borders:none;\n"
"    border-radius:6px;\n"
"}")
        self.Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container.setObjectName("Container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Container)
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 25)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Header = QtWidgets.QFrame(self.Container)
        self.Header.setMaximumSize(QtCore.QSize(593, 134))
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.WinBtns = QtWidgets.QFrame(self.Header)
        self.WinBtns.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WinBtns.sizePolicy().hasHeightForWidth())
        self.WinBtns.setSizePolicy(sizePolicy)
        self.WinBtns.setMinimumSize(QtCore.QSize(100, 0))
        self.WinBtns.setMaximumSize(QtCore.QSize(100, 20))
        self.WinBtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WinBtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WinBtns.setObjectName("WinBtns")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.WinBtns)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExitWin = QtWidgets.QPushButton(self.WinBtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitWin.sizePolicy().hasHeightForWidth())
        self.ExitWin.setSizePolicy(sizePolicy)
        self.ExitWin.setMinimumSize(QtCore.QSize(13, 13))
        self.ExitWin.setMaximumSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.ExitWin.setFont(font)
        self.ExitWin.setStyleSheet("QPushButton{\n"
"    display:flex;\n"
"    border:none;\n"
"    border-radius:6px;\n"
"    background-color: rgb(255, 56, 0);\n"
"    color:rgb(249, 60, 0);\n"
"    justify-contents:center;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: rgb(193, 46, 0);\n"
"}\n"
"")
        self.ExitWin.setCheckable(False)
        self.ExitWin.setAutoDefault(False)
        self.ExitWin.setObjectName("ExitWin")
        self.horizontalLayout.addWidget(self.ExitWin)
        self.MinimizeWin = QtWidgets.QPushButton(self.WinBtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinimizeWin.sizePolicy().hasHeightForWidth())
        self.MinimizeWin.setSizePolicy(sizePolicy)
        self.MinimizeWin.setMinimumSize(QtCore.QSize(13, 13))
        self.MinimizeWin.setMaximumSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setFamily("Al Bayan")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.MinimizeWin.setFont(font)
        self.MinimizeWin.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:6px;\n"
"    background-color: rgb(255, 201, 3);\n"
"    color:rgb(255, 201, 3);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: rgb(221, 177, 0);\n"
"}\n"
"")
        self.MinimizeWin.setCheckable(False)
        self.MinimizeWin.setAutoDefault(False)
        self.MinimizeWin.setObjectName("MinimizeWin")
        self.horizontalLayout.addWidget(self.MinimizeWin)
        self.MaximizeWin = QtWidgets.QPushButton(self.WinBtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MaximizeWin.sizePolicy().hasHeightForWidth())
        self.MaximizeWin.setSizePolicy(sizePolicy)
        self.MaximizeWin.setMinimumSize(QtCore.QSize(13, 13))
        self.MaximizeWin.setMaximumSize(QtCore.QSize(13, 13))
        self.MaximizeWin.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.MaximizeWin.setFont(font)
        self.MaximizeWin.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:6px;\n"
"    background-color: rgb(55, 202, 65);\n"
"    color:rgb(55, 202, 65);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: rgb(58, 153, 14);\n"
"}\n"
"")
        self.MaximizeWin.setAutoDefault(False)
        self.MaximizeWin.setObjectName("MaximizeWin")
        self.horizontalLayout.addWidget(self.MaximizeWin)
        self.horizontalLayout_2.addWidget(self.WinBtns)
        self.verticalLayout_2.addWidget(self.Header, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Title = QtWidgets.QFrame(self.Container)
        self.Title.setMinimumSize(QtCore.QSize(0, 50))
        self.Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setObjectName("Title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Title)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.File_Encryptor = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setFamily("Bodoni 72")
        font.setPointSize(55)
        self.File_Encryptor.setFont(font)
        self.File_Encryptor.setStyleSheet("QLabel{\n"
"    color: #e52a0d;\n"
"\n"
"}")
        self.File_Encryptor.setAlignment(QtCore.Qt.AlignCenter)
        self.File_Encryptor.setObjectName("File_Encryptor")
        self.horizontalLayout_4.addWidget(self.File_Encryptor)
        self.verticalLayout_2.addWidget(self.Title)
        self.body = QtWidgets.QFrame(self.Container)
        self.body.setMinimumSize(QtCore.QSize(300, 700))
        self.body.setMaximumSize(QtCore.QSize(16777215, 600))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(20)
        self.body.setFont(font)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.gridLayout = QtWidgets.QGridLayout(self.body)
        self.gridLayout.setContentsMargins(0, 0, 0, 10)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Info_Screen = QtWidgets.QFrame(self.body)
        self.Info_Screen.setMinimumSize(QtCore.QSize(400, 400))
        self.Info_Screen.setMaximumSize(QtCore.QSize(400, 400))
        self.Info_Screen.setObjectName("Info_Screen")
        self.outline = QtWidgets.QLabel(self.Info_Screen)
        self.outline.setGeometry(QtCore.QRect(0, 0, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outline.sizePolicy().hasHeightForWidth())
        self.outline.setSizePolicy(sizePolicy)
        self.outline.setMinimumSize(QtCore.QSize(350, 350))
        self.outline.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.outline.setFont(font)
        self.outline.setStyleSheet("QLabel{      \n"
"        background-color: rgb(179, 207, 0);\n"
"        color:white;\n"
"        borders:none;\n"
"        border-radius:200px;\n"
"}")
        self.outline.setText("")
        self.outline.setAlignment(QtCore.Qt.AlignCenter)
        self.outline.setObjectName("outline")
        self.loading_screen = QtWidgets.QLabel(self.Info_Screen)
        self.loading_screen.setGeometry(QtCore.QRect(10, 10, 381, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loading_screen.sizePolicy().hasHeightForWidth())
        self.loading_screen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.loading_screen.setFont(font)
        self.loading_screen.setStyleSheet("QLabel{      \n"
"        background-color:#e52a0d;\n"
"        color:white;\n"
"        borders:none;\n"
"        border-radius:190px;\n"
"}")
        self.loading_screen.setText("")
        self.loading_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_screen.setObjectName("loading_screen")
        self.statusScreen = QtWidgets.QLabel(self.Info_Screen)
        self.statusScreen.setGeometry(QtCore.QRect(90, 100, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Bodoni 72")
        font.setPointSize(20)
        self.statusScreen.setFont(font)
        self.statusScreen.setStyleSheet("QLabel {\n"
"    background-color:rgb(240, 244, 244);\n"
"    color:rgb(224, 46, 0);\n"
"    borders:none;\n"
"    border-radius:20px;\n"
"}")
        self.statusScreen.setAlignment(QtCore.Qt.AlignCenter)
        self.statusScreen.setObjectName("statusScreen")
        self.percentage = QtWidgets.QLabel(self.Info_Screen)
        self.percentage.setGeometry(QtCore.QRect(150, 220, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.percentage.setFont(font)
        self.percentage.setStyleSheet("QLabel{\n"
"    background-color:rgb(179, 207, 0);    \n"
"    color:rgb(224, 228, 228);\n"
"}")
        self.percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage.setObjectName("percentage")
        self.progressBar = QtWidgets.QProgressBar(self.Info_Screen)
        self.progressBar.setGeometry(QtCore.QRect(90, 310, 221, 10))
        self.progressBar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color:rgb(240, 244, 244);\n"
"    color:green;\n"
"    borders:none;\n"
"    border-radius:4px;\n"
"    \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color:rgb(182, 210, 0);\n"
"    borders:none;\n"
"    border-radius:4px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.Info_Screen, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.footer = QtWidgets.QFrame(self.body)
        self.footer.setMinimumSize(QtCore.QSize(400, 50))
        self.footer.setMaximumSize(QtCore.QSize(16777215, 40))
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(120)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.encrypt_btn = QtWidgets.QPushButton(self.footer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encrypt_btn.sizePolicy().hasHeightForWidth())
        self.encrypt_btn.setSizePolicy(sizePolicy)
        self.encrypt_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.encrypt_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.encrypt_btn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 206, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border:none;\n"
"    border-radius:12px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(58, 186, 255);\n"
"\n"
"}")
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.horizontalLayout_3.addWidget(self.encrypt_btn)
        self.decrypt_btn = QtWidgets.QPushButton(self.footer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decrypt_btn.sizePolicy().hasHeightForWidth())
        self.decrypt_btn.setSizePolicy(sizePolicy)
        self.decrypt_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.decrypt_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.decrypt_btn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 206, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border:none;\n"
"    border-radius:12px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(58, 186, 255);\n"
"\n"
"}")
        self.decrypt_btn.setObjectName("decrypt_btn")
        self.horizontalLayout_3.addWidget(self.decrypt_btn)
        self.gridLayout.addWidget(self.footer, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.body)
        self.verticalLayout.addWidget(self.Container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ExitWin.setText(_translate("MainWindow", "x"))
        self.MinimizeWin.setText(_translate("MainWindow", "-"))
        self.MaximizeWin.setText(_translate("MainWindow", "+"))
        self.File_Encryptor.setText(_translate("MainWindow", "Salsa Secure"))
        self.statusScreen.setText(_translate("MainWindow", "Ready"))
        self.percentage.setText(_translate("MainWindow", "0%"))
        self.encrypt_btn.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt_btn.setText(_translate("MainWindow", "Decrypt"))
