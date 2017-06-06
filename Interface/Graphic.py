from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class Graphic(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000,650)
        self.center()

        grid = QGridLayout()
        self.setLayout(grid)

        layout = QHBoxLayout()
        left = QWidget()
        left.show()
        left.resize(600, 650)
        left.setLayout(layout)
        p = left.palette()
        p.setColor(left.backgroundRole(), Qt.red)
        left.setPalette(p)
        grid.addWidget(left, 1,0, 1,3)

        btn = QPushButton("Przycisk")
        layout.addWidget(btn)

        self.setWindowTitle("Pluria")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())