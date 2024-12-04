from Qtdisainer import DataUp
from PyQt6.QtCore import QTimer
from MainWondow import MainWin
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore


class Update(DataUp, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.close()
        self.progressBar.setValue(0)
        self.move(400, 150)
        self.time = QTimer()
        self.time2 = QTimer()
        self.time.timeout.connect(self.sekunda)
        self.time.start(500)

    def goo(self):
        try:
            self.win = MainWin()
            self.win.logreg()
            self.close()
        except Exception as ex:
            print(ex)

    def sekunda(self):
        self.progressBar.setValue(self.progressBar.value() + 10)
        if self.progressBar.value() >= 100:
            self.time.stop()
            self.goo()
