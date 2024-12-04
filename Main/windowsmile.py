from Qtdisainer import Smile
import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


class Windowsmile(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(Smile)
        uic.loadUi(f, self)
        self.setWindowTitle("Smile")
        self.sendsmile.clicked.connect(self.sendsmilebtn)
        self.smile1.clicked.connect(self.smile)
        self.smile2.clicked.connect(self.smile)
        self.smile3.clicked.connect(self.smile)
        self.smile4.clicked.connect(self.smile)
        self.smile5.clicked.connect(self.smile)
        self.smile6.clicked.connect(self.smile)
        self.dict_smile = {"smile1": False, "smile2": False, "smile3": False, "smile4": False, "smile5": False,
                           "smile6": False}

    def sendsmilebtn(self):
        for i in self.dict_smile:
            if self.dict_smile[i] == True:
                return f"/{i}"
        return False

    def smile(self):
        namesmile = self.sender().objectName()
        for i in self.dict_smile:
            if self.dict_smile[i] == True and i != namesmile:
                return
            elif self.dict_smile[i] == True and i == namesmile:
                self.dict_smile[i] = False
                self.sender().setStyleSheet("QPushButton {\n"
                                            "    border-radius: 45px;\n"
                                            "    border: 5px solid rgb(255, 85, 0);\n"
                                            "}QPushButton:pressed{\n"
                                            "    border: 5px solid #934200;\n"
                                            "}")
                return
        self.dict_smile[self.sender().objectName()] = True
        self.sender().setStyleSheet("QPushButton {\n"
                                    "    border-radius: 45px;\n"
                                    "    border: 5px solid rgb(213, 213, 213);\n"
                                    "}"
                                    "QPushButton:pressed{\n"
                                    "    border: 5px solid #934200;\n"
                                    "}")
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Windowsmile()
    ex.show()
    sys.exit(app.exec())
