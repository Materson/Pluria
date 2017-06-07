from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QGridLayout, QVBoxLayout, QHBoxLayout,QBoxLayout, QScrollArea, QLineEdit, QLabel, QSpacerItem, QWidgetItem
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
        self.right = QWidget()
        self.right.setStyleSheet("background-color: #9AF")
        self.rlayout = QVBoxLayout()
        self.rlayout.setAlignment(Qt.AlignTop)
        self.right.setLayout(self.rlayout)
        self.grid.addWidget(self.right, 0, 7, 1, 3)

        self.sizeWidget = QWidget()
        self.sizeLayout = QVBoxLayout()
        self.sizeWidget.setLayout(self.sizeLayout)
        self.rlayout.addWidget(self.sizeWidget)

        widthLabel = QLabel("Szerokosc")
        self.inWidth = QLineEdit()
        heightLabel = QLabel("Wysokosc")
        self.inHeight = QLineEdit()
        btn = QPushButton("Utwórz")
        btn.clicked.connect(self.createMap)

        self.sizeLayout.addWidget(widthLabel)
        self.sizeLayout.addWidget(self.inWidth)
        self.sizeLayout.addWidget(heightLabel)
        self.sizeLayout.addWidget(self.inHeight)
        self.sizeLayout.addWidget(btn)

    def createMap(self):
        width = self.inWidth.text()
        height = self.inHeight.text()
        try:
            int(width)
            int(height)
        except ValueError:
            return False
        # remove old widget and add new place
        self.height = height
        self.width = width
        self.sizeWidget.setParent(None)
        self.menuWidget = QWidget()
        self.menuLayout = QVBoxLayout()
        self.menuWidget.setLayout(self.menuLayout)
        self.rlayout.addWidget(self.menuWidget)

        # add size widget
        sizeWidget = QWidget()
        sizeLayout = QHBoxLayout()
        sizeWidget.setLayout(sizeLayout)
        self.menuLayout.addWidget(sizeWidget)
        widthLabel = QLabel("Szerokosc: "+self.width)
        heightLabel = QLabel("Wysokosc: "+self.height)

        sizeLayout.addWidget(widthLabel)
        sizeLayout.addWidget(heightLabel)

        #add buttons
        buttonsWidget = QWidget()
        buttonsLayout = QHBoxLayout()
        buttonsWidget.setLayout(buttonsLayout)

        nextTurnBtn = QPushButton("Nastepna tura")
        nextTurnBtn.clicked().connect(self.buttonHandler)


        def buttonHandler(self):
            pass
