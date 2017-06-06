from Organism import Organism
from Position import Position


class Plant (Organism):

    def __init__(self, power, world, x, y):
        super().__init__();
        self.power = power
        self.world = world
        self.x = x
        self.y = y
        self.activity = 0

    def action(self, move_dx=0, move_dy=0):
        if self.world.randInt(0, 100) <= 2 * 10:
            pos = Position()
            pos.x = self.x
            pos.y = self.y
            if self.world.findFreeSpace(pos, 1):
                self.world.addOrganism(self.image, pos.x, pos.y)
                self.world.addComment(self.image, "spread")

    def collision(self, attacker):
        a = self.x
        b = self.y
        self.world.moveOrganism(attacker, a, b)
        self.world.addComment(attacker.getImage(), "ate", self.image)
        self.world.delOrganism(self)
