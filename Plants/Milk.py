from Plants.Plant import Plant


class Milk (Plant):
    def __init__(self, power, world, x, y):
        super().__init__(power, world, x, y)
        self.image = 'm'

    def action(self, dx=0, dy=0):
        for i in range(3):
            super().action(dx, dy)

