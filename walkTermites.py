def walk(steps, interval, termites, chips, maxLimit, stepLimit):
    import turtle as t
    import random as r
    import termite as te
    from time import sleep

    t.setworldcoordinates(-maxLimit - 2, -maxLimit - 2, maxLimit + 2, maxLimit + 2)
    t.title('EXAMEN P1 BRUNO DUEÑAS')
    t.hideturtle()
    limits = [-maxLimit, maxLimit, -maxLimit, maxLimit]
    termList = []  # Lista de objetos termitas
    chipList = []  # Lista de objetos chips
    clist = list()  # Lista de objetos turtle para los chips
    tlist = list()  # Lista de objetos turtle para las termitas
    stepsWalk = []  # Array que guarda los pasos recorridos
    counter = 0  # Contador que se utilizara para saber el intervalo de pasos
    win = False  # Variable para saber si ganamos

    """
    Crea una lista de objetos turtle y objetos termite
    """
    for pi in range(termites):
        termList.append(te.Termite(
            (r.randint(limits[0], limits[1]),
             r.randint(limits[2], limits[3]))))  # Se genera la termite en un lugar aleatorio
        # Asigna forma circulo a cada turtle
        tlist.append(t.Turtle(shape="turtle"))
        tlist[pi].color(termList[pi].getColor())  # Asigna color rojo a turtle
        tlist[pi].speed(0)  # Asigna la velocidad mas alta posible
        tlist[pi].shapesize(0.4, 0.6)  # Asigna el tamano de forma
        tlist[pi].penup()  # Pen up para no dejar rastro del camino
        # Va a la posicion inicial de cada termite
        tlist[pi].goto(termList[pi].getPos())

    """
    Crea una lista de objetos chips y sus turtle correspondientes
    """
    for pi in range(chips):
        chipList.append(
            te.Chip(pi, (r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        clist.append(t.Turtle(shape="square"))
        # Asigna color del chip a turtle
        clist[pi].color(chipList[pi].getColor())
        clist[pi].speed(0)  # Asigna la velocidad mas alta posible
        clist[pi].shapesize(0.2, 0.5)  # Asigna el tamano de forma
        clist[pi].penup()  # Pen up para no dejar rastro del camino
        # Va a la posicion inicial de cada chip
        clist[pi].goto(chipList[pi].getPos())

    screen = t.getscreen()  # Obtiene la pantalla de turtle para hacer tracer

    # for i, tc in enumerate(tlist):
    #    tc.goto(termList[i].getPos())

    for ts in range(steps):

        # print(len(chipList), len(posChips))
        # print(posChips)
        for i, tc in enumerate(tlist):
            posChips = {c.getPos(): c.index for c in chipList}
            # Validamos si la termite esta sobre una chip
            if termList[i].posicion in posChips:
                win = True
                break
            # Validamos si el contador es igual al intervalo de pasos en el que la chip debe cambiar su posicion
            if counter == stepLimit:
                counter = 0
                posC = chipList[i].moveChip(chipList, posChips, limits, r)
                # Actualizamos graficamente la posicion del chip
                if posC is not None:
                    ind = posChips[posC]
                    clist[ind].color(chipList[ind].getColor())
                    clist[ind].goto(chipList[ind].getPos())
            counter += 1
            # llamamos al metodo que controlara los procesos del termite
            termList[i].checkMove(posChips, limits, interval, stepsWalk)
            tc.color(termList[i].getColor())
            tc.goto(termList[i].getPos())
        # Si ganamos rompemos el ciclo de pasos
        tc.hideturtle()
        if win:
            break
        # sleep(0.5)
        # screen.update()
        screen.tracer(100)  # Se refrescara la pantalla cada 10 ejecuciones
    t.penup()
    t.colormode(255)
    # Ubicamos el cursor en la esquina superior izquierda para mostrar el mensaje
    t.goto(limits[0], limits[1] - 5)
    # Escribimos si ganamos o no
    if win:
        t.write('GANASTE', move=False, font=('monaco', 20, 'bold'), align='left')
    else:
        t.write('NO GANASTE', move=False, font=('monaco', 20, 'bold'), align='left')
    # Mostramos la lista de pasos que hemos recorrido
    print('Lista de pasos: ', stepsWalk)

    # GRAFICA LOS PASOS QUE DIO
    # Ubicamos el cursor en la posicion del primer paso para empeza a graficar la ruta
    t.goto(stepsWalk[0])
    t.pendown()
    # Por cada paso graficamos
    for step in stepsWalk:
        if win:
            # punto verde
            t.dot(8, 50, 205, 50)
        else:
            # punto amarillo
            t.dot(8, 250, 205, 50)
        t.goto(step)
        sleep(0.1)
        screen.tracer(1000000)
    # dejamos de dibujar
    t.penup()
    t.exitonclick()  # Al hacer clic sobre la ventana grafica se cerrara


def main(args):
    """
    Uso:
    python walkTermites.py steps interval termites chips canvas_limit
    Parametros:
    steps: numero de pasos
    inteval: longitud del paso
    termites: number of termites
    chips: number of chips
    canvas_limit: canvas x,y in (-canvas_limit, canvas_limit)
    Ejemplo:
    python walkTermites.py 1000 1 10 10 10 10
    """

    if len(args) == 6:
        steps = int(args[0])
        interval = int(args[1])
        termites = int(args[2])
        chips = int(args[3])
        canvas_limit = int(args[4])
        stepLimit = int(args[5])  # Nuevo argumento para saber cada cuantos pasos movemos aleatoriamente la chip
        walk(steps, interval, termites, chips, canvas_limit, stepLimit)
    else:
        print(main.__doc__)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
