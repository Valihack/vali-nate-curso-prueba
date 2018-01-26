import random
#Se escoje el movimiento de la CPU de una posible partida ganadora
def copiar_turno_cpu(lista, lista2):
    tablero_completado=lista2
    tablero_anterior=lista
    i=0
    while i < 1:
        casilla=random.randrange(0, 9)
        if tablero_completado[casilla]==2 and tablero_anterior[casilla]==0:
            tablero_anterior[casilla]=2
            i=2
    return tablero_anterior

#La cpu crea una posible partida
def cpu (tablero_autocompletado):

    acaba = 0
    usuario=2
    cambiador=0

    while acaba<9:
        acaba=0
        pasara=0
        while pasara == 0:
            casilla = random.randrange(0, 9)
            if tablero_autocompletado[casilla]==0:
                tablero_autocompletado[casilla]=usuario
                pasara=1
        cambiador+=1
        if cambiador % 2 == 0:
            usuario=2
        else:
            usuario=1
        for i in range(0,9):
            if tablero_autocompletado[i]!=0:
             acaba+=1

    return tablero_autocompletado

#Se prueba la solucion
def probar_solucion(tablero_lista, turno):
    respuesta=0
    columna_1 = 0
    columna_2 = 1
    columna_3 = 2
    for i in range(0,3):
        if tablero_lista[columna_1]==turno and tablero_lista[columna_2]==turno and tablero_lista[columna_3]==turno:
            respuesta = 1
        columna_1 += 3
        columna_2 += 3
        columna_3 += 3
    fila_1 = 0
    fila_2 = 3
    fila_3 = 6
    for i in range(0,3):
        if tablero_lista[fila_1]==turno and tablero_lista[fila_2]==turno and tablero_lista[fila_3]==turno:
            respuesta = 1
        fila_1 += 1
        fila_2 += 1
        fila_3 += 1
    if (tablero_lista[0]==turno and tablero_lista[4]==turno and tablero_lista[8]==turno) or (tablero_lista[2]==turno and tablero_lista[4]==turno and tablero_lista[6]==turno):
        respuesta = 1
    return respuesta

# Se muestra el tablero
def mostar_tablero(tablero):
    x = 0
    y = 1
    z = 2
    for i in range(0, 3):
        print("|{}|{}|{}|".format(tablero[x], tablero[y], tablero[z]))
        print("________")
        x += 3
        y += 3
        z += 3

#Se crea el tablero
def crear_tablero():
    primer_tablero=[]
    for contador_for_creacion_tablero in range(0, 9):
        primer_tablero.append(0)
    return primer_tablero
                                                        #Inicializacion de variables

tablero_vacio=[]
tablero_de_juego=[]
tablero_autocompletado=[]
tablero=[]
nombre_usuario=input("Como te llamas? ")                #Pide el nombre del jugador
quien_empieza=random.randrange(0,2)                     #Se elige quien comienza#
print("Ahora se decide aleatoriamente quien empieza")
texto_carga="Cargando"
for j in range(0,4):                                     #Imprime el cargando
    print(texto_carga)
    texto_carga=texto_carga+"."
ganador = 0                                              #Se mantiene en ganador=0 hasta que en la comprobacion del tablero gana alguien
posible_ganador = 0                                      #Se mantiene en 0 hasta que la CPU encuentra una posible jugada ganadora
tablero_vacio=list(crear_tablero())                      #Se añaden nueve ceros a la lista
gana_cpu=0
while ganador<1:                                         #Codigo del funcionamiento de los turnos
    indice=0
    mostar_tablero(tablero_vacio)
    if quien_empieza == 1:
        casilla=int(input("Introduce tu casilla: "))-1     #Turno de la persona#casilla = int(input("En que casilla quieres tu ficha: "))-1#Seleccion de la casilla
        tablero_vacio[casilla]=1                         #Se añade ficha a casilla
        if probar_solucion(tablero_vacio, 1) == 1:       #Se comprueba si el usuario ha ganado
            ganador=1
            break
    quien_empieza = 0
    if quien_empieza==0:                                 #Turno de la cpu#
        while posible_ganador == 0:                      #Mientras no se encuentre una posible partida ganadora
            tablero_de_juego = list(tablero_vacio)       #Copia de seguridad del tablero original#
            tablero_autocompletado=list(cpu(tablero_de_juego))
            posible_ganador=probar_solucion(tablero_autocompletado, 2)#Se decide si puede ganar
        tablero_vacio = list(copiar_turno_cpu(tablero_vacio, tablero_autocompletado))#Se copia la jugada del CPU
        posible_ganador = 0                             #Resetea el bucle de posible ganadorprint(probar_solucion(tablero_vacio, 2))
        if probar_solucion(tablero_vacio, 2)==1:        #Comprueba si ha ganado el CPU
            ganador=2
            break
    quien_empieza = 1
if ganador == 1:                                        #Si el ganador es la persona
    print("Enhorabuena {} has ganado!".format(nombre_usuario))
elif ganador == 2:                                      #Si el ganador es la CPU
    print("Te ha ganado un codigo hecho en un par de horas pringao!")
mostar_tablero(tablero_vacio)