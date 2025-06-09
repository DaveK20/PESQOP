from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import json

import models

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"ui/main.ui", self)

        self.model = None

    def read_model(self, path):
        with open(path, 'r') as file:
            model =json.load(file)

        print(models.verify_model(model))
    


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.read_model("example.po")
    window.show()
    app.exec()