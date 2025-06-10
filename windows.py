from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from pulp import LpMaximize, LpMinimize

import models

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"ui/main.ui", self)

        self.solve_btn.clicked.connect(lambda: self.read_model())

        self.model = {
            "sense": None,
            "objective": None,
            "restrictions": []
        }

    def read_model(self):
        objective = self.lucro_x.value() * models.x + self.lucro_y.value() * models.y
        restrictions = [
            self.consumo_1_x.value() * models.x + self.consumo_1_y.value() * models.y <= self.materia_1.value(),
            self.consumo_2_x.value() * models.x + self.consumo_2_y.value() * models.y <= self.materia_2.value(),

            models.x >= self.demanda_min_x.value(),
            models.x <= self.demanda_max_x.value(),

            models.y >= self.demanda_min_y.value(),
            models.y <= self.demanda_max_y.value()
        ]
    
        result = models.solve(objective, restrictions)
        self.x_value.setText(str(result['x']))
        self.y_value.setText(str(result['y']))
        self.z_value.setText(str(result['z']))
        print(result['status'])

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()