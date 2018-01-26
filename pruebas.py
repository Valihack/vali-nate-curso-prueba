def probar_solucion(tablero_lista, turno):
    columna_1 = 0
    columna_2 = 1
    columna_3 = 2
    for i in range(0,3):
        if tablero_lista[columna_1]==turno and tablero_lista[columna_2]==turno and tablero_lista[columna_3]==turno:
            return 1
        columna_1 += 3
        columna_2 += 3
        columna_3 += 3
    fila_1 = 0
    fila_2 = 3
    fila_3 = 6
    for i in range(0,3):
        if tablero_lista[fila_1]==turno and tablero_lista[fila_2]==turno and tablero_lista[fila_3]==turno:
            return 1
        fila_1 += 1
        fila_2 += 1
        fila_3 += 1
    if (tablero_lista[0]==turno and tablero_lista[4]==turno and tablero_lista[8]==turno) or (tablero_lista[2]==turno and tablero_lista[4]==turno and tablero_lista[6]==turno):
        return 1
    else:
        return 0

lista=[1,1,1,2,1,1,2,2,1]
print(probar_solucion(lista,1))