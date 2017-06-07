from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QGridLayout, QVBoxLayout, QHBoxLayout,QBoxLayout, QScrollArea, QLineEdit, QLabel
from PyQt5.QtCore import Qt


class Graphic(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000,600)
        self.center()
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0,0,0,0)
        self.setLayout(self.grid)

        left = QScrollArea()
        self.grid.addWidget(left, 0,0,1,7)
        left.setWidgetResizable(True)
        mapWidget = QWidget(left)

        mapLayout = QGridLayout(mapWidget)
        mapLayout.setContentsMargins(0,0,0,0,)
        mapLayout.setSpacing(0)
        mapWidget.setLayout(mapLayout)

        self.initRight()

        left.setStyleSheet("background-color:#fff")

        h = 15
        w = 2
        buttons = []
        for i in range(w):
            row = []
            for j in range(h):
                row.append(None)
            buttons.append(row)

        for i in range(h):
            for j in range(w):
                btn = QPushButton("Przycisk("+str(j)+","+str(i)+")")
                btn.setFlat(False)
                btn.setFixedWidth(700/w)
                btn.setFixedHeight(600/h)
                btn.setMinimumHeight(60)
                btn.setMinimumWidth(60)
                mapLayout.addWidget(btn,i,j)
                buttons[j][i] = btn
        left.setWidget(mapWidget)

        self.setWindowTitle("Pluria")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initRight(self):
        self.rlayout = QVBoxLayout()
        self.rlayout.setAlignment(Qt.AlignTop)
        self.right = QWidget()
        self.right.setLayout(self.rlayout)
        self.grid.addWidget(self.right, 0, 7, 1, 3)
        self.right.setStyleSheet("background-color: #9AF")

        widthLabel = QLabel("Szerokosc")
        inWidth = QLineEdit()
        heightLabel = QLabel("Wysokosc")
        inHeight = QLineEdit()
        btn = QPushButton("Utwórz")

        self.rlayout.addWidget(widthLabel)
        self.rlayout.addWidget(inWidth)
        self.rlayout.addWidget(heightLabel)
        self.rlayout.addWidget(inHeight)
        self.rlayout.addWidget(btn)

