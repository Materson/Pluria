from Plants.Plant import Plant


class Grass (Plant):
    def __init__(self, power, world, x, y):
        super().__init__(power, world, x, y)
        self.image = 'g'
