from Plants.Plant import Plant


class Berry (Plant):
    def __init__(self, power, world, x, y):
        super().__init__(power, world, x, y)
        self.image = 'b'

    def collision(self, attacker):
        self.world.addComment(self.image, "poisoned", attacker.getImage())
        self.world.delOrganism(attacker)
