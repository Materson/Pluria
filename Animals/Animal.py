from Organism import Organism
from Position import Position


class Animal(Organism):

    def __init__(self, power, activity, world, x, y):
        super().__init__()
        self.power = power
        self.activity = activity
        self.world = world
        self.x = x
        self.y = y

    def action(self,move_dx=0, move_dy=0):
        if move_dx == 0 and move_dy == 0:
                pos = Position()
                self.randMove(pos, 1)
                move_dx = pos.x
                move_dy = pos.y
        if self.world.checkPlace(self.x + move_dx, self.y + move_dy) != '!':
            if self.world.checkPlace(self.x + move_dx, self.y + move_dy) == ' ':
                self.world.moveOrganism(self, self.x + move_dx, self.y + move_dy)
                self.world.addComment(self.image, "move")
            else:
                self.world.collision(self, self.x + move_dx, self.y + move_dy)

    def collision(self, attacker):
        if attacker.getImage() == self.image:
            # // copulate
            pos = Position()
            pos.x = self.x
            pos.y = self.y
            if self.world.findFreeSpace(pos, 1):
                self.world.addOrganism(self.image, pos.x, pos.y)
                self.world.addComment(self.image, "multiplied")
            else:
                self.world.addComment(self.image, "don't find space for multiplied")
        else:
            # // attack
            if attacker.getPower() < self.power:

                self.world.addComment(self.image, "ate", attacker.getImage())
                self.world.delOrganism(attacker)
            else:
                a = self.x
                b = self.y
                self.world.moveOrganism(attacker, a, b)
                self.world.addComment(attacker.getImage(), "ate", self.image)
                self.world.delOrganism(self)
