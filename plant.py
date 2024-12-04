import sqlite3
from PyQt6 import QtGui
import os
import speech_recognition
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import Qtdisainer
from Qtdisainer import plant, DialogFolder
from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QFontDialog
from PyQt6.QtWidgets import (
    QVBoxLayout, QListWidgetItem)
from PyQt6.QtGui import QIcon
import threading
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QFileDialog, QApplication, QDialog, QInputDialog, QWidget, QPushButton, QLabel, QMainWindow, \
    QColorDialog, QMessageBox

from PyQt6.QtCore import Qt


class PhotoConvert(QWidget):
    def __init__(self, sticker_path):
        super().__init__()
        self.file = sticker_path
        self.layout = QVBoxLayout()
        self.sticker_label = QLabel()
        pixmap = QPixmap(sticker_path).scaled(QSize(300, 300), Qt.AspectRatioMode.KeepAspectRatio)
        self.sticker_label.setPixmap(pixmap)
        self.sticker_label.setStyleSheet("border: 2px solid white")
        self.layout.addWidget(self.sticker_label)
        self.setLayout(self.layout)

    def text(self):
        return self.file


class EmailSend(Qtdisainer.Emailwindow, QDialog):
    def __init__(self, file_path):
        super().__init__()
        self.setupUi(self)
        self.file = file_path
        self.label_2.setText(self.file)
        self.pushButton.clicked.connect(self.send)
        self.flag = False
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

    def keyPressEvent(self, e):
        if e.key() == 16777220:
            self.close()

    def send(self):
        server_address = "smtp.yandex.ru"
        server_port = 587
        login = "foreveryproject@yandex.ru"
        password = "yrcpxihogvidmojj"

        try:
            text = MIMEMultipart()
            text["Subject"] = "Forevery"
            text["From"] = login
            emailto = self.lineEdit.text() + self.comboBox.currentText()
            text["To"] = emailto
            if os.path.isfile(self.file):
                with open(self.file, mode="r") as f:
                    f = f.readlines()
                for i in f:
                    i = i.rstrip()
                    if os.path.isfile(i):
                        with open(i, "rb") as f:
                            photo = MIMEBase('application', 'octet-stream')
                            photo.set_payload(f.read())
                            encoders.encode_base64(photo)
                            photo.add_header('Content-Disposition', f"attachment; filename={i}")
                            text.attach(photo)
                    else:
                        text.attach(MIMEText(f"{i}\n", 'plain'))

            with smtplib.SMTP(server_address, server_port) as server:
                server.starttls()
                server.login(login, password)
                server.send_message(text)
        except Exception as ex:
            self.flag = ex
        finally:
            self.accept()
            self.flag = "сообщение отправлено успешно"


