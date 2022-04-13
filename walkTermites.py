def walk(steps, interval, termites, chips, maxLimit):
    import turtle as t
    import random as r
    import termite as te
    from time import sleep

    t.setworldcoordinates(-maxLimit - 2, -maxLimit - 2, maxLimit + 2, maxLimit + 2)
    limits = [-maxLimit, maxLimit, -maxLimit, maxLimit]
    termList = []  # Lista de objetos termitas
    chipList = []  # Lista de objetos chips
    clist = list()  # Lista de objetos turtle para los chips
    tlist = list()  # Lista de objetos turtle para las termitas

    """
    Crea una lista de objetos turtle y objetos termite
    """
    for pi in range(termites):
        termList.append(te.Termite(
            (r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
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
        print('\r' + str(ts), end='')

        # print(len(chipList), len(posChips))
        # print(posChips)
        for i, tc in enumerate(tlist):
            # postions of all chips in the canvas
            posChips = {c.getPos(): c.index for c in chipList}

            posT = termList[i].checkChip(chipList, posChips, r, limits, interval)

            # Change color of chip if pickChip NOT returns None
            if posT is not None:
                # if ts > steps - 100:
                ind = posChips[posT]
                clist[ind].color(chipList[ind].getColor())
                clist[ind].goto(chipList[ind].getPos())

            termList[i].move(r, limits, interval)

            # if ts > steps - 100:
            tc.color(termList[i].getColor())
            tc.goto(termList[i].getPos())

        sleep(0.6)
        # screen.update()
        screen.tracer(100)  # Se refrescara la pantalla cada 10 ejecuciones

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
    python walkTermites.py 1000 1 10 10 10
    """

    if len(args) == 5:
        steps = int(args[0])
        interval = int(args[1])
        termites = int(args[2])
        chips = int(args[3])
        canvas_limit = int(args[4])
        walk(steps, interval, termites, chips, canvas_limit)
    else:
        print(main.__doc__)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
