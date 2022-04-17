class Termite:

    def __init__(self, posicion=(0, 0), color="red"):
        self.last_postion = posicion
        self.posicion = posicion
        self.color = color
        self.load = None

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

    def moveUp(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] + interval)

    def moveDown(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] - interval)

    def moveRight(self, interval=1):
        self.posicion = (self.posicion[0] + interval, self.posicion[1])

    def moveLeft(self, interval=1):
        self.posicion = (self.posicion[0] - interval, self.posicion[1])

    def move(self, r, limits, interval=1):
        mov = r.randint(0, 3)
        if mov == 0:
            if self.posicion[1] < limits[1]:
                self.moveUp(interval)
        elif mov == 1:
            if self.posicion[1] > limits[0]:
                self.moveDown(interval)
        elif mov == 2:
            if self.posicion[0] > limits[2]:
                self.moveLeft(interval)
        elif mov == 3:
            if self.posicion[0] < limits[3]:
                self.moveRight(interval)

    def checkChip(self, Chips, posChips, rand, limits, interval, termite, tc):
        if self.posicion in posChips and self.color == "red":
            if Chips[posChips[self.posicion]].color != "white" and self.posicion != self.last_postion:
                print('Toma una chip>> ', Chips[posChips[self.posicion]].color)
                self.color = "green"
                self.load = posChips[self.posicion]
                Chips[self.load].color = "white"
                self.last_postion = self.posicion
                return self.posicion
            else:
                print('No coge la chip que recién dejo')
        elif self.posicion in posChips and self.color == "green":
            if Chips[posChips[self.posicion]].color == "blue":
                print('Choca con chip sin tomar ')
                self.move(rand, limits, interval)
                print('*Se mueve*')
                tc.color(termite.getColor())
                tc.goto(termite.getPos())
                if self.posicion in posChips:
                    print('Se mueve a una chip')
                    if Chips[posChips[self.posicion]].color == "white":
                        print('Se mueve a una chip libre')
                        print('Deja una chip>> ', Chips[posChips[self.posicion]].index)
                        self.color = "red"
                        print("Pos chips antes: ", Chips[self.load].posicion)
                        Chips[self.load].posicion = self.posicion
                        print("Pos chips despues: ", Chips[self.load].posicion)
                        Chips[self.load].color = "blue"
                        self.load = None
                        self.last_postion = self.posicion
                        return self.posicion
                else:
                    print('Deja una chip en un espacio en blanco ')
                    self.color = "red"
                    print("Pos chips antes: ", Chips[self.load].posicion)
                    # print(posChips)
                    posChips[self.getPos()] = posChips.pop(Chips[self.load].posicion)
                    Chips[self.load].posicion = self.posicion
                    print("Pos chips despues: ", Chips[self.load].posicion)
                    Chips[self.load].color = "blue"
                    self.load = None
                    self.last_postion = self.posicion
                    return self.posicion


class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color
