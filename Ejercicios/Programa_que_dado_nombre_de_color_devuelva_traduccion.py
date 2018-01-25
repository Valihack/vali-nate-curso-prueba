while 1!=0:

    colores={'azul':'blue', 'rojo':'red', 'amarillo':'yellow', 'negro':'black', 'blanco':'white', 'verde':'green'}
    nombre_color_espanol=input("De que color desea saber su traducción?: ")
    for color in colores:
        if color==nombre_color_espanol:
            print("La traduccion de {} es {}".format(nombre_color_espanol, colores[nombre_color_espanol] ))