class Organism:

    def __init__(self):
        self.power = None
        self.activity = None
        self.old = 1
        self.x = None
        self.y = None
        self.image = None
        self.world = None
        self.skill = 0

    def action(self, move_x=0, move_y=0):
        return NotImplementedError

    def collision(self,attacker):
        return NotImplementedError

    def draw(self):
        print(self.image, end="")

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getImage(self):
        return self.image

    def increaseOld(self):
        self.old += 1

    def getActivity(self):
        return self.activity

    def getOld(self):
        return self.old

    def getSkill(self):
        return self.skill

    def getPower(self):
        return self.power

    def setPower(self, x):
        self.power = x

    def setOld(self,x):
        self.old = x

    def setSkill(self,x):
        self.skill = x

    def randMove(self, pos, ran):
        tmpx = [0, 1, 1, 1, 0, -1, -1, -1]
        tmpy = [-1, -1, 0, 1, 1, 1, 0, -1]

        findPlace = False
        move_num = len(tmpx) * ran
        dx = []
        dy = []
        move = []
        for i in range(move_num):
            dx.append(None)
            dy.append(None)
            move.append(i)
        for i in range(ran):
            for j in range(int(move_num/ran)):
                dx[int(move_num / ran) * i + j] = tmpx[j] * (i + 1)
                dy[int(move_num / ran) * i + j] = tmpy[j] * (i + 1)

        place = None

        while move_num > 0 and findPlace == False:
            place = self.world.randInt(0, move_num)
            move_num -= 1
            if self.world.checkPlace(self.x + dx[move[place]], self.y + dy[move[place]]) == '!':
                move[place] = move[move_num]
                continue

            findPlace = True
            place = move[place]
            pos.x = dx[place]
            pos.y = dy[place]