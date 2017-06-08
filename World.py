import os
from Animals import *
from Plants import *
from random import randint as rd


class World:
    def __init__(self, width, height, menu=None):
        self.play = True
        self.menu = menu
        self.width = width
        self.height = height
        self.orgNum = 0
        self.human = False
        self.menu = menu
        self.map =  []
        for i in range(0, self.width):
            row = []
            for j in range(0, self.height):
                row.append(None)
            self.map.append(row)

        self.comment_i = 0
        self.COMMENTS_AMOUNT = 10
        self.comments = []
        for i in range(self.COMMENTS_AMOUNT):
            self.comments.append(None)

        self.order = []
        for i in range(8):
            self.order.append([])

        self.FILL_RATIO = 5
        self.fillWorld()
        self.drawWorld()

    def getOrganism(self, x,  y):
        return self.map[x][y]

    # // ~World()
    #    // {
    # // for (int i = 0; i < height; i++)
    # // {
    #    //
    # for (int j = 0; j < width; j++)
    # // {
    # // if (map[j][i] != null)
    # // delete(map[j][i]);
    # //	}
    # //		delete[](map[i]);
    # //	}
    # //	delete[](map);
    # //
    # //	delete[](order);
    # //}

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def nextTurn(self, dx=0, dy=0):
        # TODO repair do move if is new organism
        for i in range(7,-1,-1):
            if len(self.order[i]) == 0:
                continue

            for j in range(0, len(self.order[i])):
                if self.order[i] is not None:
                    self.order[i][j].increaseOld()

        for i in range(7,-1,-1):
            if len(self.order[i]) == 0:
                continue
            j = 0
            while j < len(self.order[i]):
                if isinstance(self.order[i][j], Human.Human):
                    self.order[i][j].action(dx, dy)
                else:
                    self.order[i][j].action()
                j += 1

        self.drawWorld()

    def drawWorld(self):
        os.system("cls")
        print("Mateusz Szymanowski, nr:165319")
        for i in range(0, self.height * 2 + 1):
            for j in range(0, self.width * 2 + 1):
                if (i % 2 == 0) and (j % 2 == 0):
                    print("+", end='')
                elif (i % 2 == 0) and (j % 2 == 1):
                    print("-", end='')

                if (i % 2 == 1) and (j % 2 == 0):
                    print("|", end='')
                if (i % 2 == 1) and (j % 2 == 1):
                    if self.map[int(j / 2)][int(i / 2)] is None:
                        print(" ", end='')
                    else:
                        self.map[int(j / 2)][int(i / 2)].draw()
            print("")
        self.printComments()

    def moveOrganism(self, org, x,  y):
        self.map[x][y] = org
        self.map[org.getX()][org.getY()] = None
        org.setX(x)
        org.setY(y)

    def checkPlace(self, x, y):
        if x >= self.width or y >= self.height \
                or x < 0 or y < 0:
            return '!'
        if self.map[x][y] is None:
            return ' '
        return self.map[x][y].getImage()

    def findFreeSpace(self, pos, ran):
        dx= [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]

        for  j in range(1, ran+1):
            for i in range(0,len(dx)):
                place = self.checkPlace(pos.x + (dx[i] * j), pos.y + (dy[i] * j))
                if place == '!' or place != ' ':
                    continue

                pos.x += (dx[i] * j)
                pos.y += (dy[i] * j)
                return True
        return False

    def randInt(self, mini, maxi):
        if maxi - mini == 0:
            return 0
        return rd(mini, maxi-1)

    def addOrganism(self, image, x, y):
        if image ==  'w':
            self.map[x][y] = Wolf.Wolf(9, 5, self, x, y)
            self.order[5].append(self.map[x][y])
        elif image == 's':
            self.map[x][y] = Sheep.Sheep(4, 4, self, x, y)
            self.order[4].append(self.map[x][y])
        elif image == 'f':
            self.map[x][y] = Fox.Fox(3, 7, self, x, y)
            self.order[7].append(self.map[x][y])
        elif image == 't':
            self.map[x][y] = Turtle.Turtle(2, 1, self, x, y)
            self.order[1].append(self.map[x][y])
        elif image == 'a':
            self.map[x][y] = Antelope.Antelope(4, 4, self, x, y)
            self.order[4].append(self.map[x][y])
        elif image == 'H':
            self.map[x][y] = Human.Human(5, 5, self, x, y)
            self.order[5].append(self.map[x][y])
        elif image == 'g':
            self.map[x][y] = Grass.Grass(0, self, x, y)
            self.order[0].append(self.map[x][y])
        elif image == 'm':
            self.map[x][y] = Milk.Milk(0, self, x, y)
            self.order[0].append(self.map[x][y])
        elif image == 'G':
            self.map[x][y] = Guarana.Guarana(0, self, x, y)
            self.order[0].append(self.map[x][y])
        elif image == 'b':
            self.map[x][y] = Berry.Berry(99, self, x, y)
            self.order[0].append(self.map[x][y])
        elif image == 'X':
            self.map[x][y] = Borscht.Borscht(10, self, x, y)
            self.order[0].append(self.map[x][y])
        else:
            self.map[x][y] = None
            self.orgNum -= 1
        self.orgNum += 1

    def fillWorld(self):
        organism = "abXHfgGmstw"
        h_x = -1
        h_y = -1
        for i in range(0,len(organism)):
            if organism[i] == 'H':
                if self.human == False:
                    h_x = self.randInt(0, self.width)
                    h_y = self.randInt(0, self.height)
                    self.addOrganism('H', h_x, h_y)
                    self.addComment("H", "created")
                    self.human = True
                organism = organism.replace('H', '')
                break

        for i in range(0,self.height):
            for j in range(0,self.width):
                if i == h_y and j == h_x:
                    continue
                if self.randInt(1, 100) <= self.FILL_RATIO * 10:
                    rand_org = self.randInt(1, 100) % len(organism)
                    self.addOrganism(organism[rand_org], j, i)
                    if organism[rand_org] != ' ':
                        self.addComment(organism[rand_org], "created", "")
                else:
                    self.map[j][i] = None

    def delOrganism(self, org, x=0, y=0):
        if org == None:
            org = self.map[x][y]
        if self.map[org.getX()][org.getY()] == org:
            self.map[org.getX()][org.getY()] = None
        activity = org.getActivity()
        for i in range(0, len(self.order[activity])):
            if self.order[activity][i] == org:
                del self.order[activity][i]
                break
        self.orgNum -= 1

    def collision(self, attacker, x, y):
        self.map[x][y].collision(attacker)

    def checkOrganismPower(self, x, y):
        if self.map[x][y] is not None:
            return self.map[x][y].getPower()
        return 0

    def checkOrganismActivity(self, x, y):
        if self.map[x][y] is not None:
            return self.map[x][y].getActivity()
        return 0

    def humanDie(self):
        self.human = False

    def humanAlive(self):
        return self.human

    def game(self):
        return self.play

    def endGame(self):
        self.play = False

    def addComment(self, org1, action, org2=""):
        self.comments[self.comment_i] = org1 + " " + action + " " + org2
        self.comment_i += 1
        self.comment_i = self.comment_i % (self.COMMENTS_AMOUNT)
        self.comments[self.comment_i] = "*********************************"
        self.menu.addComment(org1 + " " + action + " " + org2)

    def printComments(self):
        for i in range(0, self.COMMENTS_AMOUNT):
            if self.comments[i] != "":
                print(self.comments[i])

    def prepareSave(self):
        text = None
        text += self.width + " " + self.height + " " + str(self.orgNum) + " "

        for i in range(7, -1, -1):
            if len(self.order[i]) == 0:
                continue

            for j in range(0, len(self.order[i])):
                org = self.order[i][j]
                text += org.getImage() + " " + org.getX() + " " + org.getY() + " " + org.getPower() + " " + org.getOld() + " "
                if isinstance(org, Human.Human):
                    text += org.getSkill() + " "
        return text

    # def
    # void
    # saveFile()
    # {
    # try{
    # PrintWriter file = new PrintWriter("save.txt");
    # file.println(prepareSave());
    # file.close();
    #
    # } catch(IOException e)
    # {
    # //
    # break;
    # }
    # }

    # def
    # void
    # loadFile()
    # throws
    # FileNotFoundException
    # {
    #     String
    # text = "";
    # try{
    # Scanner file = new Scanner(new File("save.txt"));
    # text = file.nextLine();
    # load(text);
    # file.close();
    # } catch(IOException e)
    # {
    # //
    # break;
    # }
    # }

    def load(self, text):
        arr = text.split(" ")
        self.width = int(arr[0])
        self.height = int(arr[1])
        self.orgNum = int(arr[2])

        self.map = []
        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                row.append(None)
            self.map.append(row)

        self.order = []
        for i in range(0,8):
            self.order.append(None)
        for i in range(0, len(self.order)):
            self.order[i] = []

        k = self.orgNum
        self.human = False
        for j in range(k):
            if self.human:
                i = 4 + j * 5
            else:
                i = 3 + j * 5
            org = arr[i][0]
            i += 1
            x = int(arr[i])
            i += 1
            y = int(arr[i])
            i += 1
            power = int(arr[i])
            i += 1
            old = int(arr[i])
            i += 1

            self.addOrganism(org, x, y)
            self.map[x][y].setPower(power)
            self.map[x][y].setOld(old)
            if isinstance(self.map[x][y], Human.Human):
                skill = int(arr[i])
                self.map[x][y].setSkill(skill)
                self.human = True
        self.orgNum = k
