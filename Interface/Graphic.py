from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QGridLayout, QVBoxLayout, QHBoxLayout,QBoxLayout
from PyQt5.QtCore import Qt


class Graphic(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000,650)
        self.center()
        grid = QGridLayout()
        grid.setSpacing(0)
        grid.setContentsMargins(0,0,0,0)
        self.setLayout(grid)

        llayout = QVBoxLayout()
        left = QWidget()
        left.show()
        left.resize(600, 650)
        left.setLayout(llayout)
        grid.addWidget(left, 0,0,1,7)

        rlayout= QVBoxLayout()
        right = QWidget()
        right.show()
        right.resize(300,650)
        right.setLayout(rlayout)
        grid.addWidget(right, 0,7,1,3)
        left.setStyleSheet("background-color:blue")
        right.setStyleSheet("background-color:red")


        btn = QPushButton("Przycisk")
        btn2 = QPushButton("Przycisk2")
        llayout.addWidget(btn)
        rlayout.addWidget(btn2)

        self.setWindowTitle("Pluria")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())