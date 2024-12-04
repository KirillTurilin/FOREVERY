import random
import Qtdisainer
import emailsend
from Qtdisainer import Profil
from PyQt6.QtGui import QIcon
import shutil
from PIL import Image, ImageDraw
import sqlite3
from PyQt6 import QtGui
import os
from PyQt6 import QtCore
from Qtdisainer import Captha
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QFileDialog, QDialog, QMainWindow, QMessageBox
from captcha.image import ImageCaptcha


class DiscontentWin(Qtdisainer.Discontent, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

    def keyPressEvent(self, e):
        if e.key() == 16777216:
            self.res = False
            self.close()

    def send(self):
        self.pushButton.setStyleSheet("""background: rgb(255, 255, 255);
        border: 3px solid rgb(85, 170, 255);""")
        text = self.textEdit.toPlainText()
        res = emailsend.sendsimple("foreveryproject@yandex.ru", text, "DISCONNTENT Forevery")
        if res:
            self.res = "Жалоба отправлена успешно"
        else:
            self.res = str(res)
        self.accept()


def createcaptha(text):
    image = ImageCaptcha(width=280, height=90)
    data = image.generate(text)
    image.write(text, f"Photo/captha.png")


class CapthaWin(Captha, QDialog):
    def __init__(self, x, y):
        super().__init__()
        self.setupUi(self)
        self.move(x, y)
        self.ok.clicked.connect(self.okey)
        self.cansel.clicked.connect(lambda: self.close())
        self.create()
        self.out = 0
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

    def create(self):
        words = ["Luna7", "Autum1", "Summer2", "Winter3", "Spring4", "Flower55", "Travel8", "WORlD", "Kitten", "Puppy",
                 "Hbhbe1", "Plane8", "little90"]
        self.word = random.choice(words)
        createcaptha(self.word)
        self.captha.setPixmap(QtGui.QPixmap("Photo/captha.png"))

    def okey(self):
        if self.word == self.lineEdit.text():
            self.accept()
            self.out = 1
        else:
            self.create()


def avatarka(image_path, output, size=(200, 200), corner_radius=20):
    img = Image.open(image_path)
    img = img.resize(size)
    rounded_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, img.size[0], img.size[1]), radius=corner_radius, fill=255)
    rounded_img.paste(img, (0, 0), mask)
    rounded_img.save(output)


def checklogin(login, login2):
    data = []
    with sqlite3.connect("Main/ForeveryData.db") as db:
        cursor = db.cursor()
        query = """SELECT * FROM Users"""
        cursor.execute(query)
        for i in cursor:
            data.append(i)
        db.commit()
    n = "1234567890"
    rus_alf = "йцукенгшщзхъфывапролджэячсмитьбюё"
    dopustim_log = "qwertyuiopasdfghjklzxcvbnm_-1234567890" + "qwertyuiopasdfghjklzxcvbnm".upper()
    try:
        if login == login2:
            raise ValueError("Логин должен отличатся от прошлого")
        for i in login:
            for j in data:
                if j[1] == login:
                    raise ValueError("Уже есть пользователь с таким же логином. Пожалуйста придумайте новый")
            if i == " ":
                raise ValueError("В логине не должно быть пробелов, попробуйте '_'")
            elif i in rus_alf:
                raise ValueError("В логине не должно быть Кириллицы")
            elif i not in dopustim_log:
                raise ValueError("Логин должен состоять только из букв англиского алфавита, цифр и символов -- '_-'")
        if len(login) <= 4:
            raise ValueError("Ваш логин слишком короткий. Пожалуйста придумайте новый")
        elif login[0] in n:
            raise ValueError("Логин должен начинаться на букву")
        return 1
    except ValueError as ve:
        return ve


