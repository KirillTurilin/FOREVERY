from PyQt6 import QtCore, QtGui, QtWidgets


class plant(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1410, 700)
        MainWindow.setWindowTitle("")
        MainWindow.setStyleSheet("background:rgb(85, 170, 255);\n"
                                 "border: 3px solid rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 0, 900, 700))
        self.frame.setStyleSheet(
            "background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0))")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Plant = QtWidgets.QListWidget(parent=self.frame)
        self.Plant.setGeometry(QtCore.QRect(0, 0, 900, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.Plant.setFont(font)
        self.Plant.setStyleSheet("background: rgb(255, 255, 255);\n"
                                 "color: rgb(0, 0, 0);")
        self.Plant.setObjectName("Plant")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 500, 900, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeVerCursor))
        self.lineEdit.setStyleSheet("background: rgb(143, 206, 255);\n"
                                    "color: rgb(0, 0, 0);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, 569, 900, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.frame_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(840, 0, 61, 131))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SplitHCursor))
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("background: rgb(143, 206, 255);")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.deleta = QtWidgets.QPushButton(parent=self.frame_2)
        self.deleta.setGeometry(QtCore.QRect(0, 30, 202, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.deleta.setFont(font)
        self.deleta.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.deleta.setStyleSheet("QPushButton{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background: rgb(255, 164, 164);\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.deleta.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photo/trash-circle-red-1024-no-bg-preview (carve.photos).png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.deleta.setIcon(icon)
        self.deleta.setIconSize(QtCore.QSize(207, 89))
        self.deleta.setObjectName("deleta")
        self.Font_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.Font_btn.setGeometry(QtCore.QRect(0, 0, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Font_btn.setFont(font)
        self.Font_btn.setObjectName("Font_btn")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(370, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setText("28")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setObjectName("label")
        self.photo = QtWidgets.QPushButton(parent=self.frame_2)
        self.photo.setGeometry(QtCore.QRect(200, 30, 202, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.photo.setFont(font)
        self.photo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.photo.setStyleSheet("QPushButton{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background:rgb(204, 204, 204);\n"
                                 "}\n"
                                 "")
        self.photo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Photo/Post-it_Notes-1024.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.photo.setIcon(icon1)
        self.photo.setIconSize(QtCore.QSize(91, 94))
        self.photo.setObjectName("photo")
        self.email = QtWidgets.QPushButton(parent=self.frame_2)
        self.email.setGeometry(QtCore.QRect(400, 30, 202, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.email.setStyleSheet("QPushButton{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background: rgb(19, 192, 255);\n"
                                 "}\n"
                                 "")
        self.email.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Photo/x-14-1024.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.email.setIcon(icon2)
        self.email.setIconSize(QtCore.QSize(91, 125))
        self.email.setObjectName("email")
        self.remake = QtWidgets.QPushButton(parent=self.frame_2)
        self.remake.setGeometry(QtCore.QRect(600, 30, 202, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.remake.setFont(font)
        self.remake.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.remake.setStyleSheet("QPushButton{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background: rgb(255, 255, 127);\n"
                                  "}\n"
                                  "")
        self.remake.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Photo/image_processing20210616-17152-12sxau.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.remake.setIcon(icon3)
        self.remake.setIconSize(QtCore.QSize(129, 86))
        self.remake.setObjectName("remake")
        self.save = QtWidgets.QPushButton(parent=self.frame_2)
        self.save.setGeometry(QtCore.QRect(800, 30, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save.setStyleSheet("background: rgb(0, 85, 0)\n"
                                "")
        self.save.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Photo/SAve.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.save.setIcon(icon4)
        self.save.setIconSize(QtCore.QSize(50, 50))
        self.save.setObjectName("save")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(410, 0, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(800, 70, 41, 61))
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Photo/Noto_Emoji_Oreo_1f4c2.svg.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(32, 40))
        self.pushButton.setObjectName("pushButton")
        self.main_menu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.main_menu.setGeometry(QtCore.QRect(0, -1, 113, 701))
        self.main_menu.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.main_menu.setStyleSheet("background: rgb(255, 255, 255);")
        self.main_menu.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Photo/i (6).webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.main_menu.setIcon(icon6)
        self.main_menu.setIconSize(QtCore.QSize(93, 200))
        self.main_menu.setObjectName("main_menu")
        self.Audio = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Audio.setGeometry(QtCore.QRect(1055, 60, 300, 300))
        self.Audio.setStyleSheet("background: rgb(255, 255, 255);\n"
                                 "border-radius:150;")
        self.Audio.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            "Photo/1513505875_preview_icon-1968243_960_720-no-bg-preview (carve.photos).png"),
            QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Audio.setIcon(icon7)
        self.Audio.setIconSize(QtCore.QSize(300, 390))
        self.Audio.setObjectName("Audio")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1015, 370, 390, 200))
        self.textEdit.setStyleSheet("background: rgb(143, 206, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "border: 3px solid rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.send_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.send_2.setGeometry(QtCore.QRect(1015, 575, 195, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.send_2.setFont(font)
        self.send_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.send_2.setStyleSheet("QPushButton{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "border: 3px solid rgb(155, 255, 140);\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background: rgb(155, 255, 140);\n"
                                  "border: 3px solid rgb(255, 255, 255);\n"
                                  "}\n"
                                  "")
        self.send_2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Photo/a5f1f4ec133859bb3c0faff8159174dd.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.send_2.setIcon(icon8)
        self.send_2.setIconSize(QtCore.QSize(202, 74))
        self.send_2.setObjectName("send_2")
        self.delete_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(1210, 575, 195, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.delete_2.setFont(font)
        self.delete_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_2.setStyleSheet("QPushButton{\n"
                                    "background: rgb(255, 255, 255);\n"
                                    "border: 3px solid rgb(255, 164, 164);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background: rgb(255, 164, 164);\n"
                                    "border: 3px solid rgb(255, 255, 255);\n"
                                    "}\n"
                                    "")
        self.delete_2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Photo/2079604.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_2.setIcon(icon9)
        self.delete_2.setIconSize(QtCore.QSize(91, 101))
        self.delete_2.setObjectName("delete_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Напиши что-нибудь)"))
        self.deleta.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
        self.Font_btn.setText(_translate("MainWindow", "Segoe Script"))
        self.photo.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.email.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.remake.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.save.setShortcut(_translate("MainWindow", "S, A, V, E"))
        self.label_2.setText(_translate("MainWindow", "data/home"))
        self.main_menu.setShortcut(_translate("MainWindow", "Esc"))
        self.send_2.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
        self.delete_2.setShortcut(_translate("MainWindow", "Ctrl+P"))


class WindowLog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setStyleSheet("background: rgb(255, 255, 255);\n"
                                 "border: 2px solid rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 400))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.South)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.lineeditPassword_N1_n1 = QtWidgets.QLineEdit(parent=self.tab1)
        self.lineeditPassword_N1_n1.setGeometry(QtCore.QRect(75, 225, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineeditPassword_N1_n1.setFont(font)
        self.lineeditPassword_N1_n1.setText("")
        self.lineeditPassword_N1_n1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineeditPassword_N1_n1.setObjectName("lineeditPassword_N1_n1")
        self.LineEditLogin_N1 = QtWidgets.QLineEdit(parent=self.tab1)
        self.LineEditLogin_N1.setEnabled(True)
        self.LineEditLogin_N1.setGeometry(QtCore.QRect(75, 170, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LineEditLogin_N1.setFont(font)
        self.LineEditLogin_N1.setText("")
        self.LineEditLogin_N1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.LineEditLogin_N1.setObjectName("LineEditLogin_N1")
        self.label_3 = QtWidgets.QLabel(parent=self.tab1)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 3px solid rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineeditPassword_N1_n2 = QtWidgets.QLineEdit(parent=self.tab1)
        self.lineeditPassword_N1_n2.setGeometry(QtCore.QRect(75, 275, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineeditPassword_N1_n2.setFont(font)
        self.lineeditPassword_N1_n2.setText("")
        self.lineeditPassword_N1_n2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineeditPassword_N1_n2.setObjectName("lineeditPassword_N1_n2")
        self.Sign = QtWidgets.QPushButton(parent=self.tab1)
        self.Sign.setGeometry(QtCore.QRect(50, 320, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Sign.setFont(font)
        self.Sign.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Sign.setStyleSheet("QPushButton{\n"
                                "background: rgb(255, 255, 255);\n"
                                "color: rgb(85, 170, 255);\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background: rgb(85, 170, 255);\n"
                                "color: rgb(255, 255, 255);\n"
                                "}\n"
                                "")
        self.Sign.setObjectName("Sign")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.lineeditPassword_N2 = QtWidgets.QLineEdit(parent=self.tab2)
        self.lineeditPassword_N2.setGeometry(QtCore.QRect(75, 225, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineeditPassword_N2.setFont(font)
        self.lineeditPassword_N2.setText("")
        self.lineeditPassword_N2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineeditPassword_N2.setObjectName("lineeditPassword_N2")
        self.LineEditLogin_N2 = QtWidgets.QLineEdit(parent=self.tab2)
        self.LineEditLogin_N2.setGeometry(QtCore.QRect(75, 170, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LineEditLogin_N2.setFont(font)
        self.LineEditLogin_N2.setText("")
        self.LineEditLogin_N2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.LineEditLogin_N2.setObjectName("LineEditLogin_N2")
        self.forgot = QtWidgets.QPushButton(parent=self.tab2)
        self.forgot.setGeometry(QtCore.QRect(100, 270, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.forgot.setFont(font)
        self.forgot.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.forgot.setStyleSheet("QPushButton{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "color: black;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background: rgb(85, 85, 255);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "")
        self.forgot.setObjectName("forgot")
        self.label_2 = QtWidgets.QLabel(parent=self.tab2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 3px solid rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(parent=self.tab2)
        self.login.setGeometry(QtCore.QRect(50, 300, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login.setStyleSheet("QPushButton{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "color: rgb(85, 170, 255);\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background: rgb(85, 170, 255);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "")
        self.login.setObjectName("login")
        self.tabWidget.addTab(self.tab2, "")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 0, 400, 400))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineeditPassword_N1_n1.setPlaceholderText(_translate("MainWindow", "You User Password"))
        self.LineEditLogin_N1.setPlaceholderText(_translate("MainWindow", "You User Name"))
        self.label_3.setText(_translate("MainWindow", "Thank you for choosing us.."))
        self.lineeditPassword_N1_n2.setPlaceholderText(_translate("MainWindow", "Repeat your password"))
        self.Sign.setText(_translate("MainWindow", "begin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Register"))
        self.lineeditPassword_N2.setPlaceholderText(_translate("MainWindow", "You User Password"))
        self.LineEditLogin_N2.setPlaceholderText(_translate("MainWindow", "You User Name"))
        self.forgot.setText(_translate("MainWindow", "Forgot password?"))
        self.label_2.setText(_translate("MainWindow", "Welcome to Forevery.."))
        self.login.setText(_translate("MainWindow", "go to"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Log in"))


class DataUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 375, 700, 10))
        self.progressBar.setStyleSheet("QProgressBar {border: 2px solid black;\n"
                                       " border-radius: 4px; \n"
                                       "background: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "QProgressBar::chunk {\n"
                                       "background: rgb(85, 170, 255);\n"
                                       "border-radius: 4px;}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 375))
        self.label.setStyleSheet("border: 3px solid rgb(85, 170, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Photo/aesthetic-pixel-art-background-0ax4fopcqzot21lj.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 385, 700, 65))
        self.label_2.setStyleSheet("background: rgb(255, 255, 255);\n"
                                   "border: 3px solid rgb(85, 170, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Photo/LsFa65aRXJI.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class DialogFolder(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet("QPushButton{\n"
                             "background-color: rgb(85, 170, 255);\n"
                             "color: rgb(255, 255, 255);\n"
                             "}\n"
                             "QDialog{\n"
                             "color: rgb(0, 0, 0);\n"
                             "background: rgb(255, 255, 255);\n"
                             "border: 2px solid rgb(85, 170, 255);\n"
                             "}")
        self.Area1 = QtWidgets.QScrollArea(parent=Dialog)
        self.Area1.setGeometry(QtCore.QRect(0, 50, 300, 350))
        self.Area1.setStyleSheet("QWidget{\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "border: 2px solid rgb(85, 170, 255);\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "background-color: rgb(3, 201, 255);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border: 2px solid rgb(0, 0, 0);\n"
                                 "font-family: Fixedsys;\n"
                                 "}")
        self.Area1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Area1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Area1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Area1.setWidgetResizable(True)
        self.Area1.setObjectName("Area1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 296, 346))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Area1.setWidget(self.scrollAreaWidgetContents)
        self.Area2 = QtWidgets.QScrollArea(parent=Dialog)
        self.Area2.setGeometry(QtCore.QRect(300, 50, 300, 350))
        self.Area2.setStyleSheet("QWidget{\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "border: 2px solid rgb(85, 170, 255);\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border: 2px solid rgb(0, 0, 0);\n"
                                 "font-family: Fixedsys;\n"
                                 "}")
        self.Area2.setWidgetResizable(True)
        self.Area2.setObjectName("Area2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 296, 346))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.Area2.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.addfolder = QtWidgets.QPushButton(parent=Dialog)
        self.addfolder.setGeometry(QtCore.QRect(0, 20, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.addfolder.setFont(font)
        self.addfolder.setStyleSheet("background: rgb(85, 170, 255);")
        self.addfolder.setObjectName("addfolder")
        self.addfile = QtWidgets.QPushButton(parent=Dialog)
        self.addfile.setGeometry(QtCore.QRect(300, 20, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.addfile.setFont(font)
        self.addfile.setStyleSheet("background: rgb(85, 170, 255);")
        self.addfile.setObjectName("addfile")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Folders"))
        self.label_2.setText(_translate("Dialog", "Files"))
        self.addfolder.setText(_translate("Dialog", "add folder"))
        self.addfile.setText(_translate("Dialog", "add file"))


class Profil(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 700)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet("background: rgb(255, 255, 255);\n"
                                 "border: 3px solid rgb(85, 170, 255);")
        MainWindow.setIconSize(QtCore.QSize(0, 631))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_l = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_l.setGeometry(QtCore.QRect(130, 300, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setBold(False)
        font.setWeight(50)
        self.label_l.setFont(font)
        self.label_l.setStyleSheet("background: rgb(85, 170, 255);")
        self.label_l.setObjectName("label_l")
        self.label_p = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_p.setGeometry(QtCore.QRect(130, 380, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setBold(False)
        font.setWeight(50)
        self.label_p.setFont(font)
        self.label_p.setStyleSheet("background: rgb(85, 170, 255);")
        self.label_p.setObjectName("label_p")
        self.remake1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.remake1.setGeometry(QtCore.QRect(70, 300, 51, 51))
        self.remake1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photo/pencil-icon-graphic-5uf2oteu1ocn8bum.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.remake1.setIcon(icon)
        self.remake1.setIconSize(QtCore.QSize(49, 41))
        self.remake1.setObjectName("remake1")
        self.remake2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.remake2.setGeometry(QtCore.QRect(70, 380, 51, 51))
        self.remake2.setText("")
        self.remake2.setIcon(icon)
        self.remake2.setIconSize(QtCore.QSize(49, 41))
        self.remake2.setObjectName("remake2")
        self.exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(0, 590, 1011, 111))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.exit.setStyleSheet("background: rgb(143, 206, 255);\n"
                                "border: 4px solid rgb(85, 170, 255);")
        self.exit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Photo/i (6).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit.setIcon(icon1)
        self.exit.setIconSize(QtCore.QSize(170, 134))
        self.exit.setObjectName("exit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 220, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.rename_log = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.rename_log.setGeometry(QtCore.QRect(130, 300, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rename_log.setFont(font)
        self.rename_log.setObjectName("rename_log")
        self.rename_pas = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.rename_pas.setGeometry(QtCore.QRect(130, 380, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rename_pas.setFont(font)
        self.rename_pas.setObjectName("rename_pas")
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Avatar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Avatar.setGeometry(QtCore.QRect(530, 120, 400, 400))
        self.Avatar.setStyleSheet("border-radius: 200;\n"
                                  "background: rgb(255, 255, 255);")
        self.Avatar.setText("")
        self.Avatar.setIconSize(QtCore.QSize(252, 448))
        self.Avatar.setObjectName("Avatar")

        # Up__________________________________________________________
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 700)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet("background: rgb(255, 255, 255);\n"
                                 "border: 3px solid rgb(85, 170, 255);")
        MainWindow.setIconSize(QtCore.QSize(0, 631))
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 570, 1010, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.deleteaccount = QtWidgets.QPushButton(parent=self.frame)
        self.deleteaccount.setGeometry(QtCore.QRect(535, 25, 400, 81))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteaccount.setFont(font)
        self.deleteaccount.setStyleSheet("QPushButton{\n"
                                         "background: rgb(255, 255, 255);\n"
                                         "border: 3px solid rgb(85, 170, 255);\n"
                                         "border-radius: 35;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background: rgb(255, 30, 0);\n"
                                         "border: 3px solid rgb(255, 255, 255);\n"
                                         "border-radius: 35;\n"
                                         "}")
        self.deleteaccount.setObjectName("deleteaccount")
        self.exitto = QtWidgets.QPushButton(parent=self.frame)
        self.exitto.setGeometry(QtCore.QRect(75, 25, 400, 81))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitto.setFont(font)
        self.exitto.setStyleSheet("QPushButton{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "border: 3px solid rgb(85, 170, 255);\n"
                                  "border-radius: 35;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background: rgb(255, 30, 0);\n"
                                  "border: 3px solid rgb(255, 255, 255);\n"
                                  "border-radius: 35;\n"
                                  "}")
        self.exitto.setObjectName("exitto")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 250, 1010, 61))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1010, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Photo/LsFa65aRXJI.jpg"))
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.all_folder = QtWidgets.QLabel(parent=self.centralwidget)
        self.all_folder.setGeometry(QtCore.QRect(0, 310, 601, 91))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.all_folder.setFont(font)
        self.all_folder.setObjectName("all_folder")
        self.all_files = QtWidgets.QLabel(parent=self.centralwidget)
        self.all_files.setGeometry(QtCore.QRect(0, 400, 601, 91))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.all_files.setFont(font)
        self.all_files.setObjectName("all_files")
        self.Forevery = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Forevery.setGeometry(QtCore.QRect(0, 490, 1010, 81))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Forevery.setFont(font)
        self.Forevery.setStyleSheet("background: rgb(85, 170, 255);\n"
                                    "border: 3px solid rgb(85, 170, 255);")
        self.Forevery.setObjectName("Forevery")
        self.count_folders = QtWidgets.QLabel(parent=self.centralwidget)
        self.count_folders.setGeometry(QtCore.QRect(600, 310, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.count_folders.setFont(font)
        self.count_folders.setText("")
        self.count_folders.setObjectName("count_folders")
        self.count_files = QtWidgets.QLabel(parent=self.centralwidget)
        self.count_files.setGeometry(QtCore.QRect(600, 400, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.count_files.setFont(font)
        self.count_files.setText("")
        self.count_files.setObjectName("count_files")
        self.baglook = QtWidgets.QPushButton(parent=self.centralwidget)
        self.baglook.setGeometry(QtCore.QRect(730, 310, 280, 181))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.baglook.setFont(font)
        self.baglook.setStyleSheet("background: rgb(85, 170, 255);\n"
                                   "border: 3px solid rgb(255, 255, 255);")
        self.baglook.setObjectName("baglook")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_l.setText(_translate("MainWindow", "LOGIN"))
        self.label_p.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "      Your User Name and Password"))
        self.deleteaccount.setText(_translate("MainWindow", "Delete account"))
        self.exitto.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Statistics"))
        self.all_folder.setText(_translate("MainWindow", "Folders"))
        self.all_files.setText(_translate("MainWindow", "Files"))
        self.Forevery.setText(_translate("MainWindow", "FOREVERY"))
        self.baglook.setText(_translate("MainWindow", "look bag?"))


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1010, 101))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 1010, 101))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "background: rgb(255, 255, 255);\n"
                                        "border: 3px solid rgb(85, 170, 255);\n"
                                        "}\n""")
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photo/name_icon (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(90, 104))
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 100, 721, 601))
        self.frame_2.setStyleSheet("background:rgb(255, 255, 255);\n"
                                   "border: 3px solid rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBoxfile = QtWidgets.QComboBox(parent=self.frame_2)
        self.comboBoxfile.setGeometry(QtCore.QRect(360, 0, 361, 41))
        font = QtGui.QFont()
        font.setFamily("terminal")
        self.comboBoxfile.setFont(font)
        self.comboBoxfile.setStyleSheet("QComboBox::down-arrow { \n"
                                        "padding-right: 5px;}\n"
                                        "QComboBox QAbstractItemView::item {\n"
                                        " border: none; \n"
                                        "padding-left: 5px;\n"
                                        " }\n"
                                        "QComboBox QAbstractItemView::item:selected { \n"
                                        "background: rgb(47, 175, 178); \n"
                                        "padding-left: 5px; \n"
                                        "}\n"
                                        "QComboBox{\n"
                                        "background: rgb(255, 255, 255);\n"
                                        "border: 3px solid rgb(85, 170, 255);\n"
                                        "font-family: terminal;\n"
                                        "}")
        self.comboBoxfile.setEditable(False)
        self.comboBoxfile.setCurrentText("")
        self.comboBoxfile.setDuplicatesEnabled(False)
        self.comboBoxfile.setObjectName("comboBoxfile")
        self.comboBoxFolder = QtWidgets.QComboBox(parent=self.frame_2)
        self.comboBoxFolder.setGeometry(QtCore.QRect(0, 0, 361, 41))
        font = QtGui.QFont()
        font.setFamily("terminal")
        self.comboBoxFolder.setFont(font)
        self.comboBoxFolder.setStyleSheet("QComboBox::down-arrow { \n"
                                          "padding-right: 5px;}\n"
                                          "QComboBox QAbstractItemView::item {\n"
                                          " border: none; \n"
                                          "padding-left: 5px;\n"
                                          " }\n"
                                          "QComboBox QAbstractItemView::item:selected { \n"
                                          "background: rgb(47, 175, 178); \n"
                                          "padding-left: 5px; \n"
                                          "}\n"
                                          "QComboBox{\n"
                                          "background: rgb(255, 255, 255);\n"
                                          "border: 3px solid rgb(85, 170, 255);\n"
                                          "font-family: terminal;\n"
                                          "}")
        self.comboBoxFolder.setEditable(True)
        self.comboBoxFolder.setCurrentText("")
        self.comboBoxFolder.setDuplicatesEnabled(False)
        self.comboBoxFolder.setObjectName("comboBoxFolder")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 721, 561))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Photo/869a61947e07fd6e9d185796baf14174.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(720, 100, 291, 601))
        self.frame_3.setStyleSheet("background: rgb(85, 170, 255);\n"
                                   "border: 3px solid white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.dele = QtWidgets.QPushButton(parent=self.frame_3)
        self.dele.setGeometry(QtCore.QRect(50, 510, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.dele.setFont(font)
        self.dele.setStyleSheet("QPushButton{\n"
                                "border: 3px solid  rgb(191, 0, 0);\n"
                                "color: black;\n"
                                "background:rgb(255, 255, 255);\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "border: 3px solid rgb(255, 255, 255);\n"
                                "background: rgb(191, 0, 0);\n"
                                "color: white;\n"
                                "}\n"
                                "")
        self.dele.setObjectName("dele")
        self.rename = QtWidgets.QPushButton(parent=self.frame_3)
        self.rename.setGeometry(QtCore.QRect(50, 440, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.rename.setFont(font)
        self.rename.setStyleSheet("QPushButton{\n"
                                  "border: 3px solid  rgb(85, 85, 255);\n"
                                  "color: black;\n"
                                  "background:rgb(255, 255, 255);\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "border: 3px solid rgb(255, 255, 255);\n"
                                  "color: white;\n"
                                  "background: rgb(85, 85, 255);\n"
                                  "}\n"
                                  "")
        self.rename.setObjectName("rename")
        self.open = QtWidgets.QPushButton(parent=self.frame_3)
        self.open.setGeometry(QtCore.QRect(50, 370, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.open.setFont(font)
        self.open.setStyleSheet("QPushButton{\n"
                                "background: rgb(255, 255, 255);\n"
                                "border: 3px solid rgb(85, 170, 0);\n"
                                "color: black\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "border: 3px solid rgb(255, 255, 255);\n"
                                "background: rgb(85, 170, 0);\n"
                                "color: white;\n"
                                "}\n"
                                "")
        self.open.setObjectName("open")
        self.folder = QtWidgets.QPushButton(parent=self.frame_3)
        self.folder.setGeometry(QtCore.QRect(50, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.folder.setFont(font)
        self.folder.setStyleSheet("QPushButton{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "border: 3px solid rgb(0, 0, 0);\n"
                                  "color: black\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "border: 3px solid rgb(255, 255, 255);\n"
                                  "background: rgb(85, 170, 255);\n"
                                  "color: white;\n"
                                  "}\n"
                                  "")
        self.folder.setObjectName("folder")
        self.file = QtWidgets.QPushButton(parent=self.frame_3)
        self.file.setGeometry(QtCore.QRect(50, 100, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.file.setFont(font)
        self.file.setStyleSheet("QPushButton{\n"
                                "background: rgb(255, 255, 255);\n"
                                "border: 3px solid rgb(0, 0, 0);\n"
                                "color: black\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "border: 3px solid rgb(255, 255, 255);\n"
                                "background: rgb(85, 170, 255);\n"
                                "color: white;\n"
                                "}\n"
                                "")
        self.file.setObjectName("file")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(50, 310, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dele.setText(_translate("MainWindow", "delete"))
        self.rename.setText(_translate("MainWindow", "rename"))
        self.open.setText(_translate("MainWindow", "open"))
        self.folder.setText(_translate("MainWindow", "add folder"))
        self.file.setText(_translate("MainWindow", "add file"))


class Captha(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog{\n"
                             "color: rgb(0, 0, 0);\n"
                             "background: rgb(255, 255, 255);\n"
                             "border: 3px solid rgb(85, 170, 255);\n"
                             "}\n"
                             "")
        self.captha = QtWidgets.QLabel(parent=Dialog)
        self.captha.setGeometry(QtCore.QRect(0, 0, 500, 150))
        self.captha.setStyleSheet("border: 3px solid rgb(85, 170, 255);")
        self.captha.setText("")
        self.captha.setScaledContents(True)
        self.captha.setObjectName("captha")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(0, 150, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 3px solid rgb(85, 170, 255);\n"
                                    "background: rgb(85, 170, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(4, 205, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ok = QtWidgets.QPushButton(parent=Dialog)
        self.ok.setGeometry(QtCore.QRect(33, 260, 200, 28))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.ok.setFont(font)
        self.ok.setStyleSheet("border: 3px solid rgb(85, 170, 255);\n"
                              "background: rgb(85, 170, 255);")
        self.ok.setObjectName("ok")
        self.cansel = QtWidgets.QPushButton(parent=Dialog)
        self.cansel.setGeometry(QtCore.QRect(267, 260, 200, 28))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.cansel.setFont(font)
        self.cansel.setStyleSheet("border: 3px solid rgb(85, 170, 255);\n"
                                  "background: rgb(85, 170, 255);")
        self.cansel.setObjectName("cansel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Please enter the captcha to confirm"))
        self.ok.setText(_translate("Dialog", "I agree"))
        self.cansel.setText(_translate("Dialog", "Cansel"))


class Discontent(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(971, 604)
        Dialog.setStyleSheet("background:rgb(85, 170, 255);\n"
                             "border: 3px solid white;")
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 70, 971, 461))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: white;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 971, 71))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgb(255, 255, 255);\n"
                                 "border: 3px solid rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 530, 971, 71))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background: rgb(255, 255, 255);\n"
                                      "border: 3px solid rgb(85, 170, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background: rgb(85, 170, 255);\n"
                                      "border: 3px solid rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "print your DISCONTENT"))
        self.pushButton.setText(_translate("Dialog", "send"))


class Emailwindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(735, 297)
        Dialog.setStyleSheet("background: rgb(85, 170, 255);\n"
                             "border: 3px solid rgb(255, 255, 255);")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 140, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(430, 140, 171, 41))
        font = QtGui.QFont()
        font.setFamily("terminal")
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeVerCursor))
        self.comboBox.setStyleSheet("QComboBox::down-arrow { \n"
                                    "padding-right: 5px;}\n"
                                    "QComboBox QAbstractItemView::item {\n"
                                    " border: none; \n"
                                    "padding-left: 5px;\n"
                                    " }\n"
                                    "QComboBox QAbstractItemView::item:selected { \n"
                                    "background: rgb(47, 175, 178); \n"
                                    "padding-left: 5px; \n"
                                    "}\n"
                                    "QComboBox{\n"
                                    "background: rgb(255, 255, 255);\n"
                                    "font-family: terminal;\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 535, 28))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background: rgb(85, 170, 255);\n"
                                      "border: 0px\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("baclground: rgb(85, 170, 255);\n"
                                   "border: 0px")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Your mailing address                  "))
        self.comboBox.setCurrentText(_translate("Dialog", "@yandex.ru"))
        self.comboBox.setItemText(0, _translate("Dialog", "@gmail.com"))
        self.comboBox.setItemText(1, _translate("Dialog", "@rambler.ru"))
        self.comboBox.setItemText(2, _translate("Dialog", "@yandex.ru"))
        self.comboBox.setItemText(3, _translate("Dialog", "@internet.ru"))
        self.comboBox.setItemText(4, _translate("Dialog", "@list.ru"))
        self.comboBox.setItemText(5, _translate("Dialog", "@bk.ru"))
        self.comboBox.setItemText(6, _translate("Dialog", "@mail.ru"))
        self.comboBox.setItemText(7, _translate("Dialog", "@inbox.ru"))
        self.label.setText(_translate("Dialog", "please enter your email"))
        self.pushButton.setText(_translate("Dialog", "send"))
        self.label_2.setText(_translate("Dialog", "file: "))
