# Metodo para sacar la llave del diccionario de poschips mediante su valor
def get_key(val, posChips):
    for key, value in posChips.items():
        if val == value:
            return key


# Metodo que devuelve la distancia euclidiana de una coordenada comparada con la coordenada de la clave 0 del poschips
def calcDist(position, posChips):
    import numpy as np
    # Pasamos las coordenadas a array para poder restarlos
    posA = np.asarray(position)
    posB = np.asarray(get_key(0, posChips))  # Obtenemos la coordenada del valor 0
    return np.linalg.norm(posA - posB)  # retornamos al distancia euclidiana


# Metodo que genera las distancias y diccionario de posibles movimientos
def generateDistances(children, posChips):
    distances = []
    posibleMoves = {}
    # Por cada hijo calculamos la distancia euclidiana
    for child in children:
        distances.append(calcDist(child, posChips))
        # Agregamos al diccionario la clave (distancia euclidiana) y valor actual (coordenada)
        posibleMoves[calcDist(child, posChips)] = child
    return distances, posibleMoves


# Retorna la menor distancia de un arreglo
def getShortestDistance(distances):
    return min(distances)


class Termite:

    def __init__(self, posicion=(0, 0), color="green"):
        self.last_postion = posicion
        self.posicion = posicion
        self.color = color
        self.load = None

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

    # Funciones de sucesor
    def moveUp(self, interval=1):
        return self.posicion[0], (self.posicion[1] + interval)

    def moveDown(self, interval=1):
        return self.posicion[0], (self.posicion[1] - interval)

    def moveRight(self, interval=1):
        return (self.posicion[0] + interval), self.posicion[1]

    def moveLeft(self, interval=1):
        return (self.posicion[0] - interval), self.posicion[1]

    # Noreste
    def moveNE(self, interval=1):
        return self.posicion[0] + interval, self.posicion[1] + interval

    # Sureste
    def moveSE(self, interval=1):
        return self.posicion[0] + interval, self.posicion[1] - interval

    # Noroeste
    def moveNW(self, interval=1):
        return self.posicion[0] - interval, self.posicion[1] + interval

    # Suroeste
    def moveSW(self, interval=1):
        return self.posicion[0] - interval, self.posicion[1] - interval

    # Metodo que genera los nodos hijos
    def generateChildren(self, limits, interval=1):
        children = []
        for mov in range(8):
            if mov == 0:
                # Se valida si esta dentro del rango del canvas
                if self.posicion[1] < limits[1]:
                    # Si cumple se agrega la coordenada al array
                    children.append(self.moveUp(interval))
            elif mov == 1:
                if self.posicion[1] > limits[0]:
                    children.append(self.moveDown(interval))
            elif mov == 2:
                if self.posicion[0] > limits[2]:
                    children.append(self.moveLeft(interval))
            elif mov == 3:
                if self.posicion[0] < limits[3]:
                    children.append(self.moveRight(interval))
            elif mov == 4:
                if self.posicion[0] < limits[3] and self.posicion[1] < limits[1]:
                    children.append(self.moveNE(interval))
            elif mov == 5:
                if self.posicion[0] < limits[3] and self.posicion[1] > limits[0]:
                    children.append(self.moveSE(interval))
            elif mov == 6:
                if self.posicion[0] > limits[2] and self.posicion[1] < limits[1]:
                    children.append(self.moveNW(interval))
            elif mov == 7:
                if self.posicion[0] > limits[2] and self.posicion[1] > limits[0]:
                    children.append(self.moveSW(interval))
        return children

    # Metodo que controla los proceos del termite
    def checkMove(self, posChips, limits, interval, stepsWalk):
        children = self.generateChildren(limits, interval)  # Generamos hijos
        distances, posibleMoves = generateDistances(children, posChips)   # Generamos las distancia y posibles movimientos
        minDistance = getShortestDistance(distances)  # Sacamos la menor distancia
        self.posicion = posibleMoves[minDistance]  # Actualizamos nuestra posicion a las coordenadas con la menor distancia
        stepsWalk.append(self.posicion)  # Agregamos la coordenada al array de pasos dados


class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

    # Metodo que mueve la chip a un lugar aleatorio
    def moveChip(self, Chips, posChips, limits, r):
        x, y = r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3])  # Generamos x, y
        posChips[(x, y)] = posChips.pop(self.posicion)  # Actualizamos el diccionario de la posicion de las chips con la nueva coordenada
        Chips[posChips[(x, y)]].posicion = (x, y)  # Actualizamos la posicion de la chip
        return x, y  # Retornamos la posicion para graficar
