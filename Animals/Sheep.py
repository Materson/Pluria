from Animals.Animal import Animal


class Sheep (Animal):
    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = 's'

    def action(self, move_dx = 0, move_dy = 0):
        super().action(move_dx, move_dy)