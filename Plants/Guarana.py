from Plants.Plant import Plant


class Guarana (Plant):
    def __init__(self, power, world, x, y):
        super().__init__(power, world, x, y)
        self.image = 'G'

    def collision(self, attacker):
        attacker.setPower(attacker.getPower() + 3)
        self.world.addComment(attacker.getImage(), "ate", self.image+" strength +"+str(3)+" actual: "\
                              + str(attacker.getPower()))
        super().collision(attacker)

