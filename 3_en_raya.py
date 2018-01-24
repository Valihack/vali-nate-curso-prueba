import random

def tablero_final(tablero, tablero_nuevo):
    i=0
    while i < 1:
        casilla=random.randrange(0, 9)
        if tablero_nuevo[casilla]==2 and tablero[casilla]==0:
            tablero[casilla]=2
            i=2

    return tablero

def cpu (tablero_nuevo):
    acaba = 0
    usuario=2
    cambiador=0
    while acaba<9:
        acaba=0
        pasara=0
        while pasara == 0:
            casilla = random.randrange(0, 9)
            if tablero_nuevo[casilla]==0:
                tablero_nuevo[casilla]=usuario
                pasara=1
        cambiador+=1
        if cambiador % 2 == 0:
            usuario=2
        else:
            usuario=1
        for i in range(0,9):
            if tablero_nuevo[i]!=0:
             acaba+=1
    return tablero_nuevo

def probar_solucion(tablero, turno):
    columna_1 = 0
    columna_2 = 1
    columna_3 = 2
    for i in range(0,3):
        if tablero[columna_1]==turno and tablero[columna_2]==turno and tablero[columna_3]==turno:
            return 1
        columna_1 += 3
        columna_2 += 3
        columna_3 += 3
    fila_1 = 0
    fila_2 = 3
    fila_3 = 6
    for i in range(0,3):
        if tablero[fila_1]==turno and tablero[fila_2]==turno and tablero[fila_3]==turno:
            return 1
        fila_1 += 1
        fila_2 += 1
        fila_3 += 1
    if (tablero[0]==turno and tablero[4]==turno and tablero[8]==turno) or (tablero[2]==turno and tablero[4]==turno and tablero[6]==turno):
        return 1
    else:
        return 0

nombre_usuario=input("Como te llamas? ")
primer_tablero=[]
tablero=[]
tablero_nuevo=[]

#Se crea el tablero#
k=0
for k in range(0,9):
    primer_tablero.append(0)
print(primer_tablero)
#Se elige quien comienza#
print("Ahora se decide aleatoriamente quien empieza")
texto_carga="Cargando"
for j in range(0,4):
    print(texto_carga)
    texto_carga=texto_carga+"."
quien_empieza=random.randrange(0,2)

#Turnos#
ganador = 0
posible_ganador = 0
while ganador<1:
    # Se muestra el tablero#
    x = 0
    y = 1
    z = 2
    for i in range(0, 3):
        print("|{}|{}|{}|".format(primer_tablero[x],primer_tablero[y], primer_tablero[z]))
        print("________")
        x += 3
        y += 3
        z += 3
    # Turno de la persona#
    if quien_empieza == 1:
        primer_tablero[int(input("En que casilla quieres tu ficha: "))]=1
        ganador=probar_solucion(primer_tablero, 1)
        quien_empieza=0
    tablero=primer_tablero
    print(tablero)
    # Turno de la cpu#
    if quien_empieza==0:
        while posible_ganador ==0:
            # Copia de seguridad del tablero original#
            tablero_nuevo = tablero
            print(tablero_nuevo)
            tablero_nuevo = cpu(tablero_nuevo)
            posible_ganador=probar_solucion(tablero_nuevo, 2)

        tablero = tablero_final(tablero, tablero_nuevo)
        primer_tablero=tablero
        ganador = probar_solucion(tablero, 2)
        quien_empieza = 1
        if ganador == 1:
            ganador = 2
# Se muestra el tablero Final#
print("Así ha acabado la partida, quieres volver a jugar? Yes/No")
x = 0
y = 1
z = 2
for i in range(0, 3):
    print("|{}|{}|{}|".format(tablero[x], tablero[y], tablero[z]))
    print("________")
    x += 3
    y += 3
    z += 3
if ganador == 1:
    print("Enhorabuena has ganado!")
elif ganador == 2:
    print("Te ha ganado un codigo hecho en un par de horas pringao!")