import sqlite3
import os
import shutil
import portfolio
from Qtdisainer import MainWindow
from plant import Plantwindow
from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from login_register import Loginwindow
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QInputDialog, QMainWindow, QMessageBox


class MainWin(MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.id = None
        self.setupUi(self)
        self.setfolder = set()
        self.setWindowIcon(QIcon("Photo/07d8350ba47011efb5653e02b2e4c1e1_1.jfif"))
        self.setIconSize(QSize(30, 30))
        self.setWindowTitle("FOREVERY")
        self.setfile = set()
        self.setFixedSize(1010, 700)
        self.folder.clicked.connect(self.folderadd)
        self.setStyleSheet("""background: rgb(255, 255, 255);
border: 3px solid rgb(85, 170, 255);
font-family: terminal;""")
        self.foldername = None
        self.whatfolder = None
        self.current = None
        self.comboBoxFolder.activated.connect(self.folderclick)
        self.comboBoxfile.activated.connect(self.filelick)
        self.file.clicked.connect(self.fileadd)
        self.comboBoxfile.setEditable(False)
        self.comboBoxFolder.setEditable(False)
        self.comboBoxFolder.setPlaceholderText("Folders")
        self.comboBoxfile.setPlaceholderText("Files")
        self.open.clicked.connect(self.plantopen)
        self.rename.clicked.connect(self.renameobj)
        self.dele.clicked.connect(self.delete)
        self.pushButton_6.clicked.connect(self.gotoprofil)
        self.foldershow()

    def folderadd(self):
        text, ok = QInputDialog.getText(self, "add folder", "folder name:")
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

    def fileadd(self):
        if self.foldername is None or self.whatfolder is None:
            return
        text, ok = QInputDialog.getText(self, "add file", "file name:")
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
                self.comboBoxfile.setCurrentText(text)
                self.folderclick()

    def foldershow(self):
        data = []
        self.label.setText("")
        self.comboBoxFolder.clear()
        self.comboBoxFolder.setPlaceholderText("Folders")
        self.current = None
        with sqlite3.connect("Main/ForeveryData.db") as db:
            cursor = db.cursor()
            query = """SELECT folder_name FROM Folders WHERE user_id = ?;"""
            cursor.execute(query, (self.id,))
            for i in cursor:
                data.append(i)
            db.commit()
            for i in data:
                if os.path.isdir(str(i[0])):
                    if str(i[0]) not in self.setfolder:
                        self.comboBoxFolder.addItem(str(i[0]))
                        self.setfolder.add(str(i[0]))
                else:
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """DELETE FROM Folders WHERE folder_name = ?;"""
                        cursor.execute(query, i)
                        db.commit()
        self.setfolder = set()

    def folderclick(self):
        self.label.setText(f"folder:{self.comboBoxFolder.currentText()}")
        data = []
        self.current = (self.comboBoxFolder.currentText(), 1)
        self.foldername = self.comboBoxFolder.currentText()
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
            self.comboBoxfile.clear()
            self.setfile = set()
            for i in data:
                if os.path.isfile(f"{self.foldername}/{i[0]}.txt"):
                    if str(i[0]) not in self.setfile:
                        self.comboBoxfile.addItem(str(i[0]))
                        self.setfile.add(str(i[0]))
                else:
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """DELETE FROM Files WHERE file_name = ?;"""
                        cursor.execute(query, i)
                        db.commit()

    def logreg(self):
        self.win = Loginwindow(self)
        self.win.show()

    def filelick(self):
        self.current = (self.comboBoxfile.currentText(), 2)
        self.label.setText(f"file:{self.comboBoxfile.currentText()}")

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

    def plantopen(self):
        if self.current is None or self.current[1] == 1:
            return
        self.plant = Plantwindow(f"{self.foldername}/{self.current[0]}.txt", self.id, self.x(), self.y(), self)
        self.plant.show()
        self.close()

    def delete(self):
        if self.current is None:
            return
        if self.current[1] == 2:
            if os.path.isfile(f"{self.foldername}/{self.current[0]}.txt"):
                self.Dialog("Файл удален", f"Файл {self.current[0]} удален",
                            QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)
            else:
                self.Dialog("Файл не найден", f"Файл {self.current[0]} не существует",
                            QMessageBox.Icon.Warning, 40, 175, QMessageBox.StandardButton.Ok)
                return

            with sqlite3.connect("Main/ForeveryData.db") as db:
                cursor = db.cursor()
                query = """DELETE FROM Files WHERE file_name = ?;"""
                cursor.execute(query, (self.current[0],))
                db.commit()
            os.remove(f"{self.foldername}/{self.current[0]}.txt")
            self.folderclick()
        elif self.current[1] == 1:
            if os.path.isdir(f"{self.current[0]}"):
                self.Dialog("Папка удалена", f"Папка {self.current[0]} удалена успешно",
                            QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)
            else:
                self.Dialog("Папка не найдена", f"Папка {self.current[0]} не найдена",
                            QMessageBox.Icon.Warning, 40, 175, QMessageBox.StandardButton.Ok)
                return

            with sqlite3.connect("Main/ForeveryData.db") as db:
                cursor = db.cursor()
                query = """DELETE FROM Folders WHERE folder_id = ?;"""
                cursor.execute(query, (self.whatfolder,))
                db.commit()
            with sqlite3.connect("Main/ForeveryData.db") as db:
                cursor = db.cursor()
                query = """DELETE FROM Files WHERE folder_id = ?;"""
                cursor.execute(query, (self.whatfolder,))
                db.commit()
            shutil.rmtree(f"{self.current[0]}")
            self.foldershow()
            self.comboBoxfile.clear()

    def gotoprofil(self):
        self.profil = portfolio.Portfolio(self.id, self.x(), self.y(), self)
        self.profil.show()
        self.close()

    def renameobj(self):
        if self.current is None:
            return
        if self.current[1] == 2:
            text, ok = QInputDialog.getText(self, "rename file", "file new name:")
            if ok:
                if os.path.isfile(f"{self.foldername}/{text}.txt"):
                    self.Dialog("Имя файло совпадает с другим", "Новое имя должно отличатся или быть оригинальным",
                                QMessageBox.Icon.Warning, 40, 175, QMessageBox.StandardButton.Ok)
                elif text != "" and text != " ":
                    self.Dialog("Имя файло изменено", f"Новое имя файла - {text}",
                                QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)

                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """UPDATE Files SET file_name = ? WHERE file_name = ?;"""
                        cursor.execute(query, (text, self.current[0]))
                        db.commit()
                    os.renames(f"{self.foldername}/{self.current[0]}.txt", f"{self.foldername}/{text}.txt")
                    self.folderclick()
        elif self.current[1] == 1:
            text, ok = QInputDialog.getText(self, "rename folder", "folder new name:")
            if ok:
                if os.path.isdir(f"{text}"):
                    self.Dialog("Имя папки совпадает с другим", "Новое имя должно отличатся или быть оригинальным",
                                QMessageBox.Icon.Warning, 40, 175, QMessageBox.StandardButton.Ok)
                elif text != "" and text != " ":
                    self.Dialog("Имя папки изменено", f"Новое имя папки - {text}",
                                QMessageBox.Icon.Information, 40, 175, QMessageBox.StandardButton.Ok)
                    with sqlite3.connect("Main/ForeveryData.db") as db:
                        cursor = db.cursor()
                        query = """UPDATE Folders SET folder_name = ? WHERE folder_name = ?;"""
                        cursor.execute(query, (text, self.current[0]))
                        db.commit()
                    os.renames(f"{self.current[0]}", f"{text}")
                    self.foldershow()
