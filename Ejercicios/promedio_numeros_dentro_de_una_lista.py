cantidad_numeros=int(input("Cuantos numero quieres introducir: "))

numeros_usuario=[]
numero_del_usuario=""
while len(numeros_usuario)<cantidad_numeros:
    while not numero_del_usuario.isdigit():
        numero_del_usuario=input("Introduce numero: ")
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario=""
    print("Añadido!")

contador=0
suma=0

for numero in numeros_usuario:
    suma+=int(numero)
    contador+=1
print("El promedio es {}".format(suma/contador))