from World import World
from PyQt5.QtWidgets import QApplication
from Interface.Graphic import Graphic
import sys

app = QApplication(sys.argv)
window = Graphic()
sys.exit(app.exec())
# pluria = World(7, 5)
# pluria.drawWorld()
# pluria.nextTurn()
# pluria.nextTurn()