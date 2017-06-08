from Plants.Plant import Plant


class Borscht (Plant):
    def __init__(self, power, world, x, y):
        super().__init__(power, world, x, y)
        self.image = 'X'

    def action(self, a=0, b=0):
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]

        for i in range(len(dx)):
            place = self.world.checkPlace(self.x + dx[i], self.y + dy[i])
            if place != ' ' and place != '!' and self.world.checkOrganismActivity(self.x + dx[i], self.y + dy[i]) > 0 and place != "C" and place != "s'":
                self.world.addComment(self.image, "poisoned", place)
                self.world.delOrganism(None, self.x + dx[i], self.y + dy[i])

    def collision(self, attacker):
        if attacker.getImage() != "C":
            self.world.addComment(self.image, "poisoned", attacker.getImage())
            self.world.delOrganism(attacker)
        else:
            super().collision(attacker)