def checkpassword(password, password2):
    data = []
    with sqlite3.connect("Main/ForeveryData.db") as db:
        cursor = db.cursor()
        query = """SELECT * FROM Users"""
        cursor.execute(query)
        for i in cursor:
            data.append(i)
        db.commit()
    n = "1234567890"
    rus_alf = "йцукенгшщзхъфывапролджэячсмитьбюё"
    dopustim_pas = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$&" + "qwertyuiopasdfghjklzxcvbnm".upper()
    # ____________________________________________________________________
    try:
        if password2 == password:
            raise ValueError("Пароль должен отличатся от прошлого")
        for i in password:
            if i == " ":
                raise ValueError("В пароле не должно быть пробелов, попробуйте '_'")
            elif i in rus_alf:
                raise ValueError("В пароле не должно быть Кириллицы")
            elif i not in dopustim_pas:
                raise ValueError("Пароль должен состоять только из букв англиского алфавита, цифр и символов -- '!#$&@")
        if len(password) < 8:
            raise ValueError("Пароль должен быть как минимум 8 символов")
        elif password[0] in n:
            raise ValueError("Пароль должен начинаться на букву")
        return 1
    except ValueError as ve:
        return ve


class Portfolio(Profil, QMainWindow):
    def __init__(self, id, x, y, perant):
        super().__init__()
        self.id = id
        self.perant = perant
        self.setupUi(self)
        self.move(x, y)
        self.setWindowTitle("FOREVERY")
        self.setWindowTitle("FOREVERY")
        self.setFixedSize(1010, 700)
        data = []
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT * FROM Users WHERE user_id = ?;"""
            cursor.execute(query, (self.id,))
            for i in cursor:
                data.append(i)
            db.commit()
        self.file_name_avatar, self.username, self.userpassword = data[0][-1], data[0][1], data[0][2]
        self.label_l.setText(self.username)
        self.label_p.setText(self.userpassword)
        self.exit.clicked.connect(lambda: self.close())
        self.setWindowIcon(QIcon("Photo/07d8350ba47011efb5653e02b2e4c1e1_1.jfif"))
        self.setIconSize(QSize(30, 30))
        self.Avatar.enterEvent = self.on_hover_enter
        self.Avatar.leaveEvent = self.on_hover_leave
        self.Avatar.setIconSize(QSize(600, 390))
        self.Avatar.setIcon(QIcon(self.file_name_avatar))
        self.setFixedSize(1010, 700)
        self.hide_2(True)
        self.hide_1(False)
        self.Avatar.clicked.connect(self.newavatar)
        self.rename_log.setHidden(True)
        self.rename_pas.setHidden(True)
        self.relogin = False
        self.repassword = False
        self.remake1.clicked.connect(self.remakelogin)
        self.remake2.clicked.connect(self.remakepassword)
        self.statistic()
        self.deleteaccount.clicked.connect(self.deleteacc)
        self.exit.clicked.connect(self.goto)
        self.exitto.clicked.connect(self.exito)
        self.baglook.clicked.connect(self.discontent)

    def exito(self):
        self.perant.logreg()
        self.close()

    def goto(self):
        self.perant.show()
        self.perant.move(self.x(), self.y())
        self.close()

    def remakelogin(self):
        if self.relogin:
            self.rename_log.setHidden(True)
            icon = QtGui.QIcon("Photo/pencil-icon-graphic-5uf2oteu1ocn8bum.png")
            icon.addPixmap(QtGui.QPixmap(),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.remake1.setIcon(icon)
            res = checklogin(self.rename_log.text(), self.username)
            self.relogin = False
            if res == 1:
                self.username = self.rename_log.text()
                with sqlite3.connect("Main/ForeveryData.db") as db:
                    cursor = db.cursor()
                    query = """UPDATE Users SET username = ? WHERE user_id = ?;"""
                    cursor.execute(query, (self.username, self.id))
                    db.commit()
                self.label_l.setText(self.username)
            else:
                self.dialog = self.Dialog("", f"{res}. Попробуйте снова", QMessageBox.Icon.Warning, 75, 150,
                                          QMessageBox.StandardButton.Ok)
        else:
            self.rename_log.setHidden(False)
            self.relogin = True
            icon = QtGui.QIcon("Photo/Echo_curation_alt.svg.png")
            icon.addPixmap(QtGui.QPixmap(),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.remake1.setIcon(icon)
            self.rename_log.setText(self.label_l.text())

    def remakepassword(self):
        if self.repassword:
            self.rename_pas.setHidden(True)
            icon = QtGui.QIcon("Photo/pencil-icon-graphic-5uf2oteu1ocn8bum.png")
            icon.addPixmap(QtGui.QPixmap(),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.remake2.setIcon(icon)
            res = checkpassword(self.rename_pas.text(), self.userpassword)
            self.repassword = False
            if res == 1:
                self.userpassword = self.rename_pas.text()
                with sqlite3.connect("Main/ForeveryData.db") as db:
                    cursor = db.cursor()
                    query = """UPDATE Users SET password = ? WHERE user_id = ?;"""
                    cursor.execute(query, (self.userpassword, self.id))
                    db.commit()
                self.label_p.setText(self.userpassword)
            else:
                self.dialog = self.Dialog("", f"{res}. Попробуйте снова", QMessageBox.Icon.Warning, 75, 150,
                                          QMessageBox.StandardButton.Ok)
        else:
            self.rename_pas.setHidden(False)
            self.repassword = True
            icon = QtGui.QIcon("Photo/Echo_curation_alt.svg.png")
            icon.addPixmap(QtGui.QPixmap(),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.remake2.setIcon(icon)
            self.rename_pas.setText(self.label_p.text())

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

    def discontent(self):
        self.dis = DiscontentWin()
        self.dis.exec()
        res = self.dis.res
        if res == False:
            return
        self.dialog = self.Dialog("", f"{res}", QMessageBox.Icon.Information, 75, 150,
                                  QMessageBox.StandardButton.Ok)

    def statistic(self):
        count_folder = 0
        count_file = 0
        data = []
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT folder_name, folder_id FROM Folders WHERE user_id = ?;"""
            cursor.execute(query, (self.id,))
            for i in cursor:
                data.append(i)
            db.commit()
            for i in data:
                if os.path.isdir(str(i[0])):
                    count_folder += 1
                    data2 = []
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor2 = db.cursor()
                        query = """SELECT file_name FROM Files WHERE folder_id = ?;"""
                        cursor2.execute(query, (i[1],))
                        for j in cursor2:
                            data2.append(j)
                        db.commit()
                        for j in data2:
                            if os.path.isfile(f"{i[0]}/{j[0]}.txt"):
                                count_file += 1
                            else:
                                with sqlite3.connect("Main/ForeveryData.db") as db:
                                    cursor = db.cursor()
                                    query = """DELETE FROM Files WHERE file_name = ?;"""
                                    cursor.execute(query, (j[0],))
                                    db.commit()
                else:
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """DELETE FROM Folders WHERE folder_id = ?;"""
                        cursor.execute(query, (i[1],))
                        db.commit()
        self.count_files.setText(str(count_file))
        self.count_folders.setText(str(count_folder))

    def deleteacc(self):
        captcha = CapthaWin(self.x() + 300, self.y() + 200)
        captcha.exec()
        if captcha.out == 1:
            self.dialog = self.Dialog("", f"Ваш Аккаунт удален будем ждать вас снова", QMessageBox.Icon.Critical,
                                      self.x() + 600, self.y() + 500,
                                      QMessageBox.StandardButton.Ok)
        else:
            self.dialog = self.Dialog("", f"Вы приняли правильное решение удаление отменино",
                                      QMessageBox.Icon.Information,
                                      self.x() + 600, self.y() + 500, QMessageBox.StandardButton.Ok)
            return
        data = []
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT folder_name, folder_id FROM Folders WHERE user_id = ?;"""
            cursor.execute(query, (self.id,))
            for i in cursor:
                data.append(i)
            db.commit()
            for i in data:
                data2 = []
                if os.path.isdir(str(i[0])):
                    shutil.rmtree(str(i[0]))
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor2 = db.cursor()
                        query = """SELECT file_name FROM Files WHERE folder_id = ?;"""
                        cursor2.execute(query, (i[1],))
                        for j in cursor2:
                            data2.append(j)
                        db.commit()
                        for j in data2:
                            with sqlite3.connect("Main/ForeveryData.db") as db:
                                cursor = db.cursor()
                                query = """DELETE FROM Files WHERE file_name = ?;"""
                                cursor.execute(query, (j[0],))
                                db.commit()
                with sqlite3.connect("Main/ForeveryData.db") as db:
                    cursor = db.cursor()
                    query = """DELETE FROM Folders WHERE folder_id = ?;"""
                    cursor.execute(query, (i[1],))
                    db.commit()
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """DELETE FROM Users WHERE user_id = ?;"""
            cursor.execute(query, (self.id,))
            db.commit()
        self.exito()

    def newavatar(self):
        try:
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

            if file_dialog.exec():
                selected_files = file_dialog.selectedFiles()
                self.file_name_avatar = f"{selected_files[0]}"
                avatarka(selected_files[0], self.file_name_avatar, size=(500, 500), corner_radius=260)
                icon = QtGui.QIcon(self.file_name_avatar)
                icon.addPixmap(QtGui.QPixmap(),
                               QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.Avatar.setIcon(icon)
                with sqlite3.connect("Main/ForeveryData.db") as db:
                    cursor = db.cursor()
                    query = """UPDATE Users SET avatar = ? WHERE user_id = ?;"""
                    cursor.execute(query, (self.file_name_avatar, self.id))
                    db.commit()
        except:
            with sqlite3.connect("Main/ForeveryData.db") as db:
                cursor = db.cursor()
                query = """SELECT * FROM Users WHERE user_id = ?;"""
                cursor.execute(query, (self.id,))
                avatar = cursor.fetchone()
                db.commit()
                self.file_name_avatar = avatar[-1]
                icon = QtGui.QIcon(self.file_name_avatar)
                icon.addPixmap(QtGui.QPixmap(),
                               QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.Avatar.setIcon(icon)
            self.Dialog("", f"Что то пошло не так. Попробуйте снова", QMessageBox.Icon.Warning, 530, 400,
                        QMessageBox.StandardButton.Ok)

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if delta < 0:
            self.Up()
        else:
            self.Down()

    def on_hover_enter(self, event):
        self.Avatar.setIconSize(QSize(600, 160))
        self.Avatar.setIcon(
            QIcon("Photo/678-6780577_instagram-camera-icon-png-image-free-d-no-bg-preview (carve.photos).png"))

    def on_hover_leave(self, event):
        self.Avatar.setIconSize(QSize(600, 390))
        self.Avatar.setIcon(QIcon(self.file_name_avatar))

    def Up(self):
        self.hide_2(False)
        self.hide_1(True)

    def Down(self):
        self.hide_2(True)
        self.hide_1(False)

    def hide_1(self, bool):
        self.Avatar.setHidden(bool)
        self.label_l.setHidden(bool)
        self.label_p.setHidden(bool)
        self.remake1.setHidden(bool)
        self.remake2.setHidden(bool)
        self.label.setHidden(bool)
        self.exit.setHidden(bool)

    def hide_2(self, bool):
        self.frame.setHidden(bool)
        self.label.setHidden(bool)
        self.label_2.setHidden(bool)
        self.count_folders.setHidden(bool)
        self.count_files.setHidden(bool)
        self.all_folder.setHidden(bool)
        self.all_files.setHidden(bool)
        self.baglook.setHidden(bool)
        self.Forevery.setHidden(bool)
        self.exitto.setHidden(bool)
        self.label_3.setHidden(bool)
        self.deleteaccount.setHidden(bool)