if __name__ == '__main__':
    from Dataup import Update
    from PyQt6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    ex = Update()
    ex.show()
    sys.exit(app.exec())