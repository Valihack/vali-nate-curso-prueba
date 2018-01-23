def espar(numeros_usuario):
    lista_pares=[]
    j=0
    while j < len(numeros_usuario):
        if numeros_usuario[j] % 2==0:
            lista_pares.append(numeros_usuario[j])
        j+=1

    return lista_pares
cantidad_numeros=int(input("Introduce cuantos numeros quieres introducir: "))
numeros_usuario=[]
while len(numeros_usuario)<cantidad_numeros:
    numero_del_usuario=int(input("Introduce numero: "))
    numeros_usuario.append(numero_del_usuario)
    print("Añadido!")
print(numeros_usuario)
print(espar(numeros_usuario))