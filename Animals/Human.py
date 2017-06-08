from Animals.Animal import Animal
class Human (Animal):
    def __init__(self, power, activity, world, x, y):
        super().__init__(power, activity, world, x, y)
        self.image = 'H';
        # JFrame h = new JFrame();

    def action(self, dx, dy):

        move = None
        if dx == 0 and dy == -1: move = 'u' #// UP
        elif dx == 1 and dy == 0: move = 'r' #// RIGHT
        elif dx == 0 and dy == 1: move = 'd' #// DOWN
        elif dx == -1 and dy == 0: move = 'l' #// LEFT
        elif dx == -1 and dy == -1: move = 'e' #// ESC
        elif dx == 1 and dy == 1: move = 's' #// SPACE

        if move == 'u':
            if self.skill > 0:
                self.fire(0, -1)
            else:
                super().action(0, -1)
        elif move == 'r':
            if self.skill > 0:
                self.fire(1, 0)
            else:
                super().action(1, 0)
        elif move == 'd':
            if self.skill > 0:
                self.fire(0, 1)
            else:
                super().action(0, 1)
        elif move == 'l':
            if self.skill > 0:
                self.fire(-1, 0)
            else:
                super().action(-1, 0)
        elif move == 'e':
            self.world.endGame()
        elif move == 's':
            if self.skill > 0:
                self.fire()
            elif self.skill == 0:
                self.world.addComment(self.image, "actived fire")
                self.skill = 5
                self.fire()
            elif self.skill < 0:
                    self.world.addComment("Fire light up;", str(((-1) * self.skill) - 1) + " to ignite")

        if self.skill < 0: self.skill += 1

    def __del__(self):
        self.world.humanDie()

    def collistion(self, attacker):
        if self.skill > 0:
            self.world.delOrganism(attacker)
            self.world.addComment("H", "burn", attacker.getImage())
        else:
            super().collision(attacker)

    def fire(self, move_x=0, move_y=0):
        self.world.addComment("H:", "BURN IT ALL!;", str(self.skill - 1) + " left")
        if move_x != 0 or move_y != 0:
            place = self.world.checkPlace(self.x + move_x, self.y + move_y)
            if place != ' ' and place != '!':
                self.world.delOrganism(None, self.x + move_x, self.y + move_y)
            super().action(move_x, move_y)
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]

        for i in range(len(dx)):
            place = self.world.checkPlace(self.x + dx[i], self.y + dy[i])
            if place != ' ' and place != '!':
                self.world.delOrganism(None, self.x + dx[i], self.y + dy[i])

        self.skill -= 1
        if self.skill == 0:
            self.skill = -5 -1
            self.world.addComment("H:", "Flame went out;", str((-1) * self.skill - 1) + " to ignite")
            self.image = 'H'

