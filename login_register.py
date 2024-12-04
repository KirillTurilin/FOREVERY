from random import random
from PyQt6.QtGui import QIcon
from Qtdisainer import WindowLog
import random
import sqlite3
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox


def adddatabase(login, password, avatar):
    with sqlite3.connect("Main/ForeveryData.db") as db:
        cursor = db.cursor()
        query = """INSERT INTO Users (username, password, avatar) VALUES (?, ?, ?);"""
        cursor.execute(query, (login, password, avatar))
        db.commit()


def randomizo():
    return random.choice(["Photo/Avatarbase2.png", "Photo/Avatarbase3.png"])


def registor(login, password, password2):
    data = []
    global id
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
    dopustim_pas = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$&" + "qwertyuiopasdfghjklzxcvbnm".upper()
    try:
        if password2 != password:
            raise ValueError("Пароли не совпадают")
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
        adddatabase(login, password, randomizo())
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT user_id FROM Users WHERE username = ?;"""
            cursor.execute(query, (login,))
            id = cursor.fetchone()[0]
            db.commit()
        return "Вы успешно зарегестрированны"
    except ValueError as ve:
        return ve


def log(login, password):
    data = []
    global id
    with sqlite3.connect("Main/ForeveryData.db") as db:
        cursor = db.cursor()
        query = """SELECT * FROM Users"""
        cursor.execute(query)
        for i in cursor:
            data.append(i)
        db.commit()
    try:
        for i in data:
            if i[1] == login:
                break
        else:
            raise ValueError("Не найден пользователь с таким логином")
        if i[2] == password:
            pass
        else:
            raise ValueError("Не верный пароль")
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT user_id FROM Users WHERE username = ?;"""
            cursor.execute(query, (login,))
            id = cursor.fetchone()[0]
            db.commit()

        return "Вы успешно авторизовались"

    except ValueError as ve:
        return ve


class Loginwindow(WindowLog, QMainWindow):
    def __init__(self, perant):
        super().__init__()
        self.perant = perant
        photo = ["Photo/3d209063735a57501cc337553cddbd35.jpg", "Photo/dd33eb45786d11ee8e447a2f0d1382ba_upscaled.jfif",
                 "Photo/pngtree-blue-and-white-gradient-wave-stripe-curve-png-image_377074.jpg",
                 "Photo/drawing-illustration-abstract-blue-cloud-flower-plant-petal-sketch-land-plant-flowering-plant-watercolor-paint-291828.jpg"]
        self.setupUi(self)
        self.setWindowIcon(QIcon("Photo/07d8350ba47011efb5653e02b2e4c1e1_1.jfif"))
        self.setIconSize(QSize(30, 30))
        self.setWindowTitle("Forevery")
        self.setFixedSize(800, 400)
        self.pixmap = QPixmap(random.choice(photo))
        self.label.setPixmap(self.pixmap)
        self.login.clicked.connect(self.loginin)
        self.forgot.setHidden(True)
        self.Sign.clicked.connect(self.regin)
        self.forgot.clicked.connect(self.forgotpassword)

    def loginin(self):
        login = self.LineEditLogin_N2.text()
        password = self.lineeditPassword_N2.text()
        lbl = log(login, password)
        if str(lbl) == "Вы успешно авторизовались":
            self.Dialog("Авторизация прошла успешно", str(lbl), QMessageBox.Icon.Information, 40, 175,
                        QMessageBox.StandardButton.Ok)
            self.perant.move(self.x() - 40, self.y() - 40)
            self.perant.id = id
            self.perant.foldershow()
            self.perant.show()
            self.close()
        elif str(lbl) == "Не верный пароль":
            self.forgot.setHidden(False)
            self.Dialog("Забыли пароль?", str(lbl), QMessageBox.Icon.Question, 40, 175, QMessageBox.StandardButton.Ok)
        else:
            self.Dialog("Ошибка Авторизации", str(lbl), QMessageBox.Icon.Critical, 40, 175,
                        QMessageBox.StandardButton.Ok)

    def regin(self):
        login = self.LineEditLogin_N1.text()
        password1 = self.lineeditPassword_N1_n1.text()
        password2 = self.lineeditPassword_N1_n2.text()
        lbl = registor(login, password1, password2)
        if lbl == "Вы успешно зарегестрированны":
            self.Dialog("Регистрация прошла успешно", str(lbl), QMessageBox.Icon.Information, 40, 175,
                        QMessageBox.StandardButton.Ok)
            self.perant.move(self.x() - 40, self.y() - 40)
            self.perant.id = id
            self.perant.foldershow()
            self.perant.show()
            self.close()
        else:
            self.Dialog("Ошибка регистрации", str(lbl), QMessageBox.Icon.Critical, 40, 175,
                        QMessageBox.StandardButton.Ok)

    def forgotpassword(self):
        if self.LineEditLogin_N2.text() != "" or log(self.LineEditLogin_N2.text(),
                                                     self.lineeditPassword_N2.text()) == "Не верный пароль":
            self.Dialog("Ты забыл пароль?",
                        f"К сожеления Forevery ничем тебе помочь не может ведь проверить что {self.LineEditLogin_N2.text()} это а никой нибудь Кирилл Турилин",
                        QMessageBox.Icon.Warning, 40, 175,
                        QMessageBox.StandardButton.Ok)

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