class FolderFile(DialogFolder, QDialog):
    def __init__(self, id, x, y):
        super().__init__()
        self.id = id
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.move(x + 600, y + 300)
        self.foldershow()
        self.addfolder.clicked.connect(self.folder)
        self.whatfolder = None
        self.foldername = None
        self.addfile.clicked.connect(self.files)

    def folder(self):
        text, ok = QInputDialog.getText(self, "Добавление папки", "Имя папки:")
        if ok:
            if os.path.isdir(text):
                self.Dialog("Папка с таким именем уже существует", "Папка с таким именем уже существует",
                            QMessageBox.Icon.Warning, 40, 175, QMessageBox.StandardButton.Ok)
            elif text != "" and text != " ":
                self.Dialog("Папка успешно создана", f"Папка с именем {text} создана",
                            QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)

                with sqlite3.connect("Main/ForeveryData.db") as db:
                    cursor = db.cursor()
                    query = """INSERT INTO Folders (user_id, folder_name) VALUES (?, ?);"""
                    cursor.execute(query, (self.id, text))
                    db.commit()
                os.mkdir(text)
                self.foldershow()

    def files(self):
        if self.foldername is None or self.whatfolder is None:
            return
        text, ok = QInputDialog.getText(self, "Добавление записи", "Имя новой записи:")
        if ok:
            if os.path.isfile(f"{self.foldername}/{text}.txt"):
                self.Dialog("запись с таким именем уже существует", "Запись с таким именем уже существует",
                            QMessageBox.Icon.Warning, 40, 175, QMessageBox.StandardButton.Ok)
            elif text != "" and text != " ":
                self.Dialog("Запись успешно создана", f"Запись с именем {text} создана",
                            QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)

                with sqlite3.connect("Main/ForeveryData.db") as db:
                    cursor = db.cursor()
                    query = """INSERT INTO Files (folder_id, file_name, file_path) 
VALUES (?, ?, ?);"""
                    cursor.execute(query, (self.whatfolder, f"{text}", f"{self.foldername}/{text}.txt"))
                    db.commit()
                file = open(f"{self.foldername}/{text}.txt", mode="w")
                file.close()
                self.folderclick()

    def foldershow(self):
        data = []
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT folder_name FROM Folders WHERE user_id = ?;"""
            cursor.execute(query, (self.id,))
            for i in cursor:
                data.append(i)
            db.commit()
            scroll_content = QWidget()
            layout = QVBoxLayout(scroll_content)
            for i in data:
                if os.path.isdir(str(i[0])):
                    butt = QPushButton(i[0], self)
                    butt.resize(300, 20)
                    butt.clicked.connect(self.folderclick)
                    layout.addWidget(butt)
                else:
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """DELETE FROM Folders WHERE folder_name = ?;"""
                        cursor.execute(query, i)
                        db.commit()
            self.Area1.setWidget(scroll_content)

    def folderclick(self):
        data = []
        try:
            if self.sender().text() == "add file":
                a = 1 / 0
            self.foldername = self.sender().text()
        except:
            pass
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT folder_id FROM Folders WHERE folder_name = ?;"""
            cursor.execute(query, (self.foldername,))
            f_i = cursor.fetchone()
            self.whatfolder = f_i[0]
            db.commit()
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT file_name FROM Files WHERE folder_id = ?;"""
            cursor.execute(query, f_i)
            for i in cursor:
                data.append(i)
            db.commit()
            scroll_content = QWidget()
            layout = QVBoxLayout(scroll_content)
            for i in data:
                if os.path.isfile(f"{self.foldername}/{i[0]}.txt"):
                    butt = QPushButton(i[0], self)
                    butt.resize(300, 20)
                    butt.clicked.connect(self.plant)
                    layout.addWidget(butt)
                else:
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """DELETE FROM Files WHERE file_name = ?;"""
                        cursor.execute(query, i)
                        db.commit()
            self.Area2.setWidget(scroll_content)

    def plant(self):
        self.file_path = f"{self.foldername}/{self.sender().text()}.txt"
        self.accept()

    def give_file(self):
        return self.file_path

    def Dialog(self, Title, text, type, x, y, button):
        self.msg_box = QMessageBox()
        self.msg_box.move(self.x() + x, self.y() + y)
        self.msg_box.setStyleSheet("""QPushButton{
                                        background-color: rgb(85, 170, 255);
                                        color: rgb(255, 255, 255);
                                        }
                                        QMessageBox{
                                        color: rgb(0, 0, 0);
                                        background: rgb(255, 255, 255);
                                        border: 2px solid rgb(85, 170, 255);
                                        }""")
        self.msg_box.setWindowTitle(Title)
        self.msg_box.setText(text)
        self.msg_box.setIcon(type)
        self.msg_box.setStandardButtons(button)
        self.msg_box.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.msg_box.exec()


class Plantwindow(plant, QMainWindow):
    def __init__(self, file, id, x, y, parent):
        super().__init__()
        self.file = file
        self.perant = parent
        self.setupUi(self)
        self.setWindowIcon(QIcon("Photo/07d8350ba47011efb5653e02b2e4c1e1_1.jfif"))
        self.setIconSize(QSize(30, 30))
        self.setWindowTitle("FOREVERY")
        self.s = "йцукенгшщзхъфывапролджэячсмитьбюё1234567890.,qwertyuiopasdfghjklzxcvbnm"
        self.countlist = 0
        self.setWindowTitle("FOREVERY")
        self.updatefile = True
        self.flag_line = None
        self.id = id
        self.move(x, y)
        self.setFixedSize(1010, 700)
        self.horizontalSlider.valueChanged.connect(self.slider)
        self.Font_btn.clicked.connect(self.styleentry)
        self.deleta.clicked.connect(self.clear)
        self.label.setFont(QFont("Segoe Script", 10, QFont.Weight.Bold))
        self.Plant.itemDoubleClicked.connect(self.clearselection)
        self.remake.clicked.connect(self.remake_btn)
        self.photo.clicked.connect(self.addphoto)
        self.main_menu.clicked.connect(self.mainmenu)
        self.save.clicked.connect(self.savefile)
        self.label_2.setText(self.file)
        self.pushButton.clicked.connect(self.newfile)
        self.textEdit.setHidden(True)
        self.send_2.setHidden(True)
        self.delete_2.setHidden(True)
        self.Audio.move(1055, 200)
        self.Audiofalg = False
        self.textEdit.setReadOnly(True)
        self.Audio.clicked.connect(self.audioconect)
        self.delete_2.clicked.connect(lambda: self.textEdit.clear())
        self.delete_2.clicked.connect(self.newaudio)
        self.send_2.clicked.connect(self.addAudioforplant)
        self.email.clicked.connect(self.emailto)
        self.Audionew = False
        self.flagThread = None
        self.showfile(file)

    def emailto(self):
        self.sendem = EmailSend(self.file)
        self.sendem.exec()
        self.Dialog("", self.sendem.flag,
                    QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)

    def audioconect(self):
        if self.Audionew:
            return
        self.newaudio()

    def addAudioforplant(self):
        text = self.textEdit.toPlainText().split("\n")
        for i in text:
            self.Plant.addItem(i)
            self.countlist += 1
            item = self.Plant.item(self.countlist - 1)
            self.Plant.scrollToItem(item)
        self.updatefile = False
        self.textEdit.clear()
        self.textEdit.setReadOnly(True)
        self.newaudio()

    def audio(self):
        recognizer = speech_recognition.Recognizer()
        self.Audionew = True
        try:
            with speech_recognition.Microphone() as source:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="ru-RU")
                self.textEdit.append(text)
        except:
            self.Audionew = False
            self.Audiofalg = False
            self.textEdit.setHidden(True)
            self.send_2.setHidden(True)
            self.delete_2.setHidden(True)
            self.Audio.move(1055, 200)
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap("Photo/555-5554942_restart-icon-restart-png-clipart-no-bg-preview (carve.photos).png"),
                QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.Audio.setIcon(icon)
            self.Audio.setIconSize(QSize(300, 390))
            return

        self.Audionew = False
        self.Audiofalg = True
        self.textEdit.setReadOnly(False)
        self.send_2.setHidden(False)
        self.delete_2.setHidden(False)

    def Dialog(self, Title, text, type, x, y, button):
        self.msg_box = QMessageBox()
        self.msg_box.move(self.x() + x, self.y() + y)
        self.msg_box.setStyleSheet("""QPushButton{
                                        background-color: rgb(85, 170, 255);
                                        color: rgb(255, 255, 255);
                                        }
                                        QMessageBox{
                                        color: rgb(0, 0, 0);
                                        background: rgb(255, 255, 255);
                                        border: 2px solid rgb(85, 170, 255);
                                        }""")
        self.msg_box.setWindowTitle(Title)
        self.msg_box.setText(text)
        self.msg_box.setIcon(type)
        self.msg_box.setStandardButtons(button)
        self.msg_box.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.msg_box.exec()

    def newaudio(self):
        if self.Audiofalg:
            self.textEdit.clear()
            self.Audiofalg = False
            self.textEdit.setHidden(True)
            self.send_2.setHidden(True)
            self.delete_2.setHidden(True)
            self.Audio.move(1055, 200)
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap("Photo/1513505875_preview_icon-1968243_960_720-no-bg-preview (carve.photos).png"),
                QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.Audio.setIcon(icon)
            return
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photo/stream.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Audio.setIcon(icon)
        self.textEdit.setHidden(False)
        self.Audio.move(1055, 60)
        self.autoswap_thread2 = threading.Thread(target=self.audio, daemon=True)
        self.autoswap_thread2.start()

    def newfile(self, file):
        self.dialog = FolderFile(self.id, self.x(), self.y())
        self.dialog.exec()
        file_path = self.dialog.give_file()
        self.showfile(file_path)

    def showfile(self, file):
        self.file = file
        self.Plant.clear()
        self.label_2.setText(file)
        if os.path.isfile(file):
            with open(file, mode="r") as f:
                f = f.readlines()
            self.countlist = -1
            for i in f:
                self.countlist += 1
                i = i.rstrip()
                if os.path.isfile(i):
                    self.addphoto(i)
                else:
                    self.Plant.addItem(i)

    def savefile(self):
        if not os.path.isdir(self.file.split("/")[0]):
            os.mkdir(self.file.split("/")[0])
        with open(self.file, mode="w") as file:
            for x in range(self.Plant.count()):
                if os.path.isfile(self.Plant.item(x).text()[1::]):
                    file.write(f"{self.Plant.item(x).text()[1::]}\n")
                    continue
                file.write(f"{self.Plant.item(x).text()}\n")
            self.updatefile = True
            msg_box = QMessageBox()
            x, y = self.x(), self.y()
            msg_box.move(x + 800, y + 600)
            msg_box.setStyleSheet("""QPushButton{
            background-color: rgb(85, 170, 255);
            color: rgb(255, 255, 255);
            }
            QMessageBox{
            color: rgb(0, 0, 0);
            background: rgb(255, 255, 255);
            border: 2px solid rgb(85, 170, 255);
            }""")
            msg_box.setWindowTitle(f"Есть не сохраненный прогресс")
            msg_box.setText(f"Запись {self.file.split("/")[1:][0]} успешно сохранена ")
            msg_box.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
            msg_box.exec()

    def mainmenu(self):
        self.perant.move(self.x(), self.y())
        if self.updatefile:
            self.perant.show()
            self.close()
            return
        msg_box = QMessageBox()
        x, y = self.x(), self.y()
        msg_box.move(x + 300, y + 300)
        msg_box.setStyleSheet("""QPushButton{
background-color: rgb(85, 170, 255);
color: rgb(255, 255, 255);
}
QMessageBox{
color: rgb(0, 0, 0);
background: rgb(255, 255, 255);
border: 2px solid rgb(85, 170, 255);
}""")
        msg_box.setWindowTitle("Есть не сохраненный прогресс")
        msg_box.setText("У вас есть несохраненный прогресс. Хотите его сохранить?")
        msg_box.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Close)
        msg_box.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.savefile()
            self.perant.show()
            self.close()
            return
        elif result == QMessageBox.StandardButton.Close:
            return
        elif result == QMessageBox.StandardButton.Cancel:
            self.perant.show()
            self.close()
            return

    def send(self):
        msg = self.lineEdit.text()
        if len(msg) == 0:
            if self.flag_line is not None:
                self.flag_line = None
                return
            return
        if self.flag_line == "remake":
            self.lineEdit.setText("")
            self.flag_line = None
            self.current_item.setText(msg)
            return
        self.countlist += 1
        self.lineEdit.setText("")
        self.Plant.addItem(msg)
        item = self.Plant.item(self.countlist - 1)
        self.Plant.scrollToItem(item)
        self.updatefile = False

    def slider(self):
        range = self.horizontalSlider.value()
        self.setFixedSize(1010 + range * 4, 700)

    def keyPressEvent(self, e):
        if e.key() == 16777220:
            self.send()
        elif e.text() == "":
            return
        elif e.text() in self.s:
            s = self.lineEdit.text() + str(e.text())
            self.lineEdit.setText(s)
            self.lineEdit.setFocus()

    def styleentry(self):
        current_item = self.Plant.currentItem()
        if current_item is None:
            font, ok = QFontDialog.getFont()
            if ok:
                self.lineEdit.setFont(font)
                self.Plant.setFont(font)
                self.Font_btn.setFont(QFont(font.family(), 10, font.weight(), font.italic()))
                self.Font_btn.setText(font.family())
                self.label.setText(str(font.pointSize()))
                self.label.setFont(QFont(font.family(), 10))
                return
            return

        color = QColorDialog.getColor()
        if color.isValid():
            current_item.setForeground(color)

        font, ok = QFontDialog.getFont()
        if ok:
            current_item.setFont(font)

    def remake_btn(self, item):
        self.current_item = self.Plant.currentItem()
        if self.current_item is None:
            return
        if os.path.isfile(self.current_item.text()[1::]):
            current_row = self.Plant.currentRow()
            if self.replacephoto(current_row):
                self.clear()
                self.updatefile = False
                return
        self.lineEdit.setText(self.current_item.text())
        self.flag_line = "remake"
        self.updatefile = False

    def clear(self):
        if self.flag_line is not None:
            return
        current_item = self.Plant.currentItem()
        if current_item is None:
            self.Plant.clear()
            self.countlist = 0
            self.updatefile = False
            return
        current_row = self.Plant.currentRow()
        if current_row >= 0:
            item = self.Plant.takeItem(current_row)
            del item
            self.countlist -= 1
        self.updatefile = False

    def replacephoto(self, index):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                izo = PhotoConvert(file)
                list_item_widget = QListWidgetItem()
                list_item_widget.setSizeHint(izo.sizeHint())
                list_item_widget.setText(f" {izo.text()}")
                self.Plant.insertItem(index, list_item_widget)
                self.Plant.setItemWidget(list_item_widget, izo)
                self.countlist += 1
                item = self.Plant.item(self.countlist - 1)
                self.Plant.scrollToItem(item)
            self.updatefile = False
            return True

    def addphoto(self, file=None):
        if file:
            izo = PhotoConvert(file)
            list_item_widget = QListWidgetItem()
            list_item_widget.setSizeHint(izo.sizeHint())
            list_item_widget.setText(f" {izo.text()}")
            self.Plant.addItem(list_item_widget)
            self.Plant.setItemWidget(list_item_widget, izo)
            self.countlist += 1
            item = self.Plant.item(self.countlist - 1)
            self.Plant.scrollToItem(item)
            self.updatefile = False
            return

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                izo = PhotoConvert(file)
                list_item_widget = QListWidgetItem()
                list_item_widget.setSizeHint(izo.sizeHint())
                list_item_widget.setText(f" {izo.text()}")
                self.Plant.addItem(list_item_widget)
                self.Plant.setItemWidget(list_item_widget, izo)
                self.countlist += 1
                item = self.Plant.item(self.countlist - 1)
                self.Plant.scrollToItem(item)
        self.updatefile = False

    def clearselection(self, item):
        current_item = self.Plant.currentItem()
        if item == current_item:
            self.Plant.setCurrentItem(None)
