from Animals.Animal import Animal
class Fox (Animal):

    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = 'f'

    def action(self, a=0, b=0):
        dx = [ 0, 1, 1, 1, 0, -1, -1, -1 ]
        dy = [ -1, -1, 0, 1, 1, 1, 0, -1 ]
        findPlace = False
        move_num = len(dx)
        move = []
        for i in range(move_num):
            move.append(i)
        rand_int = None
        place = None

        while move_num >= 0 and findPlace is False:
            rand_int = self.world.randInt(0, move_num)
            move_num -= 1
            place = self.world.checkPlace(self.x + dx[move[rand_int]], self.y + dy[move[rand_int]])
            if place == '!':
                move[rand_int] = move[move_num]
                continue

            if place != ' ':
                if self.world.checkOrganismPower(self.x + dx[move[rand_int]], self.y + dy[move[rand_int]]) > self.power:
                    move[rand_int] = move[move_num]
                    self.world.addComment(self.image, "hissed", place)
                    continue

            findPlace = True
            super().action(dx[move[rand_int]], dy[move[rand_int]])

