from Animals.Animal import Animal
from Position import Position


class Antelope(Animal):
    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = 'a'

    def action(self, dx=0, dy=0):
        pos = Position()
        self.randMove(pos, 2)
        super().action(pos.x, pos.y)

    def collision(self, attacker):
        if attacker.getImage() != self.image:
            if self.world.randInt(0, 100) <= 50:
                pos = Position()
                pos.x = self.x
                pos.y = self.y
                if self.world.findFreeSpace(pos, 2):
                    a = self.x
                    b = self.y
                    super().action(pos.x - self.x, pos.y - self.y)
                    self.world.moveOrganism(attacker, a, b)
                    self.world.addComment(self.image, "run away from", attacker.getImage())
                else:
                    super().collision(attacker)
            else:
                super().collision(attacker)
        else:
            super().collision(attacker)
