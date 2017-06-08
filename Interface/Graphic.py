from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QScrollArea, QLineEdit, QLabel, QTextEdit, QMenu
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt
from World import World

class Graphic(QWidget):
    def __init__(self):
        super().__init__()
        self.minBtnSize = 30
        # self.widget.keyPressed.connect(self.keyPressEvent)
        # self.keyPressEvent = self.keyHandler
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
        self.inWidth.setFocus()

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
        self.inWidth = None
        self.inHeight = None

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
        # self.commentsArea.setLineWrapMode(QTextEdit.NoWrap)
        # self.commentsArea.moveCursor(QTextCursor.End)
        # sb = self.commentsArea.verticalScrollBar()
        # sb.setValue(sb.maximum())
        self.commentsArea.textChanged.connect(self.moveTextArea)
        font = self.commentsArea.font()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.commentsArea.setFont(font)
        self.menuLayout.addWidget(self.commentsArea)

        # remove old and create new map
        self.mapWidget.setParent(None)
        self.mapWidget = QWidget(self.left)
        self.mapLayout = QGridLayout()
        self.mapLayout.setSpacing(0)
        self.mapLayout.setContentsMargins(0, 0, 0, 0)
        self.mapWidget.setLayout(self.mapLayout)

        self.map = World(self.width, self.height, self)
        self.buttons = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(None)
            self.buttons.append(row)

        for i in range(self.height):
            for j in range(self.width):
                text = self.map.checkPlace(j, i)
                btn = QPushButton(text)
                btn.setFlat(False)
                btn.setFixedWidth(700 / self.width)
                btn.setFixedHeight(600 / self.height)
                btn.setMinimumHeight(self.minBtnSize)
                btn.setMinimumWidth(self.minBtnSize)
                btn.setContextMenuPolicy(Qt.CustomContextMenu)
                btn.customContextMenuRequested.connect(self.contextMenu)
                btn.clicked.connect(self.returnFocus)
                self.mapLayout.addWidget(btn, i, j)
                self.buttons[j][i] = btn
        self.left.setWidget(self.mapWidget)
        self.refreshMap()

        self.setFocus()

    def buttonHandler(self):
        # TODO implement save and load
        text = self.sender().text()
        if text == "Nastepna tura":
            self.map.nextTurn()
            self.refreshMap()

        print("button Handler")
        self.setFocus()

    def returnFocus(self):
        self.setFocus()

    def contextMenu(self):
        self.setFocus()
        btn = self.sender()
        if btn.text() != " ":
            print("nie puste")
            return False
        idx = self.mapLayout.indexOf(btn)
        location = self.mapLayout.getItemPosition(idx)
        x = location[1]
        y = location[0]

        menu = QMenu(self)
        antelope = menu.addAction("Antelope")
        berry = menu.addAction("Berry")
        borscht = menu.addAction("Borscht")
        fox = menu.addAction("Fox")
        grass = menu.addAction("Grass")
        guarana = menu.addAction("Guarana")
        human = False
        if self.map.humanAlive() == False:
            human = menu.addAction("Human")
        milk = menu.addAction("Milk")
        turtle = menu.addAction("Turtle")
        sheep = menu.addAction("Sheep")
        wolf = menu.addAction("Wolf")

        vscroll = self.left.verticalScrollBar()
        hscroll = self.left.horizontalScrollBar()
        pos = btn.pos()
        pos.setX(pos.x() - hscroll.value())
        pos.setY(pos.y() - vscroll.value())
        action = menu.exec_(self.mapToGlobal(pos))
        if action == antelope:
            self.map.addOrganism("a", x, y)
        elif action == berry:
            self.map.addOrganism("b", x, y)
        elif action == borscht:
            self.map.addOrganism("X", x, y)
        elif action == fox:
            self.map.addOrganism("f", x, y)
        elif action == grass:
            self.map.addOrganism("g", x, y)
        elif action == guarana:
            self.map.addOrganism("G", x, y)
        elif action == human:
            self.map.addOrganism("H", x, y)
        elif action == milk:
            self.map.addOrganism("m", x, y)
        elif action == turtle:
            self.map.addOrganism("t", x, y)
        elif action == sheep:
            self.map.addOrganism("s", x, y)
        elif action == wolf:
            self.map.addOrganism("w", x, y)

        self.refreshMap()

    def addComment(self, text):
        self.commentsArea.insertPlainText(text+"\n")

    def moveTextArea(self):
        self.commentsArea.moveCursor(QTextCursor.End)
        self.commentsArea.ensureCursorVisible()

    def refreshMap(self):
        for i in range(self.height):
            for j in range(self.width):
                text = self.map.checkPlace(j, i)
                self.buttons[j][i].setText(text)
                if text == "H" or text == "O":
                    self.buttons[j][i].setStyleSheet("background-color:#aa0")
                    vscroll = self.left.verticalScrollBar()
                    hscroll = self.left.horizontalScrollBar()
                    vscroll.setValue(self.buttons[j][i].y() - self.left.height()/2)
                    hscroll.setValue(self.buttons[j][i].x() - self.left.width()/2)
                else:
                    self.buttons[j][i].setStyleSheet("background-color:#d")

    def keyPressEvent(self, e):

        print("key press event")
        if e.key() == Qt.Key_Left:
            self.map.nextTurn(-1, 0)
            self.refreshMap()
        elif e.key() == Qt.Key_Down:
            self.map.nextTurn(0, 1)
            self.refreshMap()
        elif e.key() == Qt.Key_Right:
            self.map.nextTurn(1, 0)
            self.refreshMap()
        elif e.key() == Qt.Key_Up:
            self.map.nextTurn(0, -1)
            self.refreshMap()
        elif e.key() == Qt.Key_Space:
            self.map.nextTurn(1, 1)
            self.refreshMap()
        elif e.key() == Qt.Key_Return:
            print("enter")
            if (self.inHeight is not None) and (self.inWidth is not None):
                self.createMap()
        elif e.key() == Qt.Key_Escape:
            self.close()

            # def contextMenuEvent(self, e):
            #     menu = QMenu(self)
            #     quitAction = menu.addAction("Quit")
            #     action = menu.exec_(self.mapToGlobal(e.pos()))
            #     print(e.sender().text())
            #     if action == quitAction:
            #         self.close()