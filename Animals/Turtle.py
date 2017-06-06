from Animals.Animal import Animal


class Turtle (Animal):
    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = 't'

    def action(self, dx=0, dy=0):
        dx = self.world.randInt(0,100)
        if dx >= 75:
            super().action()
        else:
            self.world.addComment(self.image, "resting")

    def collision(self, attacker):
        if attacker.getImage() == self.image:
            super().collision(attacker)
        elif attacker.getPower() >= 5:
            super().collision(attacker)
        else:
            self.world.addComment(self.image, "blocked", attacker.getImage())

