
diccionario=[]

while 0!=1:
    eleccion = int(input("Que quieres hacer? 1.Añadir 2.Consultar: "))

    if eleccion == 1:
        print("---Añadiendo---")
        nombres=input("Cual es el nombre?: ")
        anos = input("Cual es el año?: ")
        diccionario.append([nombres, anos])
        print("Añadido!!! Posicion en la lsita de nombres/años: {}".format(len(diccionario)))
    if eleccion == 2 :
        print("---Consultando---")
        eleccion_consultar=int(input("Que metodo deseas usar, 1.Nombre, 2.Año, 3.Indice: "))

        if eleccion_consultar == 1:
            nombre=input("Introduce el nombre: ")
            for nombre_ano in diccionario:
                if nombre_ano[0]==nombre:
                    print("Nombre: {} Año: {}".format(nombre_ano[0], nombre_ano[1]))
        if eleccion_consultar == 2:
            nombre=input("Introduce el año: ")
            for nombre_ano in diccionario:
                if nombre_ano[1]==nombre:
                    print("Nombre: {} Año: {}".format(nombre_ano[0], nombre_ano[1]))
        if eleccion_consultar == 3:
            indice=int(input("Introduce el indice: "))-1

            print("Nombre: {} Año: {}".format(diccionario[indice][0], diccionario[indice][1]))