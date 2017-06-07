from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QScrollArea, QLineEdit, QLabel, QTextEdit
from PyQt5.QtGui import QTextCursor
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

        self.left = QScrollArea()
        self.left.setWidgetResizable(True)
        self.left.setStyleSheet("background-color:#ddd")
        self.grid.addWidget(self.left, 0,0,1,7)

        self.mapWidget = QWidget(self.left)
        self.mapLayout = QGridLayout(self.mapWidget)
        self.mapLayout.setContentsMargins(0,0,0,0)
        self.mapLayout.setSpacing(0)
        self.mapWidget.setLayout(self.mapLayout)

        self.initRight()

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

        self.menuWidget = QWidget()
        self.menuLayout = QVBoxLayout()
        self.menuWidget.setLayout(self.menuLayout)
        self.rlayout.addWidget(self.menuWidget)

        widthLabel = QLabel("Szerokosc")
        self.inWidth = QLineEdit()
        heightLabel = QLabel("Wysokosc")
        self.inHeight = QLineEdit()
        btn = QPushButton("Utwórz")
        btn.clicked.connect(self.createMap)

        self.menuLayout.addWidget(widthLabel)
        self.menuLayout.addWidget(self.inWidth)
        self.menuLayout.addWidget(heightLabel)
        self.menuLayout.addWidget(self.inHeight)
        self.menuLayout.addWidget(btn)

    def createMap(self, width = 0, height = 0):
        if width == 0 and height == 0:
            width = self.inWidth.text()
            height = self.inHeight.text()
            try:
                int(width)
                int(height)
            except ValueError:
                return False
        self.height = int(height)
        self.width = int(width)

        # remove old and create new map
        self.mapWidget.setParent(None)
        self.mapWidget = QWidget(self.left)
        self.mapLayout = QGridLayout()
        self.mapLayout.setSpacing(0)
        self.mapLayout.setContentsMargins(0,0,0,0)
        self.mapWidget.setLayout(self.mapLayout)

        buttons = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(None)
            buttons.append(row)

        for i in range(self.height):
            for j in range(self.width):
                btn = QPushButton("Przycisk(" + str(j) + "," + str(i) + ")")
                btn.setFlat(False)
                btn.setFixedWidth(700 / self.width)
                btn.setFixedHeight(600 / self.height)
                btn.setMinimumHeight(60)
                btn.setMinimumWidth(60)
                self.mapLayout.addWidget(btn, i, j)
                buttons[j][i] = btn
        self.left.setWidget(self.mapWidget)

        # remove old widget and add new place
        self.menuWidget.setParent(None)
        self.menuWidget = QWidget()
        self.menuLayout = QVBoxLayout()
        self.menuWidget.setLayout(self.menuLayout)
        self.rlayout.addWidget(self.menuWidget)

        # add size widget
        sizeWidget = QWidget()
        sizeLayout = QHBoxLayout()
        sizeWidget.setLayout(sizeLayout)
        self.menuLayout.addWidget(sizeWidget)
        widthLabel = QLabel("Szerokosc: "+str(self.width))
        heightLabel = QLabel("Wysokosc: "+str(self.height))

        sizeLayout.addWidget(widthLabel)
        sizeLayout.addWidget(heightLabel)

        #add buttons
        buttonsWidget = QWidget()
        buttonsLayout = QHBoxLayout()
        buttonsWidget.setLayout(buttonsLayout)
        self.menuLayout.addWidget(buttonsWidget)

        nextTurnBtn = QPushButton("Nastepna tura")
        nextTurnBtn.clicked.connect(self.buttonHandler)

        saveBtn = QPushButton("Zapisz")
        saveBtn.clicked.connect(self.buttonHandler)

        loadBtn = QPushButton("Wczytaj")
        loadBtn.clicked.connect(self.buttonHandler)

        buttonsLayout.addWidget(nextTurnBtn)
        buttonsLayout.addWidget(saveBtn)
        buttonsLayout.addWidget(loadBtn)

        # comments area
        self.commentsArea = QTextEdit()
        self.commentsArea.setReadOnly(True)
        self.commentsArea.setLineWrapMode(QTextEdit.NoWrap)
        self.commentsArea.moveCursor(QTextCursor.End)
        self.menuLayout.addWidget(self.commentsArea)

    def buttonHandler(self):
        # TODO implement this function
        pass
