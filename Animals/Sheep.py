from Animals.Animal import Animal


class Sheep (Animal):
    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = 's'
