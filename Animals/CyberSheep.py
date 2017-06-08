from Animals.Sheep import Sheep

class Point:
    def __init__(self, x, y, fromX, fromY):
        self.x = x
        self.y = y
        self.dx = fromX
        self.dy = fromY


class CyberSheep(Sheep):
    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = "s'"

    def action(self, move_dx = 0, move_dy = 0):
        if self.world.getBorschtCount() > 0:
            self.image = "C"
            self.power = 11
            self.visit = []
            for i in range(self.world.getHeight() * self.world.getWidth()):
                self.visit.append(False)

            number = self.world.getWidth() * self.y + self.x
            self.visit[number] = True

            neighbors = []
            dx = self.world.getDx()
            dy = self.world.getDy()
            for i in range(len(dx)):
                if self.world.checkPlace(self.x + dx[i], self.y + dy[i]) != "!":
                    place = Point(self.x + dx[i], self.y + dy[i], dx[i], dy[i])
                    neighbors.append(place)

            while len(neighbors) > 0:
                place = neighbors.pop(0)
                if self.world.checkPlace(place.x, place.y) == "X":
                    neighbors = []
                    super().action(place.dx, place.dy)
                else:
                    for i in range(len(dx)):
                        if self.world.checkPlace(place.x + dx[i], place.y + dy[i]) != "!":
                            number = self.world.getWidth() * place.y + dy[i] + place.x + dx[i]
                            if(self.visit[number] == False):
                                self.visit[number] = True
                                newPlace = Point(place.x + dx[i], place.y + dy[i], place.dx, place.dy)
                                neighbors.append(newPlace)
        else:
            self.image = "s'"
            self.power = 4
            super().action()